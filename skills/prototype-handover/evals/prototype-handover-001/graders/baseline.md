---
type: regex  # the frozen baseline, tied to its number, is the floor engineering must reach
pattern: 'frozen baseline|baseline[^.\n]{0,60}\b(?:floor|must (?:reach|match|beat))|\bfloor\b[^.\n]{0,60}\bbaseline|baseline[^.\n]{0,40}(?:\b364\b|\b91\s?%)|(?:\b364\b|\b91\s?%)[^.\n]{0,40}\bbaseline'
flags: i
---
