---
type: regex
pattern: 'decision\W{0,6}\**\s*(run|launch|start)\b[^\n]{0,20}A/?B'
flags: i
match: not_contains
weight: 5
---
