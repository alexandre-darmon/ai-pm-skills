#!/usr/bin/env python3
"""Run `claude plugin eval` on skills and apply the repo's pass rules (PRD §11.3).

Usage: python3 scripts/run_evals.py [--full] [--all] [--runs N] [--base REF] [--regrade] [skill_dir ...]

Which skills: the folders given, else every skill in skills/ (--all), else the
skills and drafts changed since REF (default origin/main).
Arms: --full runs with and without the skill. Otherwise the "without" scores are
reused from baselines/<skill>.json when its cases, model and judge still match;
the "without" arm never sees the skill, so only those can change it.
A skill fails if a case scores below its eval_threshold, a graders/redline-* grader
misses in any run with the skill, a negative case fires the skill, or its mean delta
is under 10 points (negative cases left out: without the skill they cannot fire).
The report also lists graders that do not tell the two arms apart (a warning, not a failure).

Writes eval-out/<skill>.json (the baseline format: commit it to baselines/ to
freeze a baseline) and prints a Markdown summary, also to $GITHUB_STEP_SUMMARY.
Every paid run also saves each run's final answer to eval-out/answers/<skill>/.
--regrade re-scores those saved answers with the current graders: no model call,
no cost. It checks grader changes only; after a change to the skill itself the
answers are stale, and the report says so.
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
from validate_skills import read_frontmatter, regex_passes, run_js_regex  # noqa: E402

ROOT = Path(__file__).parent.parent
MODEL = "claude-sonnet-5-5"
JUDGE = "claude-haiku-5-5"
MAX_COST_USD = 3  # per skill and run, 3 cases x 2 arms cost about 0.5 on the API
REDLINE = "redline-"
MIN_DELTA = 0.10  # a skill must beat the model alone by 10 points (PRD §11.3)


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
    if delta is not None and round(delta, 4) < MIN_DELTA:
        failures.append(f"mean delta {delta:+.2f} is under {MIN_DELTA:+.2f}: the skill adds too little over the model alone")
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


def skill_hash(folder: Path) -> str:
    """Fingerprint of what the agent reads (SKILL.md, references, templates): a change makes saved answers stale."""
    h = hashlib.sha256()
    for f in sorted(p for p in folder.rglob("*") if p.is_file() and "evals" not in p.relative_to(folder).parts):
        h.update(str(f.relative_to(folder)).encode() + b"\0" + f.read_bytes())
    return h.hexdigest()


def final_answer(trace: str | None) -> str:
    path = Path(trace) if trace else None
    if not path or not path.is_file():
        return ""
    results = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if '"type":"result"' in line.replace(" ", "")]
    return results[-1].get("result", "") if results else ""


def save_answers(result: dict, folder: Path, out: Path) -> None:
    """Keep each run's final answer and its non-regex grader results, so --regrade can re-score them for free."""
    runs = {}
    for case in result.get("cases", []):
        regex = {g["name"] for g in case["graders"] if g["type"] == "regex"}
        for arm, rs in (case.get("arms") or {"with": case.get("runs", [])}).items():
            for i, r in enumerate(rs, start=1):
                name = f"{case['name']}/{arm}-{i}.md"
                (out / name).parent.mkdir(parents=True, exist_ok=True)
                (out / name).write_text(final_answer(r.get("tracePath")), encoding="utf-8")
                runs.setdefault(case["name"], {}).setdefault(arm, []).append({"file": name, "error": r.get("error"), "graders": {
                    g["name"]: g["passed"] for g in r.get("graders", []) if g["name"] not in regex}})
    meta = {"startedAt": result.get("startedAt"), "claudeVersion": result.get("claudeVersion"), "skillHash": skill_hash(folder)}
    (out / "runs.json").write_text(json.dumps({**meta, "cases": runs}, indent=2) + "\n")


def case_graders(folder: Path, case: str) -> list[dict]:
    graders = []
    for f in sorted((folder / "evals" / case / "graders").glob("*.md")):
        fm, body = read_frontmatter(f)
        if fm.get("type") == "regex" and "pattern" not in fm and body.strip():
            fm["pattern"] = body.strip()  # the harness reads the body as the pattern when the key is absent
        graders.append({"name": fm.get("name", f.stem), "type": fm["type"], "weight": fm.get("weight", 1),
                        "config": {k: v for k, v in fm.items() if k not in ("type", "weight", "name")}})
    return graders


