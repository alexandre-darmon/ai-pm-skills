---
type: regex  # wrong-country policy is the largest mode, 7 traces
pattern: '\b(7|seven)\b[^\n]{0,400}(countr|entit|jurisdiction|French (rule|polic)|wrong[- ](country|polic|rule))|(countr|entit|jurisdiction|French (rule|polic))[^\n]{0,400}\b(7|seven)\b'
flags: i
---
