---
type: regex
pattern: '(?<!\b(?:if|whether|unless)\b[^\n.]{0,80})\bart(?:icle|\.)?\s*22\b[^\n.]{0,40}\b(?:applies|(?:does not|doesn[\''’]t|will not|won[\''’]t) apply)\b'
flags: i
match: not_contains
weight: 5
---
