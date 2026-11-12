---
type: regex  # the reshape replaces the 14-call agent loop with a fixed workflow where code does the lookups
pattern: '(lookups?|search(es)?|join|match\w*)[^\n.]{0,60}\b(in code|by code|in SQL|deterministic\w*)|\bcode (does|handles|runs|performs|makes)\b[^\n.]{0,40}(lookups?|search\w*|match\w*)|deterministic (lookups?|matching|code)|fixed workflow'
flags: i
---
