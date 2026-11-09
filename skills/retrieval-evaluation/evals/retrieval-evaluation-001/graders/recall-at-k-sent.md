---
type: regex  # retrieval scored at the k the generator receives
pattern: 'recall\s*@\s*5|recall at (k ?= ?)?5|hit rate|recall[^\n]{0,60}(top[- ]?5|k ?= ?5|five)|(top[- ]?5|k ?= ?5)[^\n]{0,60}recall|recall[^\n]{0,60}\b(5|five) (chunks|pieces|passages)\b|\b(needed|right|relevant|correct|answer-bearing) (passage|piece|chunk)s?\b[^\n]{0,30}\bin the (top[- ]?)?(5|five)\b[^\n]{0,20}\b(sent|passed|given|received)\b'
flags: i
---
