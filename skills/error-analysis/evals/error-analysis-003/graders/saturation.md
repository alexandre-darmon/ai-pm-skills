---
type: regex  # read until no new mode appears
pattern: 'saturat\w*|no new (failure )?(modes?|categor\w*|kinds?|types?)|\b(until|stop (when|once|after))\b[^\n]{0,100}\b(nothing new|no new)\b|\bin a row\b[^\n]{0,40}\b(nothing new|no new)\b'
flags: i
---
