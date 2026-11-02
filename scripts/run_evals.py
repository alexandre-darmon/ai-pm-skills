#!/usr/bin/env python3
"""Run `claude plugin eval` on skills and apply the repo's pass rules (PRD §11.3).

Usage: python3 scripts/run_evals.py [--full] [--all] [--runs N] [--base REF] [skill_dir ...]

Which skills: the folders given, else every skill in skills/ (--all), else the
skills and drafts changed since REF (default origin/main).
Arms: --full runs with and without the skill. Otherwise the "without" scores are
reused from baselines/<skill>.json when its cases, model and judge still match;
the "without" arm never sees the skill, so only those can change it.
A skill fails if a case scores below its eval_threshold, a graders/redline-* grader
misses in any run with the skill, a negative case fires the skill, or its mean delta
is <= 0 (negative cases left out: without the skill they cannot fire).
The report also lists graders that do not tell the two arms apart (a warning, not a failure).

Writes eval-out/<skill>.json (the baseline format: commit it to baselines/ to
freeze a baseline) and prints a Markdown summary, also to $GITHUB_STEP_SUMMARY.
Exits 1 if a skill fails.
"""
import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate_skills import read_frontmatter  # noqa: E402

ROOT = Path(__file__).parent.parent
MODEL = "claude-sonnet-5-5"
JUDGE = "claude-haiku-5-5"
MAX_COST_USD = 3  # per skill and run, 3 cases x 2 arms cost about 0.5 on the API
REDLINE = "redline-"


def changed_skills(base: str) -> list[Path]:
    names = subprocess.run(["git", "diff", "--name-only", f"{base}...HEAD"], cwd=ROOT,
                           capture_output=True, text=True, check=True).stdout.split()
    folders = {ROOT / p.split("/")[0] / p.split("/")[1] for p in names
               if p.split("/")[0] in ("skills", "drafts") and p.count("/") >= 2}
    return sorted(f for f in folders if (f / "SKILL.md").is_file())


def cases_hash(folder: Path) -> str:
    """Fingerprint of the cases and graders: a change means stored "without" scores are stale."""
    h = hashlib.sha256()
    evals = folder / "evals"
    # results/ is output and fixtures/ is only read by the validator: neither changes a run.
    for f in sorted(p for p in evals.rglob("*") if p.is_file() and not {"results", "fixtures"} & set(p.relative_to(evals).parts)):
        h.update(str(f.relative_to(evals)).encode() + b"\0" + f.read_bytes())
    return h.hexdigest()


def skill_check(grader: dict) -> str | None:
    """'fires' for the grader proving the skill was called (an indicator), 'silent' for one proving it was not (max: 0)."""
    if grader["type"] != "tool_used" or grader["config"].get("tool") != "Skill":
        return None
    return "silent" if grader["config"].get("max") == 0 else "fires"


def passes(runs: list[dict], name: str) -> int:
    return sum(not r.get("error") and any(g["name"] == name and g["passed"] for g in r.get("graders", [])) for r in runs)


def run_score(run: dict, indicators: set[str]) -> float:
    """Weighted share of graders passed, leaving out the skill-fired indicator so both arms score alike."""
    if run.get("error"):
        return 0.0
    graders = [g for g in run.get("graders", []) if g["name"] not in indicators]
    total = sum(g["weight"] for g in graders)
    return sum(g["weight"] for g in graders if g["passed"]) / total if total else 0.0


def mean(xs: list[float]) -> float | None:
    return sum(xs) / len(xs) if xs else None


def summarise(result: dict, skill: str, chash: str) -> dict:
    cases = {}
    for case in result.get("cases", []):
        indicators = {g["name"] for g in case["graders"] if skill_check(g) == "fires"}
        silent = {g["name"] for g in case["graders"] if skill_check(g) == "silent"}
        arms = case.get("arms") or {"with": case.get("runs", [])}
        with_runs, without_runs = arms.get("with", []), arms.get("without", [])
        scored = [g["name"] for g in case["graders"] if g["name"] not in indicators]
        cases[case["name"]] = {
            "score": mean([run_score(r, indicators) for r in with_runs]),
            "scoreWithout": mean([run_score(r, indicators) for r in without_runs]),
            "fired": sum(any((g["name"] in indicators and g["passed"]) or (g["name"] in silent and not g["passed"])
                             for g in r.get("graders", [])) for r in with_runs),
            "runs": len(with_runs),
            "runsWithout": len(without_runs),
            "negative": bool(silent),
            # runs passed per grader, [with, without]: the discrimination report and red-line rule read it
            "graders": {n: [passes(with_runs, n), passes(without_runs, n) if without_runs else None] for n in scored},
        }
    return {"skill": skill, "model": MODEL, "judgeModel": JUDGE, "claudeVersion": result.get("claudeVersion"),
            "date": str(result.get("startedAt", ""))[:10], "casesHash": chash, "partial": result.get("partial", False),
            "costUsd": result.get("costUsd"), "cases": cases}


