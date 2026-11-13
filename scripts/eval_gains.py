"""Write skill-eval-gains.md from baselines/ and refresh the README block.

Three arms on the same cases (the model alone, the model with the skill's output template only, the model with
the skill), scored two ways: regex graders (baselines/*.json, baselines/template-arm/) and the blind LLM judges
(baselines/judge/<judge model>/). Each gain comes with a 95% interval over cases (scripts/eval_stats.py).
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from eval_stats import bootstrap_ci, macro_mean  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DRAWS = 10_000


def pct(x):
    return "—" if x is None else f"{round(100 * x)}%"


def pts(x):
    return f"{round(100 * x):+d}" if round(100 * x) else "0"


def model_name(model):  # claude-haiku-5-5 -> Haiku 5.5
    parts = model.split("-")
    return f"{parts[1].capitalize()} {'.'.join(parts[2:])}" if parts[0] == "claude" and len(parts) > 2 else model


def groups(cases, a, b=None):
    """Per skill, the list of case values of arm a (or of a - b), skipping skills that lack an arm."""
    out = [[c[a] - c[b] if b else c[a] for c in cs.values() if a in c and (b is None or b in c)] for cs in cases.values()]
    return [g for g in out if g]


def arm_mean(cases, arm):
    g = groups(cases, arm)
    return macro_mean(g) if g else None


def gain(cases, a, b, draws):
    g = groups(cases, a, b)
    if not g:
        return "—"
    lo, hi = bootstrap_ci(g, draws=draws)
    return f"{pts(macro_mean(g))} [{pts(lo)}, {pts(hi)}]"


def point_gain(cases, a, b):
    g = groups(cases, a, b)
    return f"{pts(macro_mean(g))} pts" if g else "—"


def cost_cell(c, score_without, score_with):
    """API-equivalent cost of one answer divided by its regex score, without → with."""
    if not c or not score_without or not score_with:
        return "—"
    return f"${c[0] / score_without:.3f} → ${c[1] / score_with:.3f}"


def held(runs):  # [held, total]
    return runs[0] / runs[1] if runs[1] else None


# Reads under root: keep check_generated.INPUTS in step with any new folder read here.
def main(root=ROOT, draws=DRAWS):
    base = root / "baselines"
    regex, per_skill, models, costs = {}, [], set(), {}
    rl = {"without": [0, 0], "template": [0, 0], "with": [0, 0]}
    neg = [0, 0]
    for f in sorted(base.glob("*.json")):
        b = json.loads(f.read_text())
        skill = b["skill"]
        if not (root / "skills" / skill).is_dir():  # drafts keep their recorded runs but are not shown
            continue
        models.add(b.get("model", ""))
        t = base / "template-arm" / f.name
        tarm = json.loads(t.read_text()) if t.is_file() else {}
        # a template arm run on other cases than the frozen run is not comparable with it
        tcases = tarm["cases"] if tarm.get("casesHash") == b.get("casesHash") else {}
        pos = {cid: c for cid, c in b["cases"].items() if not c["negative"]}
        regex[skill] = {cid: {"with": c["score"], "without": c["scoreWithout"]} for cid, c in pos.items()}
        srl = {"without": [0, 0], "template": [0, 0], "with": [0, 0]}
        for cid, c in pos.items():
            if cid in tcases:
                regex[skill][cid]["template"] = tcases[cid]["score"]
            for g, (a, z) in c["graders"].items():
                if g.startswith("redline-"):
                    srl["with"][0] += a; srl["with"][1] += c["runs"]
                    srl["without"][0] += z; srl["without"][1] += c.get("runsWithout", c["runs"])
                    if cid in tcases:
                        srl["template"][0] += tcases[cid]["graders"][g][0]; srl["template"][1] += tcases[cid]["runs"]
        for arm in rl:
            rl[arm] = [x + y for x, y in zip(rl[arm], srl[arm])]
        for c in b["cases"].values():
            if c["negative"]:
                neg[0] += c["runs"] - c["fired"]; neg[1] += c["runs"]
        if all(c.get("costPerAnswer") and None not in c["costPerAnswer"] for c in pos.values()):
            cw = sum(c["costPerAnswer"][0] for c in pos.values()) / len(pos)
            cwo = sum(c["costPerAnswer"][1] for c in pos.values()) / len(pos)
            costs[skill] = (cwo, cw)
        one = {skill: regex[skill]}
        deltas = [c["with"] - c["without"] for c in regex[skill].values()]
        runs = sorted({c["runs"] for c in pos.values()})
        rlw = " / ".join(pct(held(srl[a])) for a in ("without", "template", "with")) if srl["with"][1] else "—"
        per_skill.append(
            f"| [`{skill}`](skills/{skill}/SKILL.md) | {pct(arm_mean(one, 'without'))} | {pct(arm_mean(one, 'template'))} "
            f"| **{pct(arm_mean(one, 'with'))}** | {pts(macro_mean([deltas]))} pts ({pts(min(deltas))} to {pts(max(deltas))}) "
            f"| {point_gain(one, 'with', 'template')} "
            f"| {rlw} | {cost_cell(costs.get(skill), arm_mean(one, 'without'), arm_mean(one, 'with'))} | {len(pos)} × {'/'.join(map(str, runs))} | {b['date']} |")

    judges, judge_rows = [], []
    for d in sorted(p for p in (base / "judge").glob("*") if p.is_dir()) if (base / "judge").is_dir() else []:
        cases, calibrated, meta = {}, True, {}
        for skill in regex:
            f = d / f"{skill}.json"
            if not f.is_file():
                continue
            j = json.loads(f.read_text())
            if j.get("limit"):  # a --limit trial, not a run: kept out of the tables
                continue
            calibrated &= bool(j.get("calibrated"))
            meta = {"model": j.get("judgeModel") or d.name, "kind": j.get("judgeKind") or "llm",
                    "recorded": meta.get("recorded", True) and j.get("answerSet") == "recorded"}
            sums = {}
            for a in j["answers"]:
                if a.get("judge") is not None:
                    sums.setdefault(a["case"], {}).setdefault(a["arm"], []).append(a["judge"])
            cases[skill] = {cid: {arm: sum(v) / len(v) for arm, v in arms.items()} for cid, arms in sums.items()}
            one = {skill: cases[skill]}
            words = " / ".join(f"{round(j['arms'][a]['words']):,}" if a in j["arms"] else "—" for a in ("without", "template", "with"))
            judge_rows.append(
                f"| `{skill}` | {model_name(j.get('judgeModel') or d.name)} | {pct(arm_mean(one, 'without'))} | {pct(arm_mean(one, 'template'))} "
                f"| {pct(arm_mean(one, 'with'))} | {point_gain(one, 'with', 'without')} "
                f"| {point_gain(one, 'with', 'template')} | {round(100 * j['noise'])} pts | {words} |")
        if cases:
            judges.append((model_name(meta["model"]), calibrated, cases, meta))

    ncases = sum(len(cs) for cs in regex.values())
    runs = sorted({c["runs"] for f in base.glob("*.json") if (root / "skills" / f.stem).is_dir()
                   for c in json.loads(f.read_text())["cases"].values()})
    model = model_name(models.pop()) if len(models) == 1 else "the same model"

    def row(label, cases, bold=False):
        w = pct(arm_mean(cases, "with"))
        return (f"| {label} | {pct(arm_mean(cases, 'without'))} | {pct(arm_mean(cases, 'template'))} | {f'**{w}**' if bold else w} "
                f"| {gain(cases, 'with', 'without', draws)} | {gain(cases, 'with', 'template', draws)} |")

    def readme_row(label, cases, bold=False):
        # the README shows the point gain only; skill-eval-gains.md keeps the intervals
        w = pct(arm_mean(cases, "with"))
        return (f"| {label} | {pct(arm_mean(cases, 'without'))} | {pct(arm_mean(cases, 'template'))} | {f'**{w}**' if bold else w} "
                f"| {point_gain(cases, 'with', 'without')} | {point_gain(cases, 'with', 'template')} |")

    def table(row):
        lines = [
            f"| Same cases, {model} answering | Model alone | Skill's template only | With the skill | Gain over the model alone | Gain over the template |",
            "| --- | --- | --- | --- | --- | --- |",
            row(f"Regex graders: {len(regex)} skill{'s' if len(regex) != 1 else ''}, {ncases} cases × {'/'.join(map(str, runs))} runs", regex, bold=True),
        ]
        for name, cal, cases, meta in judges:
            n = sum(len(cs) for cs in cases.values())
            # files written with --recorded grade the run in baselines/<skill>.json; older ones an earlier run
            kind = "Blind decision model" if meta["kind"] == "decision" else "Blind LLM judge"
            runs_label = "recorded runs" if meta["recorded"] else "earlier runs"
            lines.append(row(f"{kind}, {name}: {len(cases)} of these skills, {n} cases, {runs_label}", cases))
        return lines + tail

    tail = []
    tail.append(f"| Red lines held (the one thing the answer must never do) | {pct(held(rl['without']))} | {pct(held(rl['template']))} "
                 f"| **{pct(held(rl['with']))}** | | |")
    if costs:
        cwo = sum(c[0] / arm_mean({k: regex[k]}, "without") for k, c in costs.items()) / len(costs)
        cw = sum(c[1] / arm_mean({k: regex[k]}, "with") for k, c in costs.items()) / len(costs)
        tail.append(f"| Cost per correct answer, API equivalent ({len(costs)} skills) | ${cwo:.3f} | — | **${cw:.3f}** | {round(100 * (cw / cwo - 1)):+d}% | |")
    tail.append(f"| Stays silent on near-miss requests | — | — | **{pct(held(neg))}** | | |")
    headline = "\n".join(table(row))
    readme_table = "\n".join(table(readme_row))

    out = f"""# Skill eval gains

