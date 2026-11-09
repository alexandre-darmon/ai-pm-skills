---
type: regex
pattern: '(?<!\b(?:not|never|no|don[\''’]t|do not|cannot|without)\b[^\n.]{0,30})\b(is|are|be|fully|already) compliant\b'
flags: i
match: not_contains
weight: 5
---
