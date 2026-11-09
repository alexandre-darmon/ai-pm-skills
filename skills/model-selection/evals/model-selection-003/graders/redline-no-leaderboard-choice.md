---
type: regex
pattern: "(?<!\\b(?:not|never|no|cannot|can['’]?t|don['’]?t|won['’]?t|shouldn['’]?t)\\b[^\\n.]{0,30})\\b(based on|according to|per|from) (the )?(public )?(leaderboard|benchmarks?)\\b"
flags: i
match: not_contains
weight: 5
---
