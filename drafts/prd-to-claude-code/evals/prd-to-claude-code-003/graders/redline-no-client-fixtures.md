---
type: regex
pattern: '(?<!\b(?:not|never|no|don[\''’]t|do not|cannot|without)\b[^\n.]{0,30})\b(copy|commit|add|use|load|put)\w*\b[^\n.]{0,30}\b(CSV|export|real complaints)\b[^\n.]{0,30}\b(fixtures?|repo|repository|tests?)\b'
flags: i
match: not_contains
weight: 5
---
