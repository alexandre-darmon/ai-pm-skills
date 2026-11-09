---
type: regex
pattern: '(expir|refresh)\w*[^\n.]{0,40}\b(regularly|periodically|as needed|when relevant|from time to time)\b'
flags: i
match: not_contains
weight: 5
---
