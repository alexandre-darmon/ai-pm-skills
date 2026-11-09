---
type: regex  # retrieval scored at the k the generator receives
pattern: 'recall\s*@\s*5|recall at (k ?= ?)?5|hit rate|recall[^\n]{0,60}(top[- ]?5|k ?= ?5|five)|(top[- ]?5|k ?= ?5)[^\n]{0,60}recall'
flags: i
---
