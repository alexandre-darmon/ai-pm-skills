---
type: regex  # red line: a quality signal per class from sampled, judged or reviewed traces; usage, latency, cost and thumbs are not quality
pattern: '(per|by|each|for every|for each)[- ](question[- ])?(class|category|use[- ]case|topic|domain|stratum)[^\n]{0,120}(sampl|judg|review|pass rate|quality|correct)|(sampl|judg|review|pass rate|quality|correct)\w*[^\n]{0,120}(per|by|each|for every|for each)[- ](question[- ])?(class|category|use[- ]case|topic|domain|stratum)|stratified[^\n]{0,40}(by|per|across) (question )?(class|category|use[- ]case|topic|domain)'
flags: i
weight: 2
---
