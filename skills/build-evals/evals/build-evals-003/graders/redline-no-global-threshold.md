---
type: regex  # red line: the single global threshold is not kept, even with a per-class breakdown added
pattern: '(keep|keeping|stay with|retain|stick with)[^\n]{0,40}(single|global|overall|one|85 ?%)[^\n]{0,30}threshold'
flags: i
match: not_contains
weight: 3
---
