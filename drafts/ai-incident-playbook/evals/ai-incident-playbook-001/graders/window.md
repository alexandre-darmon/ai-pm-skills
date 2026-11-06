---
type: regex
pattern: '\b(all|every|each)\b(?!\s+(of\s+)?(the\s+|those\s+|these\s+)?40\b)[^\n.]{0,40}\b(refunds?|outputs?|actions?|payouts?|transactions?)\b[^\n.]{0,60}\b(since|window|after the (prompt|change|deploy|release|update))\b|\b(not just|not only|beyond|on top of)\s+the\s+(40|ones?|reported)\b'
flags: i
---
