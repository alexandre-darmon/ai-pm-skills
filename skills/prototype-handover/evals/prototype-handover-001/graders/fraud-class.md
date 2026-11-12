---
type: regex  # the fraud-signal class is singled out: few cases, wide interval, its own bar
pattern: 'fraud[- ]signals?\b[^.\n]{0,100}\b(?:interval|n\s?=|\d+ cases|few|small|wider|separately|own bar|recall|miss\w*|false negatives?)\b|\b(?:interval|recall|bar|miss\w*|false negatives?)\b[^.\n]{0,60}\bfraud[- ]signal'
flags: i
---
