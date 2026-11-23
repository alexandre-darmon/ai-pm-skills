---
type: regex  # a cap on the refund endpoint is generic; the skill ties caps to autonomy: any move past L2 is limited to small amounts or under a cap
pattern: '\bL[345]\b[^\n|]{0,60}(≤|<=?)\s?(\d[\d,.]*\s?(EUR|€)|€\s?\d)|\bL[345]\b[^\n|]{0,60}\b(caps?|capped|ceiling|low[- ]value|small(er)? amounts?|(under|below|up to|max(imum)?) (a |an )?(\d[\d,.]*\s?(EUR|€)|€\s?\d|set amount|fixed amount|amount|threshold|limit))|\b(caps?|capped|ceiling|low[- ]value|small amounts?)\b[^\n|]{0,40}\bL[345]\b|\bautonom\w*[^\n|]{0,30}\b(caps?|ceiling|limit\w*)?\s*(by|under|below|up to) (a |an |the )?(amount|cap|ceiling|threshold|value)'
flags: i
---
