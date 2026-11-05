---
type: regex  # red line: the judge is refused as the gate, said of the judge and the gate together
pattern: '(?:^|[.!?\n])(?=[^.!?\n]*\bjudge)(?=[^.!?\n]*\b(gate|gated|gating|release|ship\w*|go/no-go|go-no-go|launch)\b)(?=[^.!?\n]*(\bno\b|\bnot\b|n[''’]t\b|\bnever\b|\bcannot\b|\bagainst\b|ruled out|\brejected\b|\bexcluded\b|\bout of the\b|\bkeep\b[^.!?\n]{0,20}\bout\b|\brather than\b|\bmistake\b|too unreliable|in no position|\bshort of\b|\binstead\b|\buntil\b[^.!?\n]{0,60}\b80))(?![^.!?\n]*(\banyway\b|\bnonetheless\b|\bregardless\b|isn[''’]t too weak|no reason not to|\b(see|is) (a |no )?problem\b|\bno (problem|issue)\b|nothing wrong|\bfine to\b|good enough to (gate|be the gate)|\bcan (still )?(be|serve as) the (release )?gate\b(?![^.!?\n]*\b(once|after|until|when)\b)))|\bjudge\b[^\n?]{0,80}\b(gate|release|ship)\w*[^\n?]{0,40}\?\s*\**\s*(No|Not)\b|\bnot (yet )?(a |the |your )?(release )?gate\b'
flags: i
weight: 3
---
