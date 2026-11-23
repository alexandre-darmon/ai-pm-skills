---
type: regex  # zero observed is a bound, turned into bad refunds a month at the real volume
pattern: '(?<![\d,.])(?!9[ ,.]?000\b)\d[\d,.]*\s*(wrong(ly issued)?|bad|forbidden|wrong-money)?\s*(refunds?|refund events|events|errors|payouts?)( events)? (a|per|each) month|\b\d+([.,]\d+)? ?%[^\n|]{0,30}\bof (the )?9[ ,.]?000\b'
flags: i
---
