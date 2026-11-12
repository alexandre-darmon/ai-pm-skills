---
type: regex  # a few dozen synthetic cases sized per type, not 2,000 records
pattern: '\b(1[2-9]|[2-4]\d)\b[^\n]{0,30}per ([\w-]+ )?(class|category|type)|\b([4-9]\d|1[0-4]\d)\b (synthetic|anonymi[sz]ed|pseudonymi[sz]ed|fictitious|hand[- ]written|written|realistic)[^\n]{0,20}(complaints|cases|examples)|\b(40|50|60)\s?(to|–|-|and)\s?(80|90|100|120)\b[^\n]{0,40}(cases|complaints|examples)'
flags: i
---
