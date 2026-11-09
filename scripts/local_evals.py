#!/usr/bin/env python3
"""Local evals on Ollama: one model answers, the GPU is freed, another model judges. No paid call.

Usage:
  python3 scripts/local_evals.py generate [--model M] [--think] [skill_dir ...]   # answers, with and without the skill
  python3 scripts/local_evals.py unload   [--model M]                             # free the GPU and memory
  python3 scripts/local_evals.py grade    [--judge M] [--passes N] [skill_dir ...] # repo graders + blind judge
  python3 scripts/local_evals.py report                                            # eval-out/local/report.md

With no skill_dir: every skill in skills/ and drafts/.

generate mimics `claude plugin eval` with a small agent loop: both arms get the same system prompt and
tools, a Skill tool and a Read tool on the loaded skill's folder (evals/ excluded: the fixtures hold
model answers). In the "with" arm the Skill tool lists the skill (name + description, as Claude Code
does); in the "without" arm it lists none, as Claude Code without the plugin.
The tool_used graders are scored from the recorded tool calls. Answers are saved in the layout of
run_evals.py (eval-out/local/answers/<skill>/<case>/<arm>-1.md + runs.json), so its regrade() scores
the regex graders and verdict() applies the repo's pass rules. Every step resumes where it stopped.

grade also runs judge_answers.py's blind rubric with the local judge, information only and never on
govern (legal) skills (AGENTS.md). Local results are not comparable with the Claude baselines: a
different, smaller model wrote them, outside Claude Code.
"""
import argparse
import http.client
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate_skills import read_frontmatter  # noqa: E402
from run_evals import (ROOT, case_graders, cases_hash, mean, regrade, skill_hash,  # noqa: E402
                       summarise, verdict, warnings)
from concurrent.futures import ThreadPoolExecutor  # noqa: E402
from judge_answers import CRITERIA, PROMPT, SYSTEM, call_judge, collect, overall, parse_scores  # noqa: E402

OLLAMA = "http://localhost:11434"
ANSWER_MODEL = "qwen3.8:27b-mlx"
JUDGE_MODEL = "gemma4:31b-mlx"
OUT = ROOT / "eval-out" / "local"
NUM_CTX = 16384  # the largest run (skill + every reference + answer) stays under 13k tokens
AGENT_SYSTEM = """You are an AI assistant working with a product manager in a regulated European company. Answer their request in full, in English, in Markdown.
When one of the skills listed in the Skill tool matches the request, invoke it with the Skill tool before answering, then follow its instructions; it may point you to files you can open with the Read tool. When no skill matches, answer directly."""


class OllamaDown(RuntimeError):
    """Ollama stayed unreachable: stop the whole step rather than record every remaining run as failed."""


def chat(model: str, messages: list[dict], tools: list | None = None, think: bool = False, fmt=None) -> dict:
    for attempt in range(20):  # Ollama restarting (e.g. after a settings change): wait up to 10 minutes
        try:
            return _chat(model, messages, tools, think, fmt)
        except urllib.error.HTTPError:
            raise
        except (urllib.error.URLError, ConnectionError, http.client.HTTPException) as e:
            print(f"  Ollama unreachable ({e}), retry in 30s", flush=True)
            time.sleep(30)
    raise OllamaDown("Ollama unreachable for 10 minutes")


def _chat(model: str, messages: list[dict], tools: list | None = None, think: bool = False, fmt=None) -> dict:
    body = {"model": model, "messages": messages, "stream": False, "think": think, "options": {"num_ctx": NUM_CTX}}
    if tools:
        body["tools"] = tools
    if fmt:
        body["format"] = fmt
    req = urllib.request.Request(f"{OLLAMA}/api/chat", data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=3600) as r:
        return json.load(r)


def skill_folders(args: list[Path]) -> list[Path]:
    if args:
        return [p.resolve() for p in args]
    return sorted(p for d in ("skills", "drafts") for p in (ROOT / d).glob("*") if (p / "SKILL.md").is_file())


