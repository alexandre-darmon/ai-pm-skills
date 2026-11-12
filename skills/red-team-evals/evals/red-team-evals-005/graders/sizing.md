---
type: regex  # held-out seeds per class sized on the Wilson bound: about 4/r, 765 to 800 at 0.5%, 381 to 384 at 1%, 1,130 with one success
pattern: '\b4 ?/ ?r\b|\b3[.,]84 ?/|\b(38[0-4]|76[4-9]|800|1[,. ]?1[0-5]0)\b[^\n]{0,60}(attacks?|seeds?|prompts?|cases?|ideas?)|(attacks?|seeds?|prompts?|cases?)[^\n]{0,40}\b(38[0-4]|76[4-9]|800|1[,. ]?1[0-5]0)\b'
flags: i
weight: 2
---
