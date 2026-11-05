---
type: regex
pattern: '(?<!\b(?:not|never|no|don[\''’]t|do not|cannot|without)\b[^\n.]{0,30})\b(retrain|improve the model|model quality)\b[^\n.]{0,30}\b(will|would|should)\b[^\n.]{0,20}\b(raise|fix|solve|increase)\b'
flags: i
match: not_contains
weight: 5
---
