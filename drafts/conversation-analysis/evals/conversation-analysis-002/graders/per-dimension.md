---
type: regex  # the 78% and 92% are split by dimension
pattern: '(per|by|each|for every|on each)[- ]dimension|(use[- ]case|resolution)[^\n]{0,60}\bseparately\b|separately[^\n]{0,30}(use[- ]case|resolution)|\d+ ?%[^\n]{0,20}(on|for) (the )?(use[- ]case|resolution)[^\n]{0,40}\d+ ?%[^\n]{0,20}(on|for) (the )?(use[- ]case|resolution)|\|\s*agreement:? (use[- ]case|resolution)'
flags: i
---
