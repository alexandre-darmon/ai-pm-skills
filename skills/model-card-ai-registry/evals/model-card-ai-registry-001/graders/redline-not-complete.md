---
type: regex
pattern: '(?<!\b(?:not|never|no|don[\''’]t|do not|cannot|without)\b[^\n.]{0,30})\b(card|entry)\b[^\n.]{0,30}\b(is|looks) (complete|ready)\b'
flags: i
match: not_contains
weight: 5
---
