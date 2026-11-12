---
type: regex  # test the reviewers with known-wrong recommendations and their catch rate, not only an audit of the tool
pattern: '(seed|plant|inject|insert|slip)\w*[^.\n]{0,60}(wrong|incorrect|erroneous|flipped|errors?|mistakes?|canar(y|ies)|test (case|claim|item)s?)|catch[- ]rate|\bcanar(y|ies)\b[^.\n]{0,40}(claims?|recommendations?|cases?|tests?)'
flags: i
---
