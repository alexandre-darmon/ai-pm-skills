---
type: regex
pattern: '(fresh|refresh)\w*[^\n.]{0,30}\b(regular|regularly|periodic\w*|as needed)\b'
flags: i
match: not_contains
weight: 5
---
