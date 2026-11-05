---
type: regex
pattern: '(?<!\b(?:not|never|no|don[\''’]t|do not|cannot|without)\b[^\n.]{0,30})\b(the|our) (model|LLM|prompts?) (is|are) (the|our) (moat|advantage)\b'
flags: i
match: not_contains
weight: 5
---
