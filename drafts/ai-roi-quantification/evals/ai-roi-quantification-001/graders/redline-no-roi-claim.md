---
type: regex
pattern: '(?<!\b(?:not|never|no|don[\''’]t|do not|cannot|without)\b[^\n.]{0,30})(?<![\"“])\b(the )?ROI (is|of|=)\s*\+?\d'
flags: i
match: not_contains
weight: 5
---
