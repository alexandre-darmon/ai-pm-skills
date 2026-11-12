---
type: regex  # the sample is sized from the error rate it must bound or detect, not picked as a round share
pattern: 'rule of three|\b3 ?(/|÷|divided by) ?n\b|zero (errors?|misroutes?|mistakes?) in \d|\b(size|sized|sizing)\b[^\n.]{0,40}\b(to|so (it|that|you))\b[^\n.]{0,40}\b(estimate|detect|bound|measure)\w*\b[^\n.]{0,40}\b(errors?|misroutes?|rates?|change|drops?)\b'
flags: i
---
