---
type: regex  # baseline per class with n of N or an interval, not a global rate or a bare confusion matrix
pattern: '(?:per|by|each)[- ](?:class|category)[^.\n]{0,80}\b(?:intervals?|n of N|\d+ of \d+|n\s?=)|\b(?:intervals?|n of N)\b[^.\n]{0,60}\b(?:per|by|each)[- ](?:class|category)'
flags: i
---
