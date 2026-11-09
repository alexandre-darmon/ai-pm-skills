---
type: regex  # a new threshold signed before the next run
pattern: '(thresholds?|bars?)\b[^\n]{0,80}\b(sign\w*|dated|approv\w*)\b[^\n]{0,60}\bbefore\b|\bbefore\b[^\n]{0,60}\b(next|v4|following)\b[^\n]{0,40}\b(run|eval\w*|version|release)'
flags: i
---
