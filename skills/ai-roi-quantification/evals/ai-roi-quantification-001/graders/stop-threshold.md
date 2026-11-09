---
type: regex
pattern: '\b(stop|shrink|kill|wind down|switch off|do not renew|don[’'']t renew|not renew)\b[^\n]{0,80}(\b(if|when|below|under|less than|unless)\b|<)[^\n]{0,60}\d|(\b(if|when|below|under|less than)\b|<)[^\n]{0,80}\d[^\n]{0,80}\b(stop|shrink|kill|wind down|switch off|do not renew|don[’'']t renew|not renew)\b|\b(stop|kill|shrink)[- ](threshold|condition|trigger|point)[^\n]{0,80}\d'
flags: i
---
