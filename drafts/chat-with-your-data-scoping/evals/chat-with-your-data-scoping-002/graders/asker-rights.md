---
type: regex
pattern: 'row[- ]level|column[- ]level|(asker|asking user|requesting user|authenticated user|logged[- ]in user|each user|end user|user)(\x27s|s\x27|’s)?\s+(own\s+)?(rights|permissions?|entitlements?)\b|\b(run|runs|execute|executes|running)\b[^\n.]{0,30}\b(as|under|with)\b[^\n.]{0,20}\b(the )?(asker|asking|requesting|authenticated|logged[- ]in|user)'
flags: i
---
