---
type: regex
pattern: 'severity\W{0,6}\**\s*(\w+\W{1,3})?SEV ?[34]|\b(log|logged|classif\w*|treat|rate|rated|grade|graded|call|mark|set)\b[^\n.]{0,20}\bSEV ?[34]\b|\b(is|it[''’]s)\s+(a\s+)?\**SEV ?[34]\b'
flags: i
---
