---
type: regex  # labels split into few-shot pool, dev and test
pattern: '\bdev(elopment)?\b[^\n]{0,120}\btest\b|\btest\b[^\n]{0,120}\bdev(elopment)?\b|(few[- ]shot|example)s?\s+(pool|split)|\bvalidation (set|split)\b[^\n]{0,120}\btest\b|\btest\b[^\n]{0,120}\bvalidation (set|split)\b'
flags: i
---
