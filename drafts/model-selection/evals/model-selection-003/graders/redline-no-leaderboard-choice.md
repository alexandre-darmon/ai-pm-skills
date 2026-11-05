---
type: regex
pattern: '(?<!\b(?:not|never|no)\b[^\n.]{0,30})\b(based on|according to|per|from) (the )?(public )?(leaderboard|benchmarks?)\b'
flags: i
match: not_contains
weight: 5
---
