---
type: regex
pattern: 'pay_goodwill[^\n]{0,80}\b(no cap|uncapped|unlimited)\b|pay_goodwill(?!`?\s+(?:\w+\s+)?to L[0-2]\b)[^\n]{0,80}\bno approval\b'
flags: i
match: not_contains
weight: 5
---
