---
type: regex  # notes go on the first upstream failure
pattern: 'first[^\n]{0,20}(upstream )?(failure|error|mistake|step that (went|goes) wrong)|upstream|\b(record|count|log|file|code|note)\w*[^\n]{0,30}\bretrieval\b[^\n]{0,20}\bas (the|one|a) (failure|error)|\b(wrong|bad) (retrieval|clause)[^\n]{0,80}\b(counts?|recorded|logged|filed|coded) as (one|a|the)\b'
flags: i
---