def tools_for(folder: Path, arm: str) -> list[dict]:
    """Same tools in both arms, as in Claude Code with and without the plugin: only the skill list differs."""
    fm, _ = read_frontmatter(folder / "SKILL.md")
    listing = f"- {fm['name']}: {fm['description']}" if arm == "with" else "(none)"
    return [
        {"type": "function", "function": {
            "name": "Skill",
            "description": "Execute a skill within the main conversation. When the user asks you to perform a task, check whether one of "
                           f"the available skills below matches it; if so, invoke it before answering.\n\nAvailable skills:\n{listing}",
            "parameters": {"type": "object", "properties": {"skill": {"type": "string", "description": "The skill name"}}, "required": ["skill"]}}},
        {"type": "function", "function": {
            "name": "Read",
            "description": "Read a file of a loaded skill. file_path is relative to the skill's base directory (e.g. references/x.md) or absolute.",
            "parameters": {"type": "object", "properties": {"file_path": {"type": "string"}}, "required": ["file_path"]}}},
    ]


def run_tool(folder: Path, name: str, args: dict, loaded: set, arm: str) -> str:
    skill = folder.name
    if name == "Skill":
        asked = str(args.get("skill", "")).split(":")[-1].strip()
        if asked != skill or arm != "with":
            return f"Unknown skill: {asked}"
        loaded.add(skill)
        _, body = read_frontmatter(folder / "SKILL.md")
        return f"Base directory for this skill: {folder}\n\n{body.strip()}"
    if name == "Read":
        raw = str(args.get("file_path", ""))
        path = (Path(raw) if raw.startswith("/") else folder / raw).resolve()
        if not loaded or folder not in path.parents or "evals" in path.relative_to(folder).parts:
            return f"File not found: {raw}"
        return path.read_text(encoding="utf-8") if path.is_file() else f"File not found: {raw}"
    return f"Unknown tool: {name}"


def agent(folder: Path, request: str, arm: str, model: str, think: bool, max_turns: int) -> dict:
    messages = [{"role": "system", "content": AGENT_SYSTEM}, {"role": "user", "content": request}]
    tools = tools_for(folder, arm)
    calls, loaded, tokens, error = [], set(), 0, None
    answer = ""
    for _ in range(max_turns):
        for attempt in range(3):  # Ollama answers 500 when the model writes a malformed tool call: sample again
            try:
                reply = chat(model, messages, tools, think)
                break
            except urllib.error.HTTPError as e:
                if e.code != 500 or attempt == 2:
                    raise
        msg = reply["message"]
        tokens += reply.get("eval_count", 0)
        messages.append({k: msg[k] for k in ("role", "content", "tool_calls") if k in msg})
        if not msg.get("tool_calls"):
            answer = msg.get("content", "")
            break
        for tc in msg["tool_calls"]:
            fn = tc["function"]
            args = fn.get("arguments") or {}
            args = json.loads(args) if isinstance(args, str) else args
            calls.append({"tool": fn["name"], "input": args})
            messages.append({"role": "tool", "tool_name": fn["name"], "content": run_tool(folder, fn["name"], args, loaded, arm)})
    else:
        error = f"no final answer after {max_turns} turns"
    answer = re.sub(r"<think>.*?</think>", "", answer, flags=re.S).strip()
    return {"answer": answer, "calls": calls, "tokens": tokens, "error": error or (None if answer else "empty answer")}


def tool_graders(graders: list[dict], calls: list[dict], arm: str) -> dict:
    """tool_used graders, as the harness scores them: count matching calls, then check min and max."""
    out = {}
    for g in graders:
        if g["type"] != "tool_used":
            continue
        c = g["config"]
        hits = [x for x in calls if x["tool"] == c.get("tool") and
                (not c.get("input_match") or re.search(c["input_match"], json.dumps(x["input"])))]
        out[g["name"]] = int(c.get("min", 1)) <= len(hits) <= (int(c["max"]) if "max" in c else 10**9)
    return out


