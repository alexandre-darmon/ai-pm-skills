---
type: regex  # a named rate for each expert class (TPR and TNR, or recall/catch rate with specificity/false-alarm rate/pass rate on good), not agreement
pattern: '\b(TPR|sensitivity|true[- ]positive rate|recall|catch[- ]rate)\b[\s\S]{0,400}\b(TNR|specificity|true[- ]negative rate|false[- ]alarm rate|false[- ]positive rate|pass[- ]rate( target| on (the )?(good|fine)| for (the )?(good|fine)| \(judge passes))\b|\b(TNR|specificity|true[- ]negative rate|false[- ]alarm rate|false[- ]positive rate|pass[- ]rate( target| on (the )?(good|fine)| for (the )?(good|fine)| \(judge passes))\b[\s\S]{0,400}\b(TPR|sensitivity|true[- ]positive rate|recall|catch[- ]rate)\b|share of (good|fine|correct)\b[^\n]{0,60}\bpass\w*[^\n]{0,80}share of (bad|failing|wrong)\b[^\n]{0,60}\bfail'
flags: i
---
