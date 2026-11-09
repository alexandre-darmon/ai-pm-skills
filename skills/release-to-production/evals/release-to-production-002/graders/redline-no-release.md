---
type: regex
pattern: 'decision\W{0,6}\**\s*(release|ship|go)\b'
flags: i
match: not_contains
weight: 5
---
