---
type: regex
pattern: '(?<!\b(?:not|never|no|don[\''’]t|do not|cannot|without)\b[^\n.]{0,30})\b(all|every|these|the \d+)\b[^\n.]{0,30}\b(certified|official)\b'
flags: i
match: not_contains
weight: 5
---
