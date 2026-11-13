"""Write assets/evals.svg: per catalog skill, the regex score without the skill and with it, and next to it the gain an
outside blind judge (JUDGE, a general LLM from another vendor) sees on the same recorded answers.

Same style and outlined text as the banner (see lifecycle_svg.py). Needs fonttools and the Geist TTFs:
    python3 scripts/evals_svg.py <fonts_dir>
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lifecycle_svg import BORDER, FAINT, INK, MUTED, VIOLET, W, Text, background  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
MARGIN, LABEL, ROW = 56, 330, 34
JUDGE, JUDGE_NAME = "openai--gpt-6.1-sol", "GPT-6.1 Sol"


def judge_gains(root=ROOT, judge=JUDGE):
    """{skill: gain in points}: per case, the judge's mean with the skill minus without, averaged over cases."""
    out = {}
    for f in sorted((root / "baselines" / "judge" / judge).glob("*.json")):
        j = json.loads(f.read_text())
        if j.get("limit") or j.get("answerSet") != "recorded":
            continue
        cases = {}
        for a in j["answers"]:
            if a.get("judge") is not None:
                cases.setdefault(a["case"], {}).setdefault(a["arm"], []).append(a["judge"])
        g = [sum(c["with"]) / len(c["with"]) - sum(c["without"]) / len(c["without"]) for c in cases.values() if "with" in c and "without" in c]
        if g:
            out[f.stem] = round(100 * sum(g) / len(g))
    return out


def scores(root=ROOT):
    rows = []
    for f in sorted((root / "baselines").glob("*.json")):
        b = json.loads(f.read_text())
        if not (root / "skills" / b["skill"]).is_dir():
            continue
        pos = [(cid, c) for cid, c in b["cases"].items() if not c["negative"]]
        t = root / "baselines" / "template-arm" / f.name
        tarm = json.loads(t.read_text()) if t.is_file() else {}
        tc = tarm["cases"] if tarm.get("casesHash") == b.get("casesHash") else {}
        tmpl = [tc[cid]["score"] for cid, _ in pos if cid in tc]
        rows.append((b["skill"], sum(c["scoreWithout"] for _, c in pos) / len(pos),
                     sum(tmpl) / len(tmpl) if len(tmpl) == len(pos) else None,
                     sum(c["score"] for _, c in pos) / len(pos), len(pos)))
    return sorted(rows, key=lambda r: r[3] - r[1], reverse=True)


def main(fonts):
    fonts = Path(fonts)
    sans, medium, mono = (Text(fonts / f"{n}.ttf") for n in ("Geist-Regular", "Geist-Medium", "GeistMono-Regular"))
    rows, jg = scores(), judge_gains()
    x0, x1 = MARGIN + LABEL, W - MARGIN - 230
    cr, cj = W - MARGIN - 150, W - MARGIN - 70  # fixed columns: regex gain, judge gain
    sx = lambda v: x0 + v * (x1 - x0)
    top = 150
    h = top + len(rows) * ROW + 134
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" role="img" '
           f'aria-label="Eval scores of the {len(rows)} catalog skills: without the skill and with it on regex graders, and the gain seen by an outside judge">',
           f"<title>Eval scores of the {len(rows)} catalog skills</title>", *background(h),
           mono("Evals · same cases, Sonnet 5.5, 3 runs per case", MARGIN, 56, 18, FAINT),
           medium("What the skill adds: required items, and overall quality", MARGIN, 100, 30, INK)]
    for v in (0, 0.25, 0.5, 0.75, 1):
        x = sx(v)
        out.append(f'<path d="M{x:.1f} {top - 18}V{top + len(rows) * ROW - 10}" stroke="{BORDER}" stroke-width="1"/>')
        out.append(mono(f"{round(v * 100)}%", x - 14, top - 26, 12, FAINT))
    out += [mono("regex", cr - 4, top - 26, 12, FAINT), mono("judge", cj - 4, top - 26, 12, FAINT)]
    for i, (skill, wo, tm, w, n) in enumerate(rows):
        y = top + i * ROW + 8
        out.append(mono(skill, MARGIN, y + 5, 13.5, INK))
        out.append(f'<path d="M{sx(wo):.1f} {y}H{sx(w):.1f}" stroke="{VIOLET}" stroke-opacity="0.35" stroke-width="3"/>')
        out.append(f'<circle cx="{sx(wo):.1f}" cy="{y}" r="6" fill="#FFFFFF" stroke="{FAINT}" stroke-width="1.6"/>')
        out.append(f'<circle cx="{sx(w):.1f}" cy="{y}" r="7" fill="{VIOLET}"/>')
        out.append(mono(f"{round(100 * (w - wo)):+d}", cr, y + 5, 13, VIOLET))
        g = jg.get(skill)
        out.append(mono("—" if g is None else f"{g:+d}", cj, y + 5, 13, INK if g is not None else FAINT))
    y = top + len(rows) * ROW + 30
    out += [f'<circle cx="{MARGIN + 6}" cy="{y}" r="6" fill="#FFFFFF" stroke="{FAINT}" stroke-width="1.6"/>',
            sans("model alone", MARGIN + 20, y + 5, 14, MUTED),
            f'<circle cx="{MARGIN + 160}" cy="{y}" r="7" fill="{VIOLET}"/>',
            sans("with the skill, regex graders", MARGIN + 174, y + 5, 14, MUTED),
            sans("Gains in points. regex: graders written by the skills' author, they check what the skill asks for.",
                 MARGIN, y + 40, 14, MUTED),
            sans(f"judge: {JUDGE_NAME} (OpenAI), blind to the arm, overall quality of the same answers; it does not check legal correctness. "
                 "—: no saved answers without the skill to compare.",
                 MARGIN, y + 64, 14, MUTED)]
    (ROOT / "assets/evals.svg").write_text("".join(out + ["</svg>\n"]))


if __name__ == "__main__":
    main(sys.argv[1])
