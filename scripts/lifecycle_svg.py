"""Write assets/lifecycle.svg and assets/banner.svg in one style. A skill is tested if its folder is in skills/, else draft.

Text is outlined so it renders the same on GitHub with no web font. Needs fonttools and the Geist TTFs
(Geist-Regular, Geist-Medium, GeistMono-Regular, from the npm package geist):
    python3 scripts/lifecycle_svg.py <fonts_dir>
"""
import re
import sys
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
INK, MUTED, FAINT, BORDER, VIOLET = "#0A0A0A", "#5F5F66", "#6B6B70", "#E3E1E8", "#8C52EE"
STAGES = [
    ("Specify", "What correct means", ["ai-opportunity-assessment", "llm-feature-prd", "process-ai-redesign", "ai-data-requirements",
                                       "agent-design-and-tooling", "system-prompt-and-guardrails", "ai-interaction-patterns"]),
    ("Evaluate", "Offline and online", ["error-analysis", "build-evals", "llm-judge-calibration", "synthetic-eval-data", "agent-evals",
                                        "retrieval-evaluation", "model-selection", "ai-vendor-evaluation", "release-to-production",
                                        "production-evals-monitoring", "conversation-analysis"]),
    ("Prove", "To sponsor and regulator", ["assistant-kpis-cost-per-outcome", "ai-roi-quantification", "ai-act-classification",
                                           "model-card-ai-registry", "ai-incident-playbook", "ai-adoption-plan"]),
]
TAGLINE = "Evals as evidence for AI product managers in regulated companies."
W, MARGIN, GAP = 1280, 56, 24
COL = (W - 2 * MARGIN - 2 * GAP) / 3


class Text:
    def __init__(self, path):
        self.font = TTFont(path)
        self.glyphs, self.cmap = self.font.getGlyphSet(), self.font.getBestCmap()
        self.upem = self.font["head"].unitsPerEm

    def __call__(self, s, x, y, size, fill):
        scale, pen = size / self.upem, SVGPathPen(self.glyphs, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
        for ch in s:
            glyph = self.glyphs[self.cmap[ord(ch)]]
            glyph.draw(TransformPen(pen, (scale, 0, 0, -scale, x, y)))
            x += glyph.width * scale
        return f'<path d="{pen.getCommands()}" fill="{fill}"/>'


def marker(x, y, tested):
    if tested:
        return f'<rect x="{x}" y="{y - 10}" width="8" height="10" fill="{VIOLET}"/>'
    return f'<rect x="{x + 0.5}" y="{y - 9.5}" width="7" height="9" fill="none" stroke="{FAINT}"/>'


def background(h):
    return [f'<rect x="0.5" y="0.5" width="{W - 1}" height="{h - 1}" rx="16" fill="#F4F2F5" stroke="#E6E3EA"/>',
            f'<defs><radialGradient id="glow" gradientUnits="userSpaceOnUse" cx="{W + 40}" cy="-60" r="760"><stop offset="0" stop-color="#E0DFF0"/><stop offset="0.55" stop-color="#E9E7F2" stop-opacity="0.6"/><stop offset="1" stop-color="#F4F2F5" stop-opacity="0"/></radialGradient><clipPath id="r"><rect width="{W}" height="{h}" rx="16"/></clipPath></defs>',
            f'<rect width="{W}" height="{h}" fill="url(#glow)" clip-path="url(#r)"/>']


def banner(sans, medium, mono, logo):
    h, strip = 344, " · ".join(stage for stage, _, _ in STAGES)
    logo = re.sub(r'transform="[^"]*"', 'transform="translate(72 106) scale(1.375)"', logo)
    label = f"AI PM Skills: {strip}"
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" role="img" aria-label="{label}"><title>{label}</title>',
           *background(h),
           mono("Claude Code plugin · open source", 72, 82, 22, FAINT), logo,
           medium("AI PM Skills", 188, 173.5, 62, INK),
           sans(TAGLINE, 72, 256, 33.5, MUTED),
           mono(strip, 72, 319.5, 20, FAINT)]
    (ROOT / "assets/banner.svg").write_text("".join(out + ["</svg>\n"]))


def main(fonts):
    fonts = Path(fonts)
    sans, medium, mono = (Text(fonts / f"{n}.ttf") for n in ("Geist-Regular", "Geist-Medium", "GeistMono-Regular"))
    logo = re.search(r"<g transform.*?</g>", (ROOT / "assets/banner.svg").read_text(), re.S).group(0)
    logo = re.sub(r'transform="[^"]*"', f'transform="translate({MARGIN} 72) scale(0.75)"', logo)
    known = {s for _, _, skills in STAGES for s in skills}
    found = {p.name for d in ("skills", "drafts") for p in (ROOT / d).glob("*") if p.is_dir()}
    if known != found:
        sys.exit(f"STAGES and the skill folders differ: {sorted(known ^ found)}")
    tested = {p.name for p in (ROOT / "skills").glob("*") if p.is_dir()}
    banner(sans, medium, mono, re.search(r"<g transform.*?</g>", (ROOT / "assets/banner.svg").read_text(), re.S).group(0))

    y0 = 156
    H = y0 + 124 + max(len(sk) for _, _, sk in STAGES) * 26 + 40
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="AI PM Skills: three blocks and their {len(known)} skills">',
        f"<title>AI PM Skills: three blocks and their {len(known)} skills</title>",
        *background(H),
        mono(f"Evals as evidence · 3 blocks · {len(known)} skills", MARGIN, 56, 18, FAINT),
        logo,
        medium("AI PM Skills", MARGIN + 66, 106, 40, INK),
    ]
    for i, (stage, title, skills) in enumerate(STAGES):
        x = MARGIN + i * (COL + GAP)
        out += [mono(f"{i + 1:02d}", x, y0 + 16, 15, VIOLET), mono(stage, x + 28, y0 + 16, 15, FAINT)]
        out.append(f'<rect x="{x + 0.5}" y="{y0 + 30.5}" width="{COL - 1}" height="63" rx="14" fill="#FFFFFF" stroke="{BORDER}"/>')
        out.append(medium(title, x + 18, y0 + 69, 22, INK))
        if i < len(STAGES) - 1:
            ax, ay = x + COL + 5, y0 + 62
            out.append(f'<path d="M{ax} {ay}h{GAP - 10}m-5 -4l5 4l-5 4" fill="none" stroke="{FAINT}" stroke-width="1.4"/>')
        for j, skill in enumerate(skills):
            y = y0 + 124 + j * 26
            out += [marker(x + 1, y, skill in tested), mono(skill, x + 18, y, 13.5, INK if skill in tested else FAINT)]
    x, y = MARGIN + 2 * (COL + GAP), y0 + 124 + (len(STAGES[2][2]) + 1) * 26
    out += [marker(x + 1, y, True), mono("tested", x + 18, y, 13.5, INK)]
    out += [marker(x + 1, y + 26, False), mono("draft, not in the catalog yet", x + 18, y + 26, 13.5, FAINT)]
    out += [sans("Run with", x, y + 74, 15, MUTED), mono("/ai-pm-skills:<skill>", x, y + 98, 13.5, INK)]
    (ROOT / "assets/lifecycle.svg").write_text("".join(out + ["</svg>\n"]))


if __name__ == "__main__":
    main(sys.argv[1])
