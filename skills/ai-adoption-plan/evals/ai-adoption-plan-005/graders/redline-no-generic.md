---
type: regex
pattern: '(?<!\b(?:not|never|no|don[\''’]t|do not|cannot|without)\b[^\n.]{0,30})\b(a |the |one )?generic e-?learning\b[^\n.]{0,30}\b(is enough|suffices|will do|for them)\b'
flags: i
match: not_contains
weight: 5
---
