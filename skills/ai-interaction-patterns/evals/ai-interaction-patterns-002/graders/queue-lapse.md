---
type: regex  # the exception queue says what happens when its SLA lapses
pattern: '\b(SLA|time[- ]?out|deadline)\b[^\n.]{0,60}\b(escalat\w*|backup|fall(s)? ?back|reassign\w*)\b|\b(escalat\w*|backup|fall(s)? ?back|reassign\w*)\b[^\n.]{0,40}\b(after|past|beyond|when|if|once|on)\b[^\n.]{0,20}\b(SLA|time[- ]?out|deadline)\b|\bSLA\b[^\n.]{0,20}\b(lapse|breach|miss|expir)\w*[^\n.]{0,80}\b(rout\w*|mov\w*|notif\w*|alert\w*|deputy|lead|manager|owner)\b'
flags: i
---
