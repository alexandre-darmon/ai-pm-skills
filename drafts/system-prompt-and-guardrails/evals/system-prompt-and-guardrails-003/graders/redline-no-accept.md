---
type: regex
pattern: '(?<!\b(?:not|never|no|don[\''’]t|do not|cannot)\b[^\n.]{0,30})\b(accept|ship|go live|launch|approve)\w*\b[^\n.]{0,30}\b(with it|as is|at 30\s?%|the current)\b'
flags: i
match: not_contains
weight: 5
---
