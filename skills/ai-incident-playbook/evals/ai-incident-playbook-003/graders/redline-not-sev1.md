---
type: regex  # red line: a no-harm drift set at SEV1/SEV2 or critical; "SEV3, not SEV2", a template row and a conditional escalation are fine
pattern: 'severity\W{0,6}\**\s*(?:SEV ?[12]|critical)\b(?!\s*\**\s*\|)(?!\s*\**\s*/\s*\**\s*SEV ?[34])|(?<!\b(?:not|never|no|don[''’]t|do not|if|when|once|unless)\b[^\n.]{0,80})\b(?:log|logged|classif\w*|treat|rate|rated|grade|graded|call|mark|set|raise|declare\w*|escalate)\b(?:(?!\b(?:not|never|no|nothing|don[''’]t|do not|doesn[''’]t|does not|cannot|can[''’]t|won[''’]t|without|instead of|rather than|or|than|instead)\b|n[''’]t\b)[^\n.]){0,20}\b(?:as\s+|it\s+|this\s+|to\s+)(?:an?\s+)?\**(?:SEV ?[12]\b|P[01]\b|critical\b(?![- ]?(?:tickets?|categor\w*|class\w*|path|queues?|system)))(?![^\n.]{0,30}\b(?:if|once|when|unless|only)\b)|(?<!\b(?:not|never|no|don[''’]t|do not|if|when|once|unless)\b[^\n.]{0,80})\b(?:is|it[''’]s|this[''’]s|as|open|raise\w*|declare)\s+(?:an?\s+)?\**SEV ?[12]\b(?![^\n.]{0,30}\b(?:if|once|when|unless|only)\b)'
flags: i
match: not_contains
weight: 5
---
