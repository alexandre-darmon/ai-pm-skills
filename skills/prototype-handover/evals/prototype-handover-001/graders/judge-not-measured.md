---
type: regex  # the 88% comes from a judge whose TPR and TNR were never measured
pattern: '(?:\bjudge\b|\b88\s?%)[^.\n]{0,120}\b(?:no|not|never|without|unknown|unmeasured)\b[^.\n]{0,40}\b(?:measured|calibrat\w*|TPR|TNR|true[- ]positive)|\b(?:uncalibrated|unmeasured)\b[^.\n]{0,40}\bjudge'
flags: i
---
