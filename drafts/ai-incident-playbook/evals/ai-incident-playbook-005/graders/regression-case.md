---
type: regex  # every incident adds a regression case to the golden set
pattern: '(regression|eval|test)[- ]cases?\b[^\n]{0,80}\b(golden|eval|test|regression)[- ](set|suite)|\b(golden|eval|test)[- ](set|suite)\b[^\n]{0,80}\b(regression|new) (eval |test )?cases?|error[- ]analysis'
flags: i
---
