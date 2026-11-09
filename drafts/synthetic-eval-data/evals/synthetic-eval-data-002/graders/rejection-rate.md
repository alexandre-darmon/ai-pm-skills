---
type: regex  # expert review with a recorded rejection rate
pattern: 'reject(ion)?[- ]rate|(share|%|percent|proportion|number) (of )?(\w+ )?(rejected|discarded)|(reject|discard)\w*[^\n]{0,60}(record|track|log|count|measure)|(reject|discard)\w*[^\n]{0,40}(more than|over|above|exceed\w*|beyond)[^\n]{0,20}\d+ ?%|\d+ ?%[^\n]{0,30}\b(rejected|discarded)\b'
flags: i
---
