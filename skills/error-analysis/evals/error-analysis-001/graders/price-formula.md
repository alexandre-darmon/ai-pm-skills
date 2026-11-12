---
type: regex  # each mode priced as volume x share x cost per occurrence
pattern: '(frequency|count|occurrences|share|prevalence|rate|volume|9[ ,.]?000)[^\n]{0,80}(×|\bx\b|\*|times|multiplied by)[^\n]{0,80}(cost|EUR|€|share|rate|%)'
flags: i
---
