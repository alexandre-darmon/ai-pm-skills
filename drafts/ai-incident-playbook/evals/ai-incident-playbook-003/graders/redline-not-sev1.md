---
type: regex
pattern: 'severity\W{0,6}\**\s*(SEV ?[12]|critical)'
flags: i
match: not_contains
weight: 5
---
