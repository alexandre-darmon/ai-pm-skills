"""Write skill-eval-gains.md from baselines/*.json: score without and with each skill, and the gain."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def pct(x):
    return f"{round(100 * x)}%"


def main(root=ROOT):
    rows, tot = [], {"w": [], "wo": [], "rl": [0, 0, 0, 0], "neg": [0, 0]}
    for f in sorted((root / "baselines").glob("*.json")):
        b = json.loads(f.read_text())
        pos = [c for c in b["cases"].values() if not c["negative"]]
        neg = [c for c in b["cases"].values() if c["negative"]]
        w = sum(c["score"] for c in pos) / len(pos)
        wo = sum(c["scoreWithout"] for c in pos) / len(pos)
        rl = [0, 0, 0, 0]  # red-line runs held with, without, total with, total without
        for c in pos:
            for g, (a, z) in c["graders"].items():
                if g.startswith("redline-"):
                    rl[0] += a; rl[1] += z; rl[2] += c["runs"]; rl[3] += c.get("runsWithout", c["runs"])
        tot["w"].append(w); tot["wo"].append(wo)
        tot["rl"] = [x + y for x, y in zip(tot["rl"], rl)]
        tot["neg"][0] += sum(c["runs"] - c["fired"] for c in neg); tot["neg"][1] += sum(c["runs"] for c in neg)
        rlw = f"{pct(rl[0] / rl[2])} vs {pct(rl[1] / rl[3])}" if rl[2] else "—"
        rows.append(f"| [`{b['skill']}`](skills/{b['skill']}/SKILL.md) | {pct(wo)} | **{pct(w)}** | +{round(100 * (w - wo))} pts | {rlw} | {len(pos)} × {pos[0]['runs']} | {b['date']} |")
    w, wo = sum(tot["w"]) / len(tot["w"]), sum(tot["wo"]) / len(tot["wo"])
    rl, neg = tot["rl"], tot["neg"]
    out = f"""# Skill eval gains

Same model, same cases, with and without the skill. Generated from [`baselines/`](baselines/) by `python3 scripts/eval_gains.py`; do not edit by hand.

| | Without skill | With skill |
| --- | --- | --- |
| Mean score on the scored cases | {pct(wo)} | **{pct(w)}** |
| Red lines held (the one thing the answer must never do) | {pct(rl[1] / rl[3])} | **{pct(rl[0] / rl[2])}** |
| Stays silent on near-miss requests | — | **{pct(neg[0] / neg[1])}** |

## Per skill

| Skill | Without | With | Gain | Red lines held (with vs without) | Cases × runs | Run date |
| --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(rows)}

## How to read it

- **Score**: share of graders passed on a case, averaged over runs and over the scored cases. A grader checks one thing the answer must contain or must not contain (regex, free and deterministic).
- **Without / With**: the same prompt run by the same model (Sonnet 5.5), once without the skill and once with it loaded.
- **Red lines**: a red line fails the case on its own (e.g. a refund agent launched without human validation, a "compliant" verdict). Shown as the share of runs where it held.
- **Pass rule**: a skill enters the catalogue when its score reaches the threshold (0.80, 0.90 for govern and flagship skills), every red line holds in every run, and the gain is positive. Details in [docs/evaluation.md](docs/evaluation.md).
- **Re-confirmation pending** (paid runs paused): the `build-evals` and `conversation-analysis` rows are 1-run baselines; on their last 3-run check each missed a red line once, and the graders were refitted since. `llm-feature-prd` changed after its run.
- **Without** scores are not zero: the base model often gets part of the job right. The gain is what the skill adds on top.
"""
    (root / "skill-eval-gains.md").write_text(out)
    readme = root / "README.md"
    if readme.is_file() and "<!-- gains:start -->" in readme.read_text():
        head, rest = readme.read_text().split("<!-- gains:start -->", 1)
        block = out.split("\n\n")[2]  # the summary table
        note = f"<sub>{len(rows)} skills, Sonnet 5.5, same cases with and without the skill. Per-skill numbers and method: [skill-eval-gains.md](skill-eval-gains.md).</sub>"
        readme.write_text(f"{head}<!-- gains:start -->\n{block}\n\n{note}\n<!-- gains:end -->{rest.split('<!-- gains:end -->', 1)[1]}")
    return out


if __name__ == "__main__":
    sys.stdout.write(main())
