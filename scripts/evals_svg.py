"""Write assets/evals.svg: per catalog skill, the regex score without the skill, with its template only, and with it.

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
    x0, x1 = MARGIN + LABEL, W - MARGIN - 70
    sx = lambda v: x0 + v * (x1 - x0)
    top = 150
    h = top + len(rows) * ROW + 110
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" role="img" '
           f'aria-label="Eval scores of the {len(rows)} catalog skills: without the skill, with its template only, and with it">',
           f"<title>Eval scores of the {len(rows)} catalog skills</title>", *background(h),
           mono("Evals · same cases, Sonnet 5.5, 3 runs per case", MARGIN, 56, 18, FAINT),
           medium("Without the skill, its template only, with the skill", MARGIN, 100, 30, INK)]
    for v in (0, 0.25, 0.5, 0.75, 1):
        x = sx(v)
        out.append(f'<path d="M{x:.1f} {top - 18}V{top + len(rows) * ROW - 10}" stroke="{BORDER}" stroke-width="1"/>')
        out.append(mono(f"{round(v * 100)}%", x - 14, top - 26, 12, FAINT))
    for i, (skill, wo, tm, w, n) in enumerate(rows):
        y = top + i * ROW + 8
        out.append(mono(skill, MARGIN, y + 5, 13.5, INK))
        out.append(f'<path d="M{sx(wo):.1f} {y}H{sx(w):.1f}" stroke="{VIOLET}" stroke-opacity="0.35" stroke-width="3"/>')
        out.append(f'<circle cx="{sx(wo):.1f}" cy="{y}" r="6" fill="#FFFFFF" stroke="{FAINT}" stroke-width="1.6"/>')
        if tm is not None:
            out.append(f'<rect x="{sx(tm) - 4:.1f}" y="{y - 4}" width="8" height="8" fill="{MUTED}" transform="rotate(45 {sx(tm):.1f} {y})"/>')
        out.append(f'<circle cx="{sx(w):.1f}" cy="{y}" r="7" fill="{VIOLET}"/>')
        out.append(mono(f"+{round(100 * (w - wo))}", sx(w) + 14, y + 5, 13, VIOLET))
    y = top + len(rows) * ROW + 30
    out += [f'<circle cx="{MARGIN + 6}" cy="{y}" r="6" fill="#FFFFFF" stroke="{FAINT}" stroke-width="1.6"/>',
            sans("model alone", MARGIN + 20, y + 5, 14, MUTED),
            f'<rect x="{MARGIN + 160}" y="{y - 4}" width="8" height="8" fill="{MUTED}" transform="rotate(45 {MARGIN + 164} {y})"/>',
            sans("skill's template only", MARGIN + 178, y + 5, 14, MUTED),
            f'<circle cx="{MARGIN + 360}" cy="{y}" r="7" fill="{VIOLET}"/>',
            sans("with the skill (gain in points)", MARGIN + 374, y + 5, 14, MUTED),
            sans("Regex graders written by the skills' author: they reward what the skill asks for. A blind judge sees a smaller gain.",
                 MARGIN, y + 40, 14, MUTED)]
    (ROOT / "assets/evals.svg").write_text("".join(out + ["</svg>\n"]))


if __name__ == "__main__":
    main(sys.argv[1])