def generate(args) -> int:
    folders = skill_folders(args.skills)
    todo = [(f, case) for f in folders for case in sorted((f / "evals").glob("*/prompt.md"))]
    total, done_now, started = len(todo) * 2, 0, time.time()
    print(f"{len(folders)} skills, {len(todo)} cases, {total} runs with {args.model} (think={args.think})", flush=True)
    for n, (folder, prompt) in enumerate(todo):
        skill, case = folder.name, prompt.parent.name
        answers = OUT / "answers" / skill
        runs_file = answers / "runs.json"
        saved = json.loads(runs_file.read_text()) if runs_file.is_file() else {
            "model": args.model, "think": args.think, "startedAt": datetime.now(timezone.utc).isoformat(), "skillHash": skill_hash(folder), "cases": {}}
        fm, body = read_frontmatter(prompt)
        graders = case_graders(folder, case)
        for arm in ("with", "without"):
            file = f"{case}/{arm}-1.md"
            prev = saved["cases"].get(case, {}).get(arm)
            if (answers / file).is_file() and prev and not prev[0]["error"] and not args.force:
                continue  # a failed run is redone
            t = time.time()
            try:
                r = agent(folder, body.strip(), arm, args.model, args.think, int(fm.get("max_turns", 10)))
            except OllamaDown:
                print("Ollama is down: stopped. Rerun generate to resume.", flush=True)
                return 2
            except Exception as e:  # one failed call must not stop a night-long run; it is recorded as an error
                r = {"answer": "", "calls": [], "tokens": 0, "error": f"{type(e).__name__}: {e}"[:300]}
            (answers / case).mkdir(parents=True, exist_ok=True)
            (answers / file).write_text(r["answer"], encoding="utf-8")
            (answers / case / f"{arm}-1.trace.json").write_text(json.dumps({**r, "seconds": round(time.time() - t)}, indent=2), encoding="utf-8")
            saved["cases"].setdefault(case, {})[arm] = [{"file": file, "error": r["error"], "graders": tool_graders(graders, r["calls"], arm),
                                                         "skillCalls": sum(c["tool"] == "Skill" for c in r["calls"]),
                                                         "reads": [c["input"].get("file_path") for c in r["calls"] if c["tool"] == "Read"]}]
            runs_file.parent.mkdir(parents=True, exist_ok=True)
            runs_file.write_text(json.dumps(saved, indent=2) + "\n")
            done_now += 1
            left = total - (2 * n + (arm == "without") + 1)
            eta = (time.time() - started) / done_now * left / 60
            print(f"[{2 * n + (arm == 'without') + 1}/{total}] {skill}/{case}/{arm}: {round(time.time() - t)}s, {r['tokens']} tok, "
                  f"skill calls {sum(c['tool'] == 'Skill' for c in r['calls'])}, reads {sum(c['tool'] == 'Read' for c in r['calls'])}"
                  f"{', ERROR ' + r['error'] if r['error'] else ''} (about {eta:.0f} min left)", flush=True)
    failed = [f"{f.name}/{c}/{a}" for f in folders if (OUT / "answers" / f.name / "runs.json").is_file()
              for c, arms in json.loads((OUT / "answers" / f.name / "runs.json").read_text())["cases"].items()
              for a, rs in arms.items() if rs[0]["error"]]
    print(f"done; {len(failed)} runs failed" + (": " + ", ".join(failed) if failed else ""), flush=True)
    return 1 if failed else 0


def unload(args) -> int:
    for model in args.model:
        subprocess.run(["ollama", "stop", model], check=False)
    time.sleep(2)
    ps = subprocess.run(["ollama", "ps"], capture_output=True, text=True).stdout
    print(ps)
    return 1 if any(m in ps for m in args.model) else 0


def judge_one(model: str, prompt: str, schema: dict) -> dict:
    """One rubric reply: from Ollama, or from Claude on the subscription (judge_answers.call_judge) for a claude-* model."""
    if model.startswith("claude-"):
        res = call_judge(prompt, model)
        res.pop("costUsd", None)
        return res
    reply = chat(model, [{"role": "system", "content": SYSTEM}, {"role": "user", "content": prompt}], fmt=schema)
    return parse_scores(reply["message"]["content"])


