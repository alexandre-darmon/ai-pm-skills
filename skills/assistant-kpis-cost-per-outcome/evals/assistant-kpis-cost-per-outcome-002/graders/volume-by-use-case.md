---
type: regex  # volume by use case, from traces, not declared usage
pattern: 'volume[^\n]{0,40}\b(by|per) (use case|intent|topic|request type|domain)|(sessions?|conversations?|requests?)( per (day|week|month)| a (day|month))?[^\n]{0,20}\b(by|per) use case|break(s|ing)? (it |them )?down by use case|\|\s*volume\b[^\n]*\|\s*use case\b'
flags: i
---
