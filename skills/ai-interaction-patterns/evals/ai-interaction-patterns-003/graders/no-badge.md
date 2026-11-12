---
type: regex  # no confidence badge until the score is checked against outcomes
pattern: '(badge|score|confidence)[^.\n]{0,80}\b(only (if|once|when|after)|until|unless|not before)\b[^.\n]{0,60}(calibrat|measured|checked|validated|compared)|(no|drop|remove|hold|without) (the )?(green |"high confidence" |confidence )?badge'
flags: i
---
