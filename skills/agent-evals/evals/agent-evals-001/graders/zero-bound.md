---
type: regex  # zero observed is a bound, not zero risk
pattern: 'rule of three|\b3 ?/ ?n\b|≈ ?3 ?/|(zero|no|0) (failures?|errors?|forbidden events?|bad refunds?|wrong refunds?|incidents?)[^\n]{0,160}\b(up to|as high as|still (allow|permit)\w*|upper bound|cannot rule out|can.t rule out)\b'
flags: i
---
