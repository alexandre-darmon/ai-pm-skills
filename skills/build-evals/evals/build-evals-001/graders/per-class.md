---
type: regex  # asks for each category's traffic share or sets a threshold per category, not just per-class metrics
pattern: '(traffic|volume)( share)?[^.\n]{0,20}\b(per|of each|by|for each|across) (category|class)|thresholds?[^.\n]{0,15}\b(per|for each|by) (category|class)|(per|each)[- ](category|class) thresholds?|(category|class)[- ]level thresholds?'
flags: i
---
