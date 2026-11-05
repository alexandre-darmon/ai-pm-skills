---
type: regex  # the masking is checked by hand on a sample
pattern: '(residual|leak|missed)[^\n]{0,60}(rate|check|sample|review)|(check|verify|review|read|audit)[^\n]{0,60}(masked|masking)[^\n]{0,60}(sample|by hand|manually)|(sample|by hand|manually)[^\n]{0,60}(masked|masking)'
flags: i
---
