---
type: regex
pattern: 'indirect (prompt )?injection|\b(retrieved|document\w*|polic(y|ies)|upload\w*)\b[^\n]{0,80}\b(as data|are data|is data|not (as )?(instructions?|commands?)|never (as )?(instructions?|commands?)|untrusted)\b|\b(instructions?|commands?|injections?|attacks?)\b[^\n.]{0,40}\b(in|inside|within|embedded in|hidden in|planted in)\b[^\n.]{0,30}\b(retrieved|(a|the|policy|hr) (document|file|pdf|page)s?|documents|uploads?|uploaded)\b'
flags: i
---
