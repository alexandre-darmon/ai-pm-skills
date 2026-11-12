---
type: regex  # the personal production credentials are revoked or rotated
pattern: '\b(?:revok\w*|rotat\w*|withdraw\w*|disabl\w*|remov\w*)\b[^.\n]{0,60}\b(?:credentials?|access|login|account)\b|\b(?:credentials?|login|account|access)\b[^.\n]{0,60}\b(?:revok\w*|rotat\w*|withdraw\w*|disabl\w*)'
flags: i
---
