---
type: regex  # logs kept at least six months, cited to art. 26(6) or dated (2 December 2027) on the same line
pattern: '(six|6)[- ]months?[^\n]{0,160}(\b26\s*\(6\)|\bDec(ember|\.)?\s+2027\b)|(\b26\s*\(6\)|\bDec(ember|\.)?\s+2027\b)[^\n]{0,160}(six|6)[- ]months?'
flags: i
---
