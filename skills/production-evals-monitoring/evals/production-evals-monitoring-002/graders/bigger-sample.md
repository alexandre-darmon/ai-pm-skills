---
type: regex  # a sample large enough to see a 5-point drop (about 300 a week), or a larger sample
pattern: '(?<![\d,.])\b(29\d|3[0-2]\d|52\d)\b[^\n]{0,60}\b(traces|conversations|samples?|per week|a week|weekly|each week)\b|\bn\s*(≥|>=|=|≈|~)\s*(29\d|3[0-2]\d|52\d)\b|\b(increase|raise|enlarge|grow|double|triple|quadruple|bigger|larger)\w*\b[^\n]{0,40}\b(sample|the n\b)'
flags: i
---
