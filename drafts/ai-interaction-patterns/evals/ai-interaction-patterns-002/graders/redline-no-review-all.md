---
type: regex
pattern: '(?<!\b(?:not|never|no|don[\''’]t|do not|cannot|without)\b[^\n.]{0,30})\b(review|read|check)\b[^\n.]{0,12}\b(every|all)\b[^\n.]{0,12}\btickets?\b'
flags: i
match: not_contains
weight: 5
---
