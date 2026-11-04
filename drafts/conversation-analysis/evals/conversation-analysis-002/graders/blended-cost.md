---
type: regex  # the cost of the routed setup
pattern: '(blended|weighted|combined|mixed)[^\n]{0,25}(cost|price)|(effective|average) (cost|price) (per|of the|at)|cost[^\n]{0,30}(blended|at the threshold|with routing)|[×x*]\s*0[.,]0004[^\n]{0,40}\+[^\n]{0,40}[×x*]\s*0[.,]012|0[.,]0004\s*[×x*][^\n]{0,30}\+[^\n]{0,30}0[.,]012'
flags: i
---
