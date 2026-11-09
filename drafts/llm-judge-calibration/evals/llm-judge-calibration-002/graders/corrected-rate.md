---
type: regex  # the weekly pass rate is corrected for the judge errors (Rogan-Gladen)
pattern: 'rogan|gladen|corrected (weekly )?(pass )?rate|(correct|adjust)\w*[^\n]{0,80}(pass rate|rate)[^\n]{0,120}(TPR|TNR|sensitivity|specificity|error rates?|judge[’'']?s? (own )?errors|false (pass|fail|positive|negative))|TPR ?\+ ?TNR ?[−-] ?1|\(observed ?\+ ?TNR'
flags: i
---
