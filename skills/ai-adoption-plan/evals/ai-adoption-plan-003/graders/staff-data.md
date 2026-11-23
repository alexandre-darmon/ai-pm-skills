---
type: regex  # what is logged about technicians is listed item by item (queries, overrides, corrections, time per task, identifiers), so who sees each item can be settled with the DPO before any wave
pattern: '\b(logs?|logged|records?|recorded|collects?|collected|stores?|stored)\b[^\n]{0,40}\b(queries|questions asked|overrides?|corrections?|time (spent )?per (task|job|intervention)|user ids?|(technician|personal|per[- ]technician) (ids?|identifiers?)|identifiers?)\b,[^\n]{0,60}\b(queries|overrides?|corrections?|time (spent )?per (task|job|intervention)|user ids?|identifiers?)\b'
flags: i
---
