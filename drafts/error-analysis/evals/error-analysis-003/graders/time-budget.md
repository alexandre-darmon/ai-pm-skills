---
type: regex  # the expert reading fits before Friday
pattern: '\b\d+(?:[.,]\d+)?\s*(?:(?:-|–|to)\s*\d+\s*)?(hours?|hrs?|minutes?|mins?|days?|half[- ]days?)\b[^\n]{0,100}(read|annotat|trace|conversation|open[- ]cod)|(read|annotat|open[- ]cod)\w*[^\n]{0,100}\b\d+(?:[.,]\d+)?\s*(?:(?:-|–|to)\s*\d+\s*)?(hours?|hrs?|minutes?|mins?|days?)\b|\b(a|one|half a) (day|afternoon|morning)\b[^\n]{0,80}(read|annotat|trace|conversation)|(read|annotat|open[- ]cod)\w*[^\n]{0,160}\b(half a day|a (full )?day|one day|an? (afternoon|morning))\b'
flags: i
---
