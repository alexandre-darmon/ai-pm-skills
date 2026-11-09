---
type: regex  # humans keep checking every classification until the judge passes
pattern: '(keep|keeps|keeping|continue|continues|maintain|maintains|stay|stays|remain|remains)\b[^\n]{0,60}\b(full|every|all|100 ?%)\b[^\n]{0,30}(check|review)|(stay|stays|remain|remains|keep)\w*\s+(\w+\s+){0,2}?(at|on) L2\b'
flags: i
---
