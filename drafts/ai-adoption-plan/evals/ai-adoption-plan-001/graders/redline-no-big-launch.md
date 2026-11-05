---
type: regex
pattern: '(?<!\b(?:not|never|no|don[\''’]t|do not|cannot|without)\b[^\n.]{0,30})\b(launch|send|roll\w* out)\b[^\n.]{0,20}\b(to )?(everyone|all 2[, ]?000)\b[^\n.]{0,20}\bday one\b'
flags: i
match: not_contains
weight: 5
---