def grade(args) -> int:
    out_dir = args.out
    (out_dir / "grades").mkdir(parents=True, exist_ok=True)
    (out_dir / "judge").mkdir(parents=True, exist_ok=True)
    cache_file = out_dir / "judge" / "cache.jsonl"
    cache = {}
    if cache_file.is_file():
        for line in cache_file.read_text().splitlines():
            row = json.loads(line)
            if row.get("model", JUDGE_MODEL) == args.judge and "error" not in row["result"]:
                cache[row["key"]] = row["result"]  # failed replies are asked again
    schema = {"type": "object", "properties": {**{c: {"type": "integer"} for c in [*CRITERIA, "meets_goal"]}, "weakest_point": {"type": "string"}},
              "required": [*CRITERIA, "meets_goal", "weakest_point"]}
    workers = args.j if args.judge.startswith("claude-") else 1  # one local model answers one request at a time
    for folder in skill_folders(args.skills):
        fm, _ = read_frontmatter(folder / "SKILL.md")
        skill, answers = fm["name"], out_dir / "answers" / folder.name
        if not (answers / "runs.json").is_file():
            print(f"{skill}: no answers, skipped", flush=True)
            continue
        # 1. The repo's graders and pass rules, no model call.
        result = regrade(folder, answers)
        summary = summarise(result, skill, cases_hash(folder))
        summary.update(model=json.loads((answers / "runs.json").read_text()).get("model") or args.answer_model,
                       judgeModel=None, local=True, stale=result["stale"])
        failures = verdict(summary, float(fm["eval_threshold"]), None)
        summary.update(threshold=float(fm["eval_threshold"]), stage=fm.get("stage"), status=fm.get("status"),
                       folder=str(folder.relative_to(ROOT)), failures=failures, warnings=warnings(summary))
        (out_dir / "grades" / f"{skill}.json").write_text(json.dumps(summary, indent=2) + "\n")
        print(f"{skill}: {'FAIL' if failures else 'pass'}, mean delta {summary['meanDelta'] if summary['meanDelta'] is None else round(summary['meanDelta'], 2)}", flush=True)
        if args.no_judge:
            continue
        if fm.get("stage") == "govern":  # AGENTS.md: no LLM judge on legal skills
            print(f"{skill}: govern skill, no judge", flush=True)
            continue
        # 2. The blind rubric of judge_answers.py, with the chosen judge.
        items = collect(folder, answers)
        todo = [(item, p) for item in items for p in range(args.passes) if f"{item['id']}/{p}" not in cache]

        def run(job):
            item, p = job
            t = time.time()
            try:
                res = judge_one(args.judge, PROMPT.format(goal=item["goal"], request=item["request"], answer=item["answer"]), schema)
            except OllamaDown:
                raise
            except Exception as e:  # one bad reply must not lose the batch; the count is reported
                res = {"error": str(e)[:200]}
            print(f"  judge {skill}/{item['case']}/{item['arm']} pass {p + 1}: {round(time.time() - t)}s "
                  f"{'ERROR ' + res['error'] if 'error' in res else round(overall(res), 2)}", flush=True)
            return f"{item['id']}/{p}", res

        with ThreadPoolExecutor(workers) as pool:
            for key, res in pool.map(run, todo):
                cache[key] = res
                with cache_file.open("a") as f:
                    f.write(json.dumps({"key": key, "model": args.judge, "result": res}) + "\n")
        for item in items:
            item["results"] = [cache[f"{item['id']}/{p}"] for p in range(args.passes)]
        errors = [r["error"] for i in items for r in i["results"] if "error" in r]
        for item in items:
            good = [r for r in item.pop("results") if "error" not in r]
            item["scores"] = [overall(r) for r in good]
            item["judge"] = mean(item["scores"])
            item["meetsGoal"] = mean([(r["meets_goal"] - 1) / 4 for r in good])
            item["criteria"] = {c: mean([r[c] for r in good]) for c in [*CRITERIA, "meets_goal"]}
            item["weakest"] = [r["weakest_point"] for r in good]
            del item["answer"], item["request"]
        arms = {}
        for arm in ("with", "without"):
            rows = [i for i in items if i["arm"] == arm and i["judge"] is not None]
            arms[arm] = {"answers": len(rows), "judge": mean([r["judge"] for r in rows]), "meetsGoal": mean([r["meetsGoal"] for r in rows]),
                         "regex": mean([r["regex"] for r in rows]), "words": mean([r["words"] for r in rows]),
                         "criteria": {c: mean([r["criteria"][c] for r in rows]) for c in [*CRITERIA, "meets_goal"]}}
        pairs = [abs(i["scores"][0] - i["scores"][1]) for i in items if len(i["scores"]) >= 2]
        out = {"skill": skill, "judgeModel": args.judge, "calibrated": False, "passes": args.passes, "errors": len(errors),
               "firstError": errors[0] if errors else None, "noise": mean(pairs), "arms": arms, "answers": items}
        (out_dir / "judge" / f"{skill}.json").write_text(json.dumps(out, indent=2) + "\n")
    return 0


