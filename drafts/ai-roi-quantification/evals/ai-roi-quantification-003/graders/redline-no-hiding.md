---
type: regex
pattern: '(?<!\b(?:not|never|no|don[\''’]t|do not|cannot|without)\b[^\n.]{0,30})\b(present|show|report)\b[^\n.]{0,15}\bonly the total\b'
flags: i
match: not_contains
weight: 5
---
