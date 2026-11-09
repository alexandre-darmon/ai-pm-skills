---
type: regex  # a computed sample size per class and period
pattern: '\bn\s*(≥|>=|=|≈|~)\s*\d{2,4}\b|(?<![\d,.])\b\d{2,4}\s+(sampled\s+|judged\s+|random\s+|randomly drawn\s+)?(traces|answers|conversations|questions|interactions|responses)\b[^\n]{0,60}\b(per|each|a|every)\s+(class|category|week|month|day)\b|\|\s*(judged|sampled|sample size|traces|answers)[^|\n]{0,20}\bper (week|class|month|day)\b[^\n]*\n([^\n]*\n){0,6}?[^\n]*\|\s*(about |~|≈\s?)?\d{2,4}\b'
flags: i
---
