---
type: regex  # the fraud-signal class is rare: few cases, so a wide interval and its own bar
pattern: 'fraud[- ]signals?\b[^.\n]{0,120}\b(?:intervals?|wide|wider|few cases|small|rare|n\s?=|\d+ of \d+)\b|\b(?:intervals?|wide|wider|rare|small)\b[^.\n]{0,60}\bfraud[- ]signal'
flags: i
---
