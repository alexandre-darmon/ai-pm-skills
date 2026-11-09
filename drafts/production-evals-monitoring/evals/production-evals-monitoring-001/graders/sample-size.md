---
type: regex  # a computed sample size per class and period
pattern: '\bn\s*(≥|>=|=|≈|~)\s*\d{2,4}\b|(?<![\d,.])\b\d{2,4}\s+(sampled\s+|judged\s+|random\s+|randomly drawn\s+)?(traces|answers|conversations|questions|interactions|responses)\b[^\n]{0,60}\b(per|each|a|every)\s+(class|category|week|month|day)\b'
flags: i
---
