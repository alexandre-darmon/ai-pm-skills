---
type: regex
pattern: 'active customer[^\n]{0,60}\bcertified\b(?![^\n]{0,30}(until|once|after))'
flags: i
match: not_contains
weight: 5
---
