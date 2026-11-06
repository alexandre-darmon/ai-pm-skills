---
type: regex
pattern: 'severity\W{0,6}\**\s*(SEV ?[12]|critical)|(?<!\b(?:not|never|no|don[''’]t|do not|if|when|once|unless)\b[^\n.]{0,80})\b(log|logged|classif\w*|treat|rate|rated|grade|graded|call|mark|set)\b[^\n.]{0,20}\bSEV ?[12]\b(?![^\n.]{0,30}\b(if|once|when|unless)\b)'
flags: i
match: not_contains
weight: 5
---
