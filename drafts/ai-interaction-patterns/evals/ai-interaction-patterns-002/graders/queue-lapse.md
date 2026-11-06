---
type: regex
pattern: '\b(SLA|time[- ]?out|deadline)\b[^\n.]{0,60}\b(escalat\w*|backup|fall(s)? ?back|reassign\w*)\b|\b(escalat\w*|backup|fall(s)? ?back|reassign\w*)\b[^\n.]{0,40}\b(after|past|beyond|when|if|once|on)\b[^\n.]{0,20}\b(SLA|time[- ]?out|deadline)\b'
flags: i
---
