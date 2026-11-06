---
type: regex
pattern: '\b(?:eval\w*|test\w*|sample|87\s?%|60 contracts)\b[^\n]{0,120}(?<!\bto\s)\b(?:date|dated)\b|(?<!\bto\s)\b(?:date|dated)\b[^\n]{0,120}\b(?:eval\w*|test\w*|sample|87\s?%|60 contracts)\b'
flags: i
---
