---
type: regex  # the suite built from historical tickets gives each model only the fields known when the ticket arrives
pattern: '(fields?|information|data|inputs?|what)[^\n]{0,40}\b(known|available|present|existed)\b[^\n]{0,30}\b(when|at|before|by)\b[^\n]{0,30}(arriv|triage|decision|creat|submi|open|classif|intake|routing)|leak\w*[^\n]{0,80}(resolution|agent notes|after triage|final category|later|added after)|(resolution (text|notes)|agent notes|added after triage|after the fact)[^\n]{0,60}(leak|inflat|out)'
flags: i
---
