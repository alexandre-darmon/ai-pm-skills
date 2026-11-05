---
type: regex
pattern: '(?<!\b(?:not|never|no|don[\''’]t|do not|cannot|without)\b[^\n.]{0,30})\b(this|it|the assistant) (is|has) (a |real |strong )?(moat|defensible)\b'
flags: i
match: not_contains
weight: 5
---
