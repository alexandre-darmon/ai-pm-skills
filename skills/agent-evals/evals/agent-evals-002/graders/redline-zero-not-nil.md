---
type: regex  # red line: zero wrong payments in 30 trials is a bound of about 10%, not nil
pattern: 'rule of three|\b3 ?/ ?(n|30)\b|≈ ?3 ?/|(zero|no|0|none)[^\n]{0,160}\b(up to|as high as|still (allow|permit|compatible|consistent)\w*|upper bound|cannot rule out|can.t rule out|not rule out)\b[^\n]{0,40}\d+([.,]\d+)? ?%|\b(9[.,]5|10) ?%[^\n]{0,80}(upper bound|cannot (be )?ruled? out|still possible)'
flags: i
weight: 3
---
