---
type: regex  # every incident adds a regression case to the golden set
pattern: '(regression|eval|test)[- ]cases?\b[^\n]{0,80}\b(golden|eval|test|regression)[- ](set|suite)|\b(golden|eval|test)[- ](set|suite)\b[^\n]{0,80}\b(regression|new) (eval |test )?cases?|error[- ]analysis|\b(add|turn|put|feed)\w*\b[^\n.]{0,50}\b(cases?|examples?|claims?|incidents?)\b[^\n.]{0,30}\b(to|into|in) (the |a |your )?(regression|golden|eval|test)[- ](set|suite)\b|\bregression cases from (the|each|every|an?) incident'
flags: i
---
