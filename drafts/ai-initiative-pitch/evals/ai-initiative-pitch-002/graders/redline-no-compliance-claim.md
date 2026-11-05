---
type: regex
pattern: '(?<!\b(?:not|never|no|non)\b[^\n.]{0,25})\b(is|are|be|fully|already) compliant\b'
flags: i
match: not_contains
weight: 5
---
