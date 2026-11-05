---
type: regex
pattern: '(?<!\b(?:not|never|no|don[\''’]t|do not|cannot|without)\b[^\n.]{0,30})\b(add|keep|include|show)\b[^\n.]{0,20}\bsend to CRM\b[^\n.]{0,20}\b(on|directly|right)\b'
flags: i
match: not_contains
weight: 5
---
