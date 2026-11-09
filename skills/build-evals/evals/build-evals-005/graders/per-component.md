---
type: regex  # a labelled check per step, beside the end-to-end score
pattern: '(per|each|every)[- ](component|step|stage)\b[^.\n]{0,80}\b(eval|score|check|label|metric|set|accuracy)|(component|step|stage)[- ](level|wise|by[- ]step)\b[^.\n]{0,40}(eval|score|check|metric)|\b(evals?|checks?|scores?|metrics?|labell?ed sets?) (per|for each|at each|for every) (component|step|stage)\b'
flags: i
---
