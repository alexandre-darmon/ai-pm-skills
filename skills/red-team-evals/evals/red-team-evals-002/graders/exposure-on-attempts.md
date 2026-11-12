---
type: regex  # exposure is read on estimated attack attempts a month (the method); omitting it costs this grader, not the red line
pattern: '(attack attempts?\b[^.!?\n]{0,40}\b(a|per|each|every) month|monthly attack (attempts|volume|traffic)|attempt (count|volume|estimate)|(number|count|share|volume|estimate|proportion) of (monthly )?(attack attempts|attacks|attackers|malicious (conversations|users|attempts)|adversarial (conversations|users|attempts))|how many (of (them|those|these|the conversations) )?(are|were|would be|will be) (attacks|attack attempts|adversarial|malicious)|(don[''’]t|do not|never|not)\b[^.!?\n]{0,20}\b(use|apply|base\w*|multiply|read)\b[^.!?\n]{0,25}(25[,. ]?000|conversation))'
flags: i
---
