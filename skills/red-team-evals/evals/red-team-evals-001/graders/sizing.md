---
type: regex  # the per-class n computed on the Wilson bound: about 4/r, 765 to 800 held-out seeds at 0.5%, 381 to 400 at 1%
pattern: '\b4 ?/ ?r\b|\b3[.,]84 ?/|\b(38[0-4]|76[4-9]|400|800|1[,. ]?1[0-5]0)\b[^\n]{0,60}(attacks?|attempts?|seeds?|prompts?|cases?|probes?)|(attacks?|attempts?|seeds?|prompts?|cases?)[^\n]{0,40}\b(38[0-4]|76[4-9]|400|800|1[,. ]?1[0-5]0)\b'
flags: i
weight: 2
---