def verdict(summary: dict, threshold: float, baseline: dict | None) -> list[str]:
    """Fill in missing "without" scores from the baseline, then return the failures."""
    failures = []
    if summary["partial"]:
        failures.append("run stopped early (cost ceiling or error)")
    if not summary["cases"]:
        failures.append("no case ran")
    deltas = []
    for name, c in summary["cases"].items():
        if c["scoreWithout"] is None and baseline:
            b = baseline["cases"].get(name, {})
            c["scoreWithout"], c["runsWithout"] = b.get("scoreWithout"), b.get("runsWithout", 0)
            for n, counts in c.get("graders", {}).items():
                counts[1] = b.get("graders", {}).get(n, [None, None])[1]
        if c["score"] is None:
            failures.append(f"{name}: no run")
            continue
        if c.get("negative"):  # an errored run proves nothing either: only a passed silent grader counts
            missed = c["runs"] - min((w for w, _ in c["graders"].values()), default=0)
            if missed:
                failures.append(f"{name}: the skill fired, or the run errored, on a request it should leave alone ({missed}/{c['runs']} runs)")
            continue
        if c["score"] < threshold:
            failures.append(f"{name}: score {c['score']:.2f} < threshold {threshold:.2f}")
        for n, (passed, _) in c.get("graders", {}).items():
            if n.startswith(REDLINE) and passed < c["runs"]:
                failures.append(f"{name}: red line {n} missed in {c['runs'] - passed}/{c['runs']} runs")
        if c["scoreWithout"] is None:
            failures.append(f"{name}: no score without the skill (run with --full)")
        else:
            c["delta"] = c["score"] - c["scoreWithout"]
            deltas.append(c["delta"])
    summary["meanDelta"] = delta = mean(deltas)
    if delta is not None and delta <= 0:
        failures.append(f"mean delta {delta:+.2f}: the skill adds nothing over the model alone")
    return failures


def warnings(summary: dict) -> list[str]:
    """Graders that pass, or fail, in every run of both arms measure the model, not the skill."""
    found = []
    for name, c in summary["cases"].items():
        if c.get("negative") or not c.get("runs") or not c.get("runsWithout"):
            continue
        for n, (w, wo) in c.get("graders", {}).items():
            if wo is None:
                continue
            if w == c["runs"] and wo == c["runsWithout"]:
                found.append(f"{name}/{n}: passes without the skill too: it measures the model, not the skill")
            elif w == 0 and wo == 0:
                found.append(f"{name}/{n}: fails with and without the skill: check the grader")
    return found


def load_baseline(skill: str, chash: str) -> dict | None:
    path = ROOT / "baselines" / f"{skill}.json"
    if not path.is_file():
        return None
    b = json.loads(path.read_text())
    return b if (b.get("casesHash"), b.get("model"), b.get("judgeModel")) == (chash, MODEL, JUDGE) else None


def evaluate(folder: Path, full: bool, out: Path, runs: int = 1) -> tuple[dict, list[str], str]:
    fm, _ = read_frontmatter(folder / "SKILL.md")
    skill, threshold = fm["name"], float(fm["eval_threshold"])
    chash = cases_hash(folder)
    baseline = None if full else load_baseline(skill, chash)
    ablation = "none" if baseline else "with-without"
    raw = out / f"{skill}.raw.json"
    cmd = ["claude", "plugin", "eval", str(folder), "--trust-plugin", "--no-publish", "--json", str(raw),
           "--runs", str(runs), "--threshold", str(threshold), "--ablation", ablation,
           "--model", MODEL, "--judge-model", JUDGE, "--max-cost-usd", str(MAX_COST_USD)]
    print("$", " ".join(cmd), flush=True)
    code = subprocess.run(cmd, cwd=ROOT).returncode
    if not raw.is_file():
        return {"skill": skill, "cases": {}}, [f"claude plugin eval exited {code} without results"], ablation
    summary = summarise(json.loads(raw.read_text()), skill, chash)
    failures = verdict(summary, threshold, baseline)
    (out / f"{skill}.json").write_text(json.dumps(summary, indent=2) + "\n")
    return summary, failures, ablation


def report(rows: list[tuple[dict, list[str], str]]) -> str:
    fmt = lambda x: "—" if x is None else f"{x:.2f}"  # noqa: E731
    lines = ["| Skill | Case | With | Without | Delta | Fired |", "| --- | --- | --- | --- | --- | --- |"]
    for summary, _, ablation in rows:
        reused = " (reused)" if ablation == "none" else ""
        for name, c in summary["cases"].items():
            fired = f"{c['fired']}/{c['runs']}" + (" (must be 0)" if c.get("negative") else "")
            without = "—" if c.get("negative") else f"{fmt(c['scoreWithout'])}{reused}"
            lines.append(f"| {summary['skill']} | {name} | {fmt(c['score'])} | {without} "
                         f"| {fmt(c.get('delta'))} | {fired} |")
    for summary, failures, _ in rows:
        lines.append(f"\n**{summary['skill']}: {'FAIL' if failures else 'pass'}**"
                     + "".join(f"\n- {f}" for f in failures))
        notes = warnings(summary)
        if notes:
            lines.append("\nGraders that do not tell the arms apart (warning):" + "".join(f"\n- {n}" for n in notes))
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("skills", nargs="*", type=Path)
    ap.add_argument("--full", action="store_true", help="run both arms, ignore stored baselines")
    ap.add_argument("--all", action="store_true", help="every skill in skills/")
    ap.add_argument("--runs", type=int, default=1, help="runs per case; 3 confirms a red-line or discrimination finding")
    ap.add_argument("--base", default="origin/main")
    ap.add_argument("--out", type=Path, default=ROOT / "eval-out")
    args = ap.parse_args()

    if args.skills:
        folders = [p.resolve() for p in args.skills]
    elif args.all:
        folders = sorted(p for p in (ROOT / "skills").glob("*") if (p / "SKILL.md").is_file())
    else:
        folders = changed_skills(args.base)
    if not folders:
        print("No skill to evaluate.")
        return 0

    args.out.mkdir(parents=True, exist_ok=True)
    rows = [evaluate(f, args.full, args.out, args.runs) for f in folders]
    text = report(rows)
    print(text)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as f:
            f.write(text)
    return 1 if any(failures for _, failures, _ in rows) else 0


if __name__ == "__main__":
    sys.exit(main())
