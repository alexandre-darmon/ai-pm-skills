---
type: regex  # low-confidence cases reviewed, never forced into a class
pattern: '(review|unclassified|human)[^\n]{0,80}(low[- ]confidence|below (the )?threshold)|(low[- ]confidence|below (the )?threshold|uncertain|unsure)[^\n]{0,100}(review|human|unclassified)|(never|not) (be )?forced into (a |any |one )?(class|label|category)'
flags: i
---
