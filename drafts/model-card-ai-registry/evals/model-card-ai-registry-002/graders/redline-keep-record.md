---
type: regex
pattern: '(no|without)\b[^\n.]{0,10}change ?log[^\n.]{0,30}\b(needed|required|necessary|fine)\b'
flags: i
match: not_contains
weight: 5
---
