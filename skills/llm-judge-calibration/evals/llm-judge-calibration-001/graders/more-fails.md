---
type: regex  # the test needs more expert fails: TNR rests on 24 only
pattern: '(more|additional|extra|at least \d+|≥ ?\d+|>= ?\d+|about \d+|around \d+|(?<![\d.,])\d{2,3})\s+(expert[- ]|handler[- ])?(labell?ed\s+)?(wrong|incorrect|misclassified|failed|failing|fail|negative|error)\s+(examples?|labels?|cases?|classifications?|items?|answers?)|(only|just) 24\b[^\n]{0,100}(too few|not enough|small|wide|indicative|imprecise|uncertain)|enrich\w*[^\n]{0,80}(wrong|misclassif|fail|error)|(wrong|misclassified|fail\w*|negative)\s+(examples|labels|cases|classifications)[^\n]{0,40}(too few|not enough|scarce)'
flags: i
---
