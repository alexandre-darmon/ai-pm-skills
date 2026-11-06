---
type: regex
pattern: '(?<!\b(?:not|never|no|don[\''’]t|do not|cannot|without)\b[^\n.]{0,30})\b(no|not)\b[^\n.]{0,10}\b(notification|notify)\b[^\n.]{0,15}\b(needed|required)\b(?!\s+(if|when|unless|where)\b)|\bno need to notify\b(?!\s+(if|when|unless|where)\b)'
flags: i
match: not_contains
weight: 5
---
