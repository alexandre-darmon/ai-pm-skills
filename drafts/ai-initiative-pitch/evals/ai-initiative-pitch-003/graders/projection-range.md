---
type: regex
pattern: '^(?=[\s\S]*\b(projection|projected|forecast|estimated (gain|saving|value|roi))\b)(?=[\s\S]*(\d[\s\S]{0,40}\b(low|conservative)\b[\s\S]{0,160}\b(high|optimistic)\b|\b(low|conservative)\b[\s\S]{0,160}\b(high|optimistic)\b[\s\S]{0,60}\d|\d[\d,.]*\s?(k|M)?\s?(EUR|€|min\w*)?\s?(–|-|to)\s?\d[\d,.]*\s?(k|M)?\s?(EUR|€|min)|\bbetween\s+\d[\d,.]*\s?(k|M)?\s?(EUR|€|min\w*)?\s+and\s+\d))'
flags: i
---