Same model, same cases, three arms: the model alone, the model given only the skill's output template, and the model with the skill. Generated from [`baselines/`](baselines/) by `python3 scripts/eval_gains.py`; do not edit by hand.

{headline}

Gains in points. Brackets: 95% interval over cases (see below).

## Per skill, regex graders

| Skill | Without | Template only | With | Gain over the model alone (lowest to highest case) | Gain over the template | Red lines held: without / template / with | Cost per correct answer: without → with | Cases × runs | Run date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(per_skill)}

## Per skill, blind LLM judges

| Skill | Judge | Without | Template only | With | Gain over the model alone | Gain over the template | Judge noise | Words: without / template / with |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(judge_rows)}

## How to read it

- **Regex graders**: share of graders passed on a case, averaged over runs, then over a skill's scored cases, then over skills. A grader checks one thing the answer must contain or must not contain. The skills' author wrote them, so they reward what the skill asks for.
- **Template only**: the model gets the skill's own output template without its method. The gain over the template is what the method adds beyond the format ([template-only control](docs/evaluation.md)).
- **Blind LLM judge**: a model grades each answer twice on a generic rubric (sound, actionable, honest about unknowns, risk-aware, specific) without knowing the arm. It tends to favour longer answers and never grades the legal skills. Judge noise is the mean gap between its two passes on the same answer.
- **Intervals**: resample the cases within each skill 10,000 times and keep the middle 95% of the gains, with a small-sample correction (Rao-Wu rescaling, [scripts/eval_stats.py](scripts/eval_stats.py)). They show how much the gain depends on which cases were written. They do not cover the choice of graders, the judge's biases, or another model. Per skill, 3 to 5 cases are too few for an interval: the table gives the lowest and highest case gain instead.
- **Cost per correct answer**: the API-equivalent cost of one answer (as `claude plugin eval` reports it) divided by its regex score, averaged over skills; shown only for skills whose frozen run recorded the cost of each arm. A skill makes answers longer, so each answer costs more; the question is whether a correct one costs less.
- **Red lines**: a red line fails the case on its own (e.g. a refund agent launched without human validation, a "compliant" verdict). Shown as the share of runs where it held.
- **Pass rule**: a skill enters the catalogue when its regex score reaches the threshold (0.80, 0.90 for govern and flagship skills), every red line holds in every run, and the gain over the model alone is at least 10 points. Details in [docs/evaluation.md](docs/evaluation.md).
- **Runs**: 3 per case and per arm, November 2026. Two red-line graders (`assistant-kpis-cost-per-outcome`, `conversation-analysis`) were corrected after that run because they rejected correct answers; the saved answers were then re-scored.
- **Without** scores are not zero: the base model often gets part of the job right. The gain is what the skill adds on top.
"""
    (root / "skill-eval-gains.md").write_text(out)
    readme = root / "README.md"
    if readme.is_file() and "<!-- gains:start -->" in readme.read_text():
        head, rest = readme.read_text().split("<!-- gains:start -->", 1)
        note = (f"<sub>{model} answers each case {'/'.join(map(str, runs))} times per arm. **Regex graders** check that the answer contains what the skill asks for; "
                "the skills' author wrote them, so they favour the skill. The **blind LLM judge** scores general quality without knowing the arm; "
                "it tends to favour longer answers and never grades the legal skills. "
                "Gains in points; 95% intervals are in the per-skill numbers. [How the skills are tested](docs/testing-approach.md) · [per-skill numbers](skill-eval-gains.md).</sub>")
        readme.write_text(f"{head}<!-- gains:start -->\n{readme_table}\n\n{note}\n<!-- gains:end -->{rest.split('<!-- gains:end -->', 1)[1]}")
    return out


if __name__ == "__main__":
    sys.stdout.write(main())
