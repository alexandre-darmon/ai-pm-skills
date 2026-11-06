#!/usr/bin/env python3
"""Template-only control: does a skill beat its own output template? (docs/evaluation.md)

Usage: python3 scripts/template_arm.py [--runs N] [--regrade] <skill> [<skill> ...]

Builds a copy of skills/<skill> whose body is only its templates/ files: same name,
description and cases, no method, no rules, no references. Runs it with the repo's
graders, reuses the "with" and "without" scores frozen in baselines/<skill>.json, and
writes baselines/template-arm/<skill>.json. --regrade re-scores saved answers for free.
"""
import argparse
import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from run_evals import evaluate, load_baseline, cases_hash, mean, ROOT  # noqa: E402

OUT = ROOT / "eval-out" / "template-arm"
MIN_METHOD_GAIN = 0.10


def build_variant(skill: str) -> Path:
    src, dst = ROOT / "skills" / skill, OUT / "variants" / skill
    shutil.rmtree(dst, ignore_errors=True)
    dst.mkdir(parents=True)
    shutil.copytree(src / "evals", dst / "evals", ignore=shutil.ignore_patterns("results"))
    frontmatter = (src / "SKILL.md").read_text(encoding="utf-8").split("---", 2)[1]
    templates = "\n\n".join(f.read_text(encoding="utf-8") for f in sorted((src / "templates").glob("*.md")))
    (dst / "SKILL.md").write_text(f"---{frontmatter}---\n\n# {skill}\n\nProduce the answer in this format, all headings present.\n\n{templates}", encoding="utf-8")
    return dst


def mean_score(summary: dict, key: str = "score") -> float:
    return mean([c[key] for c in summary["cases"].values() if not c.get("negative")])


def compare(baseline: dict, arm: dict) -> dict:
    """Scores in one row. The method gain is what the skill adds over its own template."""
    with_skill, template = mean_score(baseline), mean_score(arm)
    return {"without": mean_score(baseline, "scoreWithout"), "template": template, "with": with_skill,
            "methodGain": with_skill - template, "methodBeatsFormat": round(with_skill - template, 4) >= MIN_METHOD_GAIN}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("skills", nargs="+")
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--regrade", action="store_true")
    args = ap.parse_args()
    dest = ROOT / "baselines" / "template-arm"
    dest.mkdir(exist_ok=True)
    print("| Skill | Without | Template | With | Method gain |\n| --- | --- | --- | --- | --- |")
    for skill in args.skills:
        variant = build_variant(skill)
        baseline = load_baseline(skill, cases_hash(ROOT / "skills" / skill))
        if not baseline:
            print(f"{skill}: baselines/{skill}.json does not match the current cases", file=sys.stderr)
            return 1
        summary, _, _ = evaluate(variant, False, OUT, args.runs, args.regrade)
        row = compare(baseline, summary)
        (dest / f"{skill}.json").write_text(json.dumps({**summary, "comparison": row}, indent=2) + "\n")
        print(f"| {skill} | {row['without']:.0%} | {row['template']:.0%} | {row['with']:.0%} | {row['methodGain'] * 100:+.0f} pts |", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
