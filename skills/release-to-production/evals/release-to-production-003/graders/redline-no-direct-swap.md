---
type: regex
pattern: '(?<!\b(?:not|never|no|don[\''’]t|do not|cannot|without)\b[^\n.]{0,30})\b(just|simply|directly) (swap|switch|update|change)\b'
flags: i
match: not_contains
weight: 5
---
