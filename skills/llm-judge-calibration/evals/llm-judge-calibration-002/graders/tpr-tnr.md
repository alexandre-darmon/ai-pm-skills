---
type: regex  # TPR and TNR reported, not agreement
pattern: '\b(TPR|sensitivity|true[- ]positive rate)\b[\s\S]{0,400}\b(TNR|specificity|true[- ]negative rate)\b|\b(TNR|specificity|true[- ]negative rate)\b[\s\S]{0,400}\b(TPR|sensitivity|true[- ]positive rate)\b'
flags: i
---
