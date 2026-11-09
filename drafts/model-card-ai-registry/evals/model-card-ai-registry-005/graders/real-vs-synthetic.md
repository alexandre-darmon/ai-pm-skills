---
type: regex  # results on real cases reported apart from generated ones
pattern: '(real|synthetic|generated)[- ](only |cases? )?(results?|scores?|pass rates?|subset)|(score|results?|pass rate)[^\n]{0,40}\b(on|for) (the )?(120 )?real (cases|files)|separately[^\n]{0,60}(real|synthetic|generated)|(real|synthetic|generated)[^\n]{0,60}(separately|apart)'
flags: i
---
