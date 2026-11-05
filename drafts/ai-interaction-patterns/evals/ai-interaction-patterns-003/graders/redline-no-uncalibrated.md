---
type: regex
pattern: '(?<!\b(?:not|never|no|don[\''’]t|do not|cannot|without)\b[^\n.]{0,30})\b(show|display|keep)\b[^\n.]{0,20}\b(92\s?%|the score|confidence)\b(?![^\n.]{0,30}\b(once|after|until|only if)\b)'
flags: i
match: not_contains
weight: 5
---
