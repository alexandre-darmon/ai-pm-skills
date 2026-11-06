---
type: regex
pattern: '\bvolumes?\b[^\n]{0,60}(\d|not (given|stated|provided|known|specified)|unknown|missing|to (ask|confirm|provide)|open (question|item))|\bvolumes?\b[^\n]*\|[^\n]*\n\s*\|[-| :]+\n[^\n]*\d|\b(?:queries|searches|requests|calls)\s*(?:/|per|a|each)\s*(?:second|sec|minute|min|hour|day|week|month)\b|\bqp[sm]\b'
flags: i
---
