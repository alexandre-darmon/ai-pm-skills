---
type: regex  # tool failures seeded at the last write on purpose
pattern: '(seed|inject|simulat|forc)\w*[^\n.]{0,60}(fail|error|time[- ]?outs?|exception|5\d\d)|fault[- ]injection|test double[^\n.]{0,60}(fail|error|time[- ]?out)|\b(make|have|let)\s+[`''"]?\w+[`''"]?\s+(fail|error|time[- ]?out|throw|return (an? )?(error|failure|timeout|nothing|empty))|tasks? where[^\n.]{0,60}\b(fails?|errors?|times? out|returns? (nothing|an? error|empty))\b'
flags: i
---
