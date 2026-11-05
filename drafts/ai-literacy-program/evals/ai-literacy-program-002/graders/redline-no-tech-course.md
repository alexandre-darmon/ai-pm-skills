---
type: regex
pattern: '(?<!\b(?:not|never|no|don[\''’]t|do not|cannot|without)\b[^\n.]{0,30})\b(keep|use|run|take)\b[^\n.]{0,20}\b(two-day|2-day|technical) course\b'
flags: i
match: not_contains
weight: 5
---
