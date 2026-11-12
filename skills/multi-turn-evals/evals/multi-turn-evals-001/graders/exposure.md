---
type: regex  # prices the rate in conversations a month, on the long conversations the sample represents
pattern: '\b1[ ,.]?(0[5-9]\d|1[0-2]\d)\b[^\n]{0,60}(conversations?|customers?|quotes?|a month|per month|monthly|/ ?month)|5[ ,.]?400[^\n]{0,20}(×|x|\*|times)[^\n]{0,10}(0[.,]2|20 ?%)'
flags: i
---
