---
type: regex
pattern: 'acceptance criteri\w*\W{0,8}[^\n]{0,30}\b(must|should) be (fast|accurate|quick)\b'
flags: i
match: not_contains
weight: 5
---
