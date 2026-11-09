---
type: regex  # confirm the inference with a sampled or seeded review, not by opinion
pattern: '(seed|plant|inject|insert)\w*[^.\n]{0,60}(error|wrong|mistake|recommendation|claim)|(audit|second|blind|independent) (review|check)[^.\n]{0,60}(sample|claims)|\bsample\w*[^.\n]{0,60}(re-?review|audit|second look|expert)'
flags: i
---
