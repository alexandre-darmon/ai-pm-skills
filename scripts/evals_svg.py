"""Write assets/evals.svg: per catalog skill, the regex score without the skill and with it, and next to it the gain an
blind judge (JUDGE) sees on the same recorded answers; only files that grade the current recorded run count.

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
# judges shown next to the regex gain, in this order: (folder under baselines/judge/, column title)
JUDGES = [("typesafe--jev-1.14", "Jev"), ("openai--gpt-6.1-sol", "GPT Sol"), ("claude-opus-5-5", "Opus")]
JUDGE = JUDGES[0][0]


def judge_gains(root=ROOT, judge=JUDGE):
    """{skill: gain in points}: per case, the judge's mean with the skill minus without, averaged over cases."""
    out = {}
    for f in sorted((root / "baselines" / "judge" / judge).glob("*.json")):
        j = json.loads(f.read_text())
        b = root / "baselines" / f.name
        current = b.is_file() and j.get("skillHash") and j.get("skillHash") == json.loads(b.read_text()).get("skillHash")
        if j.get("limit") or j.get("answerSet") != "recorded" or not current:
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
    rows = scores()
    gains = [(title, judge_gains(judge=d)) for d, title in JUDGES]
    step = 80  # one fixed column per gain: regex, then each judge
    x0, x1 = MARGIN + LABEL, W - MARGIN - 70 - step * (len(JUDGES) + 1)
    cols = [W - MARGIN - 70 - step * (len(JUDGES) - k) for k in range(len(JUDGES) + 1)]
    cr = cols[0]
    sx = lambda v: x0 + v * (x1 - x0)
    top = 150
    h = top + len(rows) * ROW + 230
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" role="img" '
           f'aria-label="Eval scores of the {len(rows)} catalog skills: without the skill and with it on regex graders, and the gains seen by three blind judges">',
           f"<title>Eval scores of the {len(rows)} catalog skills</title>", *background(h),
           mono("Evals · same cases, Sonnet 5.5, 3 runs per case", MARGIN, 56, 18, FAINT),
           medium("What the skill adds: required items, and overall quality", MARGIN, 100, 30, INK)]
    for v in (0, 0.25, 0.5, 0.75, 1):
        x = sx(v)
        out.append(f'<path d="M{x:.1f} {top - 18}V{top + len(rows) * ROW - 10}" stroke="{BORDER}" stroke-width="1"/>')
        out.append(mono(f"{round(v * 100)}%", x - 14, top - 26, 12, FAINT))
    out += [mono("regex", cr - 4, top - 26, 12, FAINT)] + [mono(t, x - 4, top - 26, 12, FAINT) for (t, _), x in zip(gains, cols[1:])]
    for i, (skill, wo, tm, w, n) in enumerate(rows):
        y = top + i * ROW + 8
        out.append(mono(skill, MARGIN, y + 5, 13.5, INK))
        out.append(f'<path d="M{sx(wo):.1f} {y}H{sx(w):.1f}" stroke="{VIOLET}" stroke-opacity="0.35" stroke-width="3"/>')
        out.append(f'<circle cx="{sx(wo):.1f}" cy="{y}" r="6" fill="#FFFFFF" stroke="{FAINT}" stroke-width="1.6"/>')
        out.append(f'<circle cx="{sx(w):.1f}" cy="{y}" r="7" fill="{VIOLET}"/>')
        out.append(mono(f"{round(100 * (w - wo)):+d}", cr, y + 5, 13, VIOLET))
        for (_, jg), x in zip(gains, cols[1:]):
            g = jg.get(skill)
            out.append(mono("—" if g is None else f"{g:+d}", x, y + 5, 13, INK if g is not None else FAINT))
    y = top + len(rows) * ROW + 30
    out += [f'<circle cx="{MARGIN + 6}" cy="{y}" r="6" fill="#FFFFFF" stroke="{FAINT}" stroke-width="1.6"/>',
            sans("model alone", MARGIN + 20, y + 5, 14, MUTED),
            f'<circle cx="{MARGIN + 160}" cy="{y}" r="7" fill="{VIOLET}"/>',
            sans("with the skill, regex graders", MARGIN + 174, y + 5, 14, MUTED),
            sans("Gains in points. regex: graders written by the skills' author, they check what the skill asks for.",
                 MARGIN, y + 40, 14, MUTED),
            sans("Jev: TypeSafe's Jev 1.14, a blind decision model from another vendor, one score per criterion, no reasons given.",
                 MARGIN, y + 64, 14, MUTED),
            sans("GPT Sol: OpenAI's GPT-6.1 Sol, a blind LLM judge from another vendor, overall quality on the same answers.",
                 MARGIN, y + 88, 14, MUTED),
            sans("Opus: Claude Opus 5.5, the same blind judge prompt; a Claude model like the one that answers.",
                 MARGIN, y + 112, 14, MUTED),
            sans("All grade the current recorded runs; none checks legal correctness. Each varies by a few points per skill; larger gaps are real disagreements.",
                 MARGIN, y + 136, 14, MUTED)]
    (ROOT / "assets/evals.svg").write_text("".join(out + ["</svg>\n"]))


if __name__ == "__main__":
    main(sys.argv[1])
