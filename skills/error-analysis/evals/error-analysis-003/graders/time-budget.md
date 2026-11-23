---
type: regex  # the time budget is for the expert's first reading to saturation (before any LLM labelling), not for checking LLM labels afterwards
pattern: '(\bexpert\w*\b|\bread\w*\b[^\n]{0,60}\bfirst\b)[^\n]{0,100}(\b\d+(?:[.,]\d+)?\s*(?:(?:-|–|to)\s*\d+(?:[.,]\d+)?\s*)?(hours?|hrs?|h|minutes?|mins?|days?)\b|\bhalf an? (day|afternoon|morning)\b|\b(a|one) (day|afternoon|morning)\b)|(\b\d+(?:[.,]\d+)?\s*(?:(?:-|–|to)\s*\d+(?:[.,]\d+)?\s*)?(hours?|hrs?|h|minutes?|mins?|days?)\b|\bhalf an? (day|afternoon|morning)\b|\b(a|one) (day|afternoon|morning)\b)[^\n]{0,60}\b(of |for )?(one|a single|an?|the) (domain |accountable )?expert|\bexpert[- ]hours?\b|(?:^|\n)(?=[^\n]*(\b\d+(?:[.,]\d+)?\s*(?:(?:-|–|to)\s*\d+(?:[.,]\d+)?\s*)?(hours?|hrs?|h|minutes?|mins?|days?)\b|\bhalf an? (day|afternoon|morning)\b|\b(a|one) (day|afternoon|morning)\b))(?=[^\n]*\b(nothing new|no new|in a row|saturat\w*|free[- ](text )?notes?|open[- ]cod\w*))'
flags: i
---
