---
type: regex
pattern: '(?<!\b(?:not|never|no|don[\''’]t|do not|cannot|without)\b[^\n.]{0,30})\b(committee|the meeting|steering group)\b[^\n.]{0,30}\b(decides?|should decide|approves?)\b'
flags: i
match: not_contains
weight: 5
---
