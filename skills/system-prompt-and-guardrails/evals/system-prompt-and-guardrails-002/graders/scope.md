---
type: regex  # the scope is tested: out-of-scope requests go into the redteam set, not only into the prompt
pattern: '\b(?:red[- ]?team|test|eval)\w*\b[^.\n]{0,120}\b(?:out[- ]of[- ]scope|off[- ]topic)\b|\b(?:\d+|ten) (?:out[- ]of[- ]scope|off[- ]topic)\b'
flags: i
---
