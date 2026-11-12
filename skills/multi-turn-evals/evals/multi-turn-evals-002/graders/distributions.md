---
type: regex  # compares simulated and real conversations as distributions
pattern: '(distribution|median|percentile|p90|histogram)[^\n]{0,100}(length|turns?|messages?|corrections?|vague|incomplete|abandon)|(compare|match|check)\w*[^\n.]{0,60}(simulat\w*|synthetic)[^\n.]{0,60}(against|with|to) (the )?real'
flags: i
---
