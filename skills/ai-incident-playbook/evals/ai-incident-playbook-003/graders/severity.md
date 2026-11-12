---
type: regex  # low severity, as a SEV level or in words
pattern: 'severity\W{0,6}\**\s*(\w+\W{1,3}){0,3}SEV ?[34]|\b(log|logged|classif\w*|treat|rate|rated|grade|graded|call|mark|set)\b[^\n.]{0,20}\bSEV ?[34]\b|\b(is|it[''’]s)\s+(a\s+)?\**SEV ?[34]\b|(?<!\b(not|never|no)\b[^\n.]{0,20})\blow(est)?[- ]severity\b|\bseverity\W{0,6}\**\s*(low|minor)\b'
flags: i
---
