---
type: regex  # the app refuses to save a label without the reviewer's identity, and a change of mind is a new row, never an overwrite
flags: i
---
(refus|block|reject|disallow|prevent|cannot|can.t|won.t)\w*[^\n]{0,30}\bsav\w*[^\n]{0,40}\b(without|unless|missing|lacks?)\b|\b(no|never)\b[^\n]{0,20}\b(label|row|record)s?\b[^\n]{0,30}without[^\n]{0,20}(reviewer|identity|user|login)|change of mind[^\n]{0,40}(new|append)|(never|not|no|without) (an? )?overwrit|append[- ]only
