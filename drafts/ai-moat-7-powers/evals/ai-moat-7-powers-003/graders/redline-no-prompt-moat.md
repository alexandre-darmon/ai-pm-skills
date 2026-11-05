---
type: regex
pattern: '(?<!\b(?:not|never|no|don[\''’]t|do not|cannot|without)\b[^\n.]{0,30})\b(prompts?|UI|interface)\b[^\n.]{0,20}\b(is|are) (a |your |the )?(moat|advantage)\b'
flags: i
match: not_contains
weight: 5
---
