---
type: regex  # faithfulness checked claim by claim
pattern: 'claim[- ]level|(each|every|per|individual|atomic|single) (factual )?(claim|statement|sentence|assertion)s?\b|split[^\n]{0,40}(claims|statements)|decompos\w*[^\n]{0,30}(claims|statements)'
flags: i
---
