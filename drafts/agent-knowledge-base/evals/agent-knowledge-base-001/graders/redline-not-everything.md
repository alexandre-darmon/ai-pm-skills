---
type: regex
pattern: '(?<!\b(?:not|never|no|don[\''’]t|do not)\b[^\n.]{0,30})\b(index|include|ingest|keep)\w*\b[^\n.]{0,20}\b(all|every|everything)\b[^\n.]{0,15}\b(40|sources|of them)?\b'
flags: i
match: not_contains
weight: 5
---