def report(args) -> int:
    fmt = lambda x, d=2: "—" if x is None else f"{x:.{d}f}"  # noqa: E731
    sign = lambda x: "—" if x is None else f"{x:+.2f}"  # noqa: E731
    rows, lines, out_dir = [], [], args.out
    for g in sorted((out_dir / "grades").glob("*.json")):
        s = json.loads(g.read_text())
        j = out_dir / "judge" / g.name
        judge = json.loads(j.read_text()) if j.is_file() else None
        pos = [c for c in s["cases"].values() if not c.get("negative")]
        neg = [c for c in s["cases"].values() if c.get("negative")]
        base = ROOT / "baselines" / g.name
        claude = json.loads(base.read_text()) if base.is_file() else None
        cpos = [c for c in claude["cases"].values() if not c.get("negative")] if claude else []
        rows.append({
            "skill": s["skill"], "stage": s["stage"], "status": s["status"], "threshold": s["threshold"],
            "with": mean([c["score"] for c in pos if c["score"] is not None]),
            "without": mean([c["scoreWithout"] for c in pos if c["scoreWithout"] is not None]),
            "delta": s.get("meanDelta"),
            "fired": f"{sum(c['fired'] for c in pos)}/{sum(c['runs'] for c in pos)}",
            "silent": f"{sum(c['runs'] - c['fired'] for c in neg)}/{sum(c['runs'] for c in neg)}",
            "belowThreshold": sum(c["score"] is not None and c["score"] < s["threshold"] for c in pos),
            "redlines": sum(n.startswith("redline-") and w < c["runs"] for c in pos for n, (w, _) in c["graders"].items()),
            "pass": not s["failures"], "failures": s["failures"],
            "jWith": judge["arms"]["with"]["judge"] if judge else None, "jWithout": judge["arms"]["without"]["judge"] if judge else None,
            "gWith": judge["arms"]["with"]["meetsGoal"] if judge else None, "gWithout": judge["arms"]["without"]["meetsGoal"] if judge else None,
            "wWith": judge["arms"]["with"]["words"] if judge else None, "wWithout": judge["arms"]["without"]["words"] if judge else None,
            "noise": judge["noise"] if judge else None,
            "claudeWith": mean([c["score"] for c in cpos]) if claude else None, "claudeWithout": mean([c["scoreWithout"] for c in cpos]) if claude else None,
        })
    models = sorted({json.loads(g.read_text()).get("model") or "?" for g in (out_dir / "grades").glob("*.json")})
    judges = sorted({json.loads(j.read_text())["judgeModel"] for j in (out_dir / "judge").glob("*.json") if j.name != "cache.jsonl"})
    lines += [f"# Eval report: {', '.join(models)}", "", f"Answers: {', '.join(models)}, judge: {', '.join(judges) or 'none'} "
              "(blind rubric, uncalibrated, information only). Generated by `scripts/local_evals.py report`.", "",
              "## Repo graders and pass rules (regex, skill-fired, red lines)", "",
              "| Skill | Stage | Status | With | Without | Delta | Fired | Negative silent | Cases < threshold | Red lines missed | Verdict |",
              "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in rows:
        lines.append(f"| {r['skill']} | {r['stage']} | {r['status']} | {fmt(r['with'])} | {fmt(r['without'])} | {sign(r['delta'])} | {r['fired']} | {r['silent']} "
                     f"| {r['belowThreshold']} | {r['redlines']} | {'pass' if r['pass'] else 'FAIL'} |")
    allp = lambda k: mean([r[k] for r in rows if r[k] is not None])  # noqa: E731
    lines += ["", f"Mean over skills: with {fmt(allp('with'))}, without {fmt(allp('without'))}, delta {sign(allp('delta'))}; "
              f"{sum(r['pass'] for r in rows)}/{len(rows)} skills pass.", "",
              "## Blind judge (generic rubric, 0 to 1; govern skills excluded)", "",
              "| Skill | Judge with | Judge without | Judge delta | Meets goal with | Meets goal without | Words with | Words without | Noise |",
              "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in rows:
        if r["jWith"] is None:
            continue
        d = None if r["jWithout"] is None else r["jWith"] - r["jWithout"]
        lines.append(f"| {r['skill']} | {fmt(r['jWith'])} | {fmt(r['jWithout'])} | {sign(d)} | {fmt(r['gWith'])} | {fmt(r['gWithout'])} "
                     f"| {fmt(r['wWith'], 0)} | {fmt(r['wWithout'], 0)} | {fmt(r['noise'])} |")
    lines += ["", "## Same skills on Claude (frozen baselines, Sonnet 5.5 in Claude Code)", "",
              "| Skill | This run with | This run without | Baseline with | Baseline without |", "| --- | --- | --- | --- | --- |"]
    for r in rows:
        if r["claudeWith"] is not None:
            lines.append(f"| {r['skill']} | {fmt(r['with'])} | {fmt(r['without'])} | {fmt(r['claudeWith'])} | {fmt(r['claudeWithout'])} |")
    lines += ["", "## Failures per skill", ""]
    for r in rows:
        if r["failures"]:
            lines.append(f"**{r['skill']}**" + "".join(f"\n- {f}" for f in r["failures"]) + "\n")
    (out_dir / "report.md").write_text("\n".join(lines) + "\n")
    (out_dir / "report.json").write_text(json.dumps(rows, indent=2) + "\n")
    print("\n".join(lines))
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("generate")
    g.add_argument("skills", nargs="*", type=Path)
    g.add_argument("--model", default=ANSWER_MODEL)
    g.add_argument("--think", action="store_true", help="let the model reason first: about twice as slow")
    g.add_argument("--force", action="store_true", help="redo runs already saved")
    u = sub.add_parser("unload")
    u.add_argument("--model", nargs="+", default=[ANSWER_MODEL, JUDGE_MODEL])
    gr = sub.add_parser("grade")
    gr.add_argument("skills", nargs="*", type=Path)
    gr.add_argument("--judge", default=JUDGE_MODEL)
    gr.add_argument("--passes", type=int, default=2, help="judge each answer this many times, to measure its noise")
    gr.add_argument("--no-judge", action="store_true")
    gr.add_argument("--out", type=Path, default=OUT, help="folder holding answers/ (eval-out/claude for run_evals.py --out eval-out/claude)")
    gr.add_argument("--answer-model", default=None, help="label for answers whose runs.json does not name the model")
    gr.add_argument("-j", type=int, default=4, help="parallel judge calls, Claude judge only")
    rp = sub.add_parser("report")
    rp.add_argument("--out", type=Path, default=OUT)
    args = ap.parse_args()
    return {"generate": generate, "unload": unload, "grade": grade, "report": report}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
