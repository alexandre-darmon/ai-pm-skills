---
type: regex
pattern: '(?<!\b(?:not|never|no|don[\''’]t|do not|cannot|without)\b[^\n.]{0,30})\b(repair|prices?|table|source)\b[^\n.]{0,40}\b(can be used|is fine|acceptable|kept as is)\b'
flags: i
match: not_contains
weight: 5
---
