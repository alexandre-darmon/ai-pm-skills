---
type: regex  # the cost of the routed setup
pattern: '(blended|weighted|combined|mixed)[^\n]{0,25}(cost|price)|(effective|average) (cost|price) (per|of the|at)|cost[^\n]{0,30}(blended|at the threshold|with routing)|[×x*]\s*0[.,]0004[^\n]{0,40}\+[^\n]{0,40}[×x*]\s*0[.,]012|0[.,]0004\s*[×x*][^\n]{0,30}\+[^\n]{0,30}0[.,]012|\b(if|when) \d+ ?% [^\n]{0,80}\bcost\b[^\n]{0,30}\d|\bcost\b[^\n]{0,20}\b(24 EUR|about \d+ EUR)[^\n]{0,30}(plus|\+)[^\n]{0,40}(share|escalat)|\bescalated share\b'
flags: i
---
