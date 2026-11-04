---
type: regex  # the pre-2026 date: Annex III high-risk duties no longer apply from 2 August 2026
pattern: '(high[- ]risk|annex III)[^.;,\n]{0,60}\b(appl(y|ies)|from|as of|starting|start)\b[^.;,\n]{0,15}(?<!\bnot\s)\b2 August 2026\b(?![^.\n]{0,60}(December 2027|postpon|moved|delayed|no longer|amended|Omnibus|now (apply|applies|from|2 December)))'
flags: i
match: not_contains
---
