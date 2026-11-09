---
type: regex  # the threshold is signed and dated before the run it judges
pattern: '(thresholds?|bars?|pass marks?)\b[^\n]{0,100}\b(sign\w*|dated|approv\w*)\b|\b(sign\w*|dated|approv\w*)\b[^\n]{0,60}\b(thresholds?|bars?|pass marks?)\b'
flags: i
---
