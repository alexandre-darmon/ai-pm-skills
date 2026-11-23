---
type: regex  # challenging the 30% is generic; the skill says what would anchor it: volume × quality (share answered correctly) × unit value, not only "a baseline"
pattern: '30 ?%[^\n]{0,200}\bvolumes?\b[^\n]{0,40}\b(quality|accura\w*|correct\w*|error rate)\b|\bvolumes?\b[^\n]{0,40}\b(quality|accura\w*|correct\w*)\b[^\n]{0,40}\b(unit value|value|cost|minutes?)\b[^\n]{0,200}30 ?%'
flags: i
---
