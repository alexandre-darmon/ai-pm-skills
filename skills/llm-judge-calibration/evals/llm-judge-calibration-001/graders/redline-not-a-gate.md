---
type: regex  # red line: the judge is refused as the gate, said of the judge and the gate together
pattern: '(?:^|[.!?\n])(?=[^.!?\n]*\bjudge)(?=[^.!?\n]*\b(gate|gated|gating|good enough|ready|drop\w*|replace\w*|stop\w*|L3)\b)(?=[^.!?\n]*(\bno\b|\bnot\b|n[’'']t\b|\bnever\b|\bcannot\b|\brefus\w*|\bwithhold|too (weak|unreliable|lenient)|\bfalls? short\b))(?![^.!?\n]*(\banyway\b|\bnonetheless\b|\bregardless\b|no reason not to|\bno (problem|issue)\b|nothing wrong))|\bnot (yet )?(a |the |your |our )?(release |level |L3 )?gate\b|^\W*no\b'
flags: i
weight: 2
---