def regrade(folder: Path, answers: Path) -> dict:
    """Score saved answers with the current graders, in the harness result format. Tool graders keep their recorded result."""
    saved = json.loads((answers / "runs.json").read_text())
    cases = []
    for name, arms in saved["cases"].items():
        graders = case_graders(folder, name)
        regex = [g for g in graders if g["type"] == "regex"]
        out_arms = {}
        for arm, rs in arms.items():
            texts = [(answers / r["file"]).read_text(encoding="utf-8") for r in rs]
            res = run_js_regex([(g["config"]["pattern"], str(g["config"].get("flags", ""))) for g in regex], texts) if regex else []
            out_arms[arm] = [{"error": r["error"], "graders": [
                {"name": g["name"], "weight": g["weight"], "passed": not isinstance(res[k], str) and regex_passes(g["config"], *res[k][i])}
                for k, g in enumerate(regex)] + [
                {"name": g["name"], "weight": g["weight"], "passed": r["graders"][g["name"]]}
                for g in graders if g["type"] != "regex" and g["name"] in r["graders"]]} for i, r in enumerate(rs)]
        cases.append({"name": name, "graders": graders, "arms": out_arms})
    return {"cases": cases, "partial": False, "costUsd": 0, "claudeVersion": saved.get("claudeVersion"),
            "startedAt": saved.get("startedAt"), "stale": saved.get("skillHash") != skill_hash(folder)}


def load_baseline(skill: str, chash: str) -> dict | None:
    path = ROOT / "baselines" / f"{skill}.json"
    if not path.is_file():
        return None
    b = json.loads(path.read_text())
    return b if (b.get("casesHash"), b.get("model"), b.get("judgeModel")) == (chash, MODEL, JUDGE) else None


def evaluate(folder: Path, full: bool, out: Path, runs: int = 1, offline: bool = False) -> tuple[dict, list[str], str]:
    fm, _ = read_frontmatter(folder / "SKILL.md")
    skill, threshold = fm["name"], float(fm["eval_threshold"])
    chash = cases_hash(folder)
    answers = out / "answers" / skill
    if offline:
        if not (answers / "runs.json").is_file():
            return {"skill": skill, "cases": {}}, [f"no saved answers in {answers}: run a paid eval first"], "regrade"
        result = regrade(folder, answers)
        summary = summarise(result, skill, chash)
        summary["regraded"], summary["stale"] = True, result["stale"]
        failures = verdict(summary, threshold, load_baseline(skill, chash))
        return summary, failures, "regrade"
    baseline = None if full else load_baseline(skill, chash)
    ablation = "none" if baseline else "with-without"
    raw = out / f"{skill}.raw.json"
    cmd = ["claude", "plugin", "eval", str(folder), "--trust-plugin", "--no-publish", "--json", str(raw),
           "--runs", str(runs), "--threshold", str(threshold), "--ablation", ablation,
           "--model", MODEL, "--judge-model", JUDGE, "--max-cost-usd", str(MAX_COST_USD), "--keep-temp"]
    print("$", " ".join(cmd), flush=True)
    code = subprocess.run(cmd, cwd=ROOT).returncode
    if not raw.is_file():
        return {"skill": skill, "cases": {}}, [f"claude plugin eval exited {code} without results"], ablation
    result = json.loads(raw.read_text())
    save_answers(result, folder, answers)
    summary = summarise(result, skill, chash)
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
        if summary.get("regraded"):
            lines.append(f"\n{summary['skill']}: regraded offline from saved answers (no model call)"
                         + (". The skill changed since these answers: this checks the graders only." if summary.get("stale") else "."))
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
    ap.add_argument("--regrade", action="store_true", help="re-score the answers saved by the last paid run: free, no model call")
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
    rows = [evaluate(f, args.full, args.out, args.runs, args.regrade) for f in folders]
    text = report(rows)
    print(text)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as f:
            f.write(text)
    return 1 if any(failures for _, failures, _ in rows) else 0


if __name__ == "__main__":
    sys.exit(main())
