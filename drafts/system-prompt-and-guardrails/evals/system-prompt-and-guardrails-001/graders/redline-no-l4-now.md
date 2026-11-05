---
type: regex
pattern: '(?<!\b(?:no|not|never|block\w*|until|before)\b[^\n.]{0,30})\bL4\b[^\n.]{0,30}\b(approved|allowed|enabled|granted|ready)\b'
flags: i
match: not_contains
weight: 5
---
