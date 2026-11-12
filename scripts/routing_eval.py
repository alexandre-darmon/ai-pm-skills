#!/usr/bin/env python3
"""Paid routing check: with every catalog skill and draft installed together, does the model load the right one?

Usage: python3 scripts/routing_eval.py [--runs N] [--case GLOB] [-j N] [--max-cost USD] [--dry-run | --summarise]

Builds one temporary plugin in eval-out/routing/plugin/ (kept there during the run: the agent reads the skill
files in place):
  .claude-plugin/plugin.json   name "ai-pm-routing"
  skills/<name>/               a copy of each skills/ and drafts/ folder WITHOUT its evals/ (their cases would run too)
  evals/<case id>/             one case per entry of routing/cases.yaml: prompt.md + graders/routes.md
The grader is a tool_used Skill grader: min 1 call anchored on the expected skill, or, for an out-of-scope
case ("none"), max 0 calls to any skill. Then runs claude plugin eval on it with the model and judge of
scripts/run_evals.py and the "with" arm only (--ablation none: without the plugin no skill can fire).

Writes eval-out/routing/raw.json (harness result), calls.json (the Skill calls of every run, read from the traces
right after the run: the traces live in temporary folders that get cleaned up), summary.json (accuracy, per-zone,
confusion, per-case calls) and confusion.md. The confusion reads which skill the agent loaded first.
--dry-run builds the folder and prints the command: free. --summarise rebuilds summary.json and confusion.md
from raw.json and calls.json: free; without calls.json it reads the traces again and stops if one is gone,
rather than counting a lost trace as "no skill loaded". Never run in CI: it costs about one answer per case and run.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from routing_check import NONE, load_cases  # noqa: E402
from run_evals import JUDGE, MODEL  # noqa: E402
from validate_skills import TRIGGER  # noqa: E402

ROOT = Path(__file__).parent.parent
OUT = ROOT / "eval-out" / "routing"
PLUGIN = "ai-pm-routing"
UNKNOWN = "unknown (trace lost)"
ANY_SKILL = r'"skill"\s*:\s*"'
COST_PER_RUN = 0.25  # USD ceiling per agent run, about twice the cost of one answer in the skills' own runs


def skill_folders(root: Path) -> list[Path]:
    return sorted(p for d in ("skills", "drafts") for p in (root / d).glob("*") if (p / "SKILL.md").is_file())


def case_files(case: dict, runs: int, max_turns: int) -> dict[str, str]:
    """prompt.md and graders/routes.md of one routing case, in the native claude plugin eval format."""
    expected = case["expected"]
    outcome = "Answers without loading any skill." if expected == NONE else f"Loads the {expected} skill."
    prompt = (f"---\nname: {case['id']}\n"
              f"description: {json.dumps('Routing, ' + case.get('zone', '') + ' (source - anonymised routing set, 2026)')}\n"
              f"tags: [routing, {case.get('zone') or 'none'}]\n"
              f"expected_outcome: {json.dumps(outcome)}\nruns: {runs}\nmax_turns: {max_turns}\n"
              f"allowed_tools: [Read, Glob, Grep, Skill]\n---\n\n{case['request'].strip()}\n")
    if expected == NONE:  # min 0 too: the default min is 1
        grader = f"---\ntype: tool_used\ntool: Skill\ninput_match: '{ANY_SKILL}'\nmin: 0\nmax: 0\n---\n"
    else:
        grader = f"---\ntype: tool_used\ntool: Skill\ninput_match: '{TRIGGER.format(name=expected)}'\nmin: 1\n---\n"
    return {"prompt.md": prompt, "graders/routes.md": grader}


def build_plugin(root: Path, dest: Path, cases: list[dict], runs: int, max_turns: int) -> Path:
    shutil.rmtree(dest, ignore_errors=True)
    (dest / ".claude-plugin").mkdir(parents=True)
    (dest / ".claude-plugin" / "plugin.json").write_text(json.dumps({
        "name": PLUGIN, "version": "0.0.0",
        "description": "Routing test: every catalog skill and draft, without their own eval cases."}, indent=2) + "\n")
    for folder in skill_folders(root):  # copies, not symlinks: a link to the folder would bring its evals/ along
        shutil.copytree(folder, dest / "skills" / folder.name, ignore=shutil.ignore_patterns("evals", "__pycache__", "*.pyc"))
    for case in cases:
        for rel, text in case_files(case, runs, max_turns).items():
            path = dest / "evals" / case["id"] / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
    return dest


def command(plugin: Path, raw: Path, runs: int, max_cost: float, jobs: int, case_glob: str | None) -> list[str]:
    """Same model, judge and flags as scripts/run_evals.py, with arm only."""
    cmd = ["claude", "plugin", "eval", str(plugin), "--trust-plugin", "--no-publish", "--json", str(raw),
           "--runs", str(runs), "--threshold", "1", "--ablation", "none",
           "--model", MODEL, "--judge-model", JUDGE, "--max-cost-usd", f"{max_cost:g}", "--keep-temp", "-j", str(jobs)]
    return cmd + (["--case", case_glob] if case_glob else [])


def skill_calls(trace: str | None) -> list[str]:
    """Skills the agent loaded, in order, from a stream-json trace; plugin prefix dropped."""
    path = Path(trace) if trace else None
    if not path or not path.is_file():
        return []
    calls = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if '"Skill"' not in line:
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        content = (event.get("message") or {}).get("content") if isinstance(event, dict) else None
        for block in content if isinstance(content, list) else []:
            if isinstance(block, dict) and block.get("type") == "tool_use" and block.get("name") == "Skill":
                name = str((block.get("input") or {}).get("skill", ""))
                calls.append(name.split(":")[-1])
    return calls


def case_runs(case: dict) -> list[dict]:
    return (case.get("arms") or {}).get("with") or case.get("runs", [])


def extract_calls(result: dict) -> tuple[dict[str, list], list[str]]:
    """{case name: [Skill calls of run i, or None when an errored run left no trace]} and the traces that are gone."""
    calls, missing = {}, []
    for case in result.get("cases", []):
        per_run = []
        for i, r in enumerate(case_runs(case)):
            trace = r.get("tracePath")
            if trace and Path(trace).is_file():
                per_run.append(skill_calls(trace))
            elif r.get("error"):
                per_run.append(None)  # the run failed: counted as an error, no calls to read
            else:
                per_run.append(None)
                missing.append(f"{case.get('name')} run {i + 1}: {trace or 'no tracePath'}")
        calls[case.get("name")] = per_run
    return calls, missing


def summarise(result: dict, cases: list[dict], calls: dict[str, list] | None = None) -> dict:
    """calls: from calls.json (extract_calls); without it the traces are read now, so they must still exist."""
    if calls is None:
        calls, _ = extract_calls(result)
    by_id = {c["id"]: c for c in cases}
    rows, confusion, zones = [], Counter(), defaultdict(lambda: [0, 0])
    for case in result.get("cases", []):
        spec = by_id.get(case["name"])
        if not spec:
            continue
        runs, recorded = case_runs(case), calls.get(case["name"], [])
        expected, firsts, correct, first_ok, errors = spec["expected"], [], 0, 0, 0
        for i, r in enumerate(runs):
            loaded = recorded[i] if i < len(recorded) else None
            # a run whose trace was lost is unknown, never "no skill loaded" (that would read as a routing error)
            first = UNKNOWN if loaded is None and not r.get("error") else (loaded[0] if loaded else NONE)
            loaded = loaded or []
            firsts.append({"first": first, "all": loaded, "error": r.get("error")})
            if r.get("error"):
                errors += 1
                continue
            # the grader says whether the expected skill fired at all; the trace says which came first
            ok = any(g.get("passed") for g in r.get("graders", []))
            correct += ok
            first_ok += ok and first == expected
            confusion[(expected, first)] += 1
        zone = spec.get("zone", "")
        zones[zone][0] += correct
        zones[zone][1] += len(runs)
        rows.append({"id": spec["id"], "zone": zone, "expected": expected, "runs": len(runs), "correct": correct,
                     "firstCorrect": first_ok, "errors": errors, "calls": firsts})
    total = sum(r["runs"] for r in rows)
    return {"model": MODEL, "claudeVersion": result.get("claudeVersion"), "date": str(result.get("startedAt", ""))[:10],
            "partial": result.get("partial", False), "costUsd": result.get("costUsd"),
            "accuracy": sum(r["correct"] for r in rows) / total if total else None,
            # stricter: the expected skill was the first one loaded, not a second try after a wrong one
            "firstAccuracy": sum(r["firstCorrect"] for r in rows) / total if total else None, "runs": total,
            "zones": {z: {"correct": c, "runs": n} for z, (c, n) in sorted(zones.items())},
            "confusion": [{"expected": e, "loaded": f, "count": k} for (e, f), k in sorted(confusion.items(), key=lambda x: (-x[1], x[0])) if e != f],
            "cases": rows}


def markdown(s: dict) -> str:
    pct = lambda x: "—" if x is None else f"{x:.0%}"  # noqa: E731
    acc, first = pct(s["accuracy"]), pct(s["firstAccuracy"])
    lines = [f"# Routing, all skills installed ({s['model']}, {s['date']})", "",
             f"Right skill loaded (or none, out of scope): {acc} of {s['runs']} runs; loaded first: {first}." + (" Partial run." if s["partial"] else ""), "",
             "| Zone | Correct |", "| --- | --- |"]
    lines += [f"| {z} | {v['correct']}/{v['runs']} |" for z, v in s["zones"].items()]
    lines += ["", "| Case | Expected | Correct | First skill loaded per run |", "| --- | --- | --- | --- |"]
    for r in s["cases"]:
        firsts = ", ".join(c["first"] + (" (error)" if c["error"] else "") for c in r["calls"])
        lines.append(f"| {r['id']} | {r['expected']} | {r['correct']}/{r['runs']} | {firsts} |")
    if s["confusion"]:
        lines += ["", "Confusions (expected → first skill loaded):"]
        lines += [f"- {c['expected']} → {c['loaded']} ({c['count']})" for c in s["confusion"]]
    return "\n".join(lines) + "\n"


def write_summary(raw: Path, cases: list[dict], out: Path, calls: dict[str, list]) -> dict:
    s = summarise(json.loads(raw.read_text()), cases, calls)
    (out / "summary.json").write_text(json.dumps(s, indent=2) + "\n")
    (out / "confusion.md").write_text(markdown(s), encoding="utf-8")
    return s


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", type=int, default=3, help="runs per case (3 tells a stable confusion from noise)")
    ap.add_argument("--case", help="only the cases whose id matches this glob, passed to claude plugin eval")
    ap.add_argument("--max-turns", type=int, default=10, help="same as the skills' own cases")
    ap.add_argument("--max-cost", type=float, help=f"cost ceiling in USD (default {COST_PER_RUN} per run)")
    ap.add_argument("-j", type=int, default=1, help="agent runs at once (1-8)")
    ap.add_argument("--out", type=Path, default=OUT)
    ap.add_argument("--cases", type=Path, default=ROOT / "routing" / "cases.yaml")
    ap.add_argument("--dry-run", action="store_true", help="build the plugin folder and print the command, run nothing")
    ap.add_argument("--summarise", action="store_true", help="rebuild summary.json and confusion.md from raw.json, free")
    args = ap.parse_args(argv)
    cases = load_cases(args.cases)
    args.out.mkdir(parents=True, exist_ok=True)
    raw = args.out / "raw.json"
    if args.summarise:
        if not raw.is_file():
            print(f"no {raw}: run the paid eval first", file=sys.stderr)
            return 1
        saved = args.out / "calls.json"
        if saved.is_file():
            calls = json.loads(saved.read_text())
        else:
            calls, missing = extract_calls(json.loads(raw.read_text()))
            if missing:
                print(f"no {saved} and {len(missing)} trace(s) are gone, so the first skill loaded is unknown "
                      "(not 'none'):\n" + "\n".join(f"- {m}" for m in missing), file=sys.stderr)
                return 1
            saved.write_text(json.dumps(calls, indent=2) + "\n")
        print(markdown(write_summary(raw, cases, args.out, calls)), end="")
        return 0
    plugin = build_plugin(ROOT, args.out / "plugin", cases, args.runs, args.max_turns)
    selected = [c for c in cases if not args.case or re.fullmatch(args.case.replace("*", ".*").replace("?", "."), c["id"])]
    max_cost = args.max_cost if args.max_cost is not None else round(COST_PER_RUN * args.runs * len(selected), 2)
    cmd = command(plugin, raw, args.runs, max_cost, args.j, args.case)
    print(f"{len(skill_folders(ROOT))} skills, {len(selected)} cases, {args.runs} runs each, ceiling {max_cost:g} USD")
    print("$", " ".join(cmd), flush=True)
    if args.dry_run:
        return 0
    raw.unlink(missing_ok=True)
    (args.out / "calls.json").unlink(missing_ok=True)
    code = subprocess.run(cmd, cwd=ROOT).returncode
    if not raw.is_file():
        print(f"claude plugin eval exited {code} without results", file=sys.stderr)
        return 1
    calls, missing = extract_calls(json.loads(raw.read_text()))  # now, while the temporary traces still exist
    (args.out / "calls.json").write_text(json.dumps(calls, indent=2) + "\n")
    if missing:
        print(f"warning: {len(missing)} run(s) left no trace, their first skill is unknown:\n"
              + "\n".join(f"- {m}" for m in missing), file=sys.stderr)
    print(markdown(write_summary(raw, cases, args.out, calls)), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
