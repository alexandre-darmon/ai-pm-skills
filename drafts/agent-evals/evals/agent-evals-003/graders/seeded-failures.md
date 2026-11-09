---
type: regex  # tool failures seeded at the last write on purpose
pattern: '(seed|inject|simulat|forc)\w*[^\n.]{0,60}(fail|error|time[- ]?outs?|exception|5\d\d)|fault[- ]injection|test double[^\n.]{0,60}(fail|error|time[- ]?out)'
flags: i
---
