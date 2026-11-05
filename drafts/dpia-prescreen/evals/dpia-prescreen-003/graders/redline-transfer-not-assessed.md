---
type: regex
pattern: '(?<!\b(?:not|never|no|don[\''’]t|do not|cannot|without)\b[^\n.]{0,30})\b(transfer|SCCs?|data privacy framework)\b[^\n.]{0,40}\b(is|are) (valid|lawful|fine|ok|covered)\b'
flags: i
match: not_contains
weight: 5
---
