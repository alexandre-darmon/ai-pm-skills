---
type: regex  # turns the bound into payments a month
pattern: '\b(11\d|120)\b[^\n.]{0,60}(payments?|a month|per month|monthly)|(up to|as many as|about|≈|~)\s*(11\d|120)\b|(10 ?%|0[.,]10?|9[.,]5 ?%|0[.,]095)\s*(×|x|\*|of)\s*(the )?1[ ,.]?200'
flags: i
---
