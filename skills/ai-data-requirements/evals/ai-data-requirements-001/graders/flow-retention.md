---
type: regex  # the flow table is filled: a retention number per destination, which copying the template's column names does not give
pattern: '\b(logs?|logging|traces?)\b[^\n]{0,80}\b\d+\s*(hours?|days?|weeks?|months?|years?)\b|\b(masked|clear|token\w*|pseudonym\w*|redact\w*)\b[^|\n]{0,30}\b\d+\s*(hours?|days?|weeks?|months?|years?)\b'
flags: i
---
