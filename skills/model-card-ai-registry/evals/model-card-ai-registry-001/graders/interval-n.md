---
type: regex  # "looks great" needs results per class with an interval, not only "a sample size"
pattern: '\binterval\b|\b(cases|results?|pass rates?|accuracy|scores?|thresholds?)\b[^\n]{0,30}\b(per|by|for each|each)[- ](question |test )?(class|category|type)\b|\b(per|by)[- ]class\b'
flags: i
---
