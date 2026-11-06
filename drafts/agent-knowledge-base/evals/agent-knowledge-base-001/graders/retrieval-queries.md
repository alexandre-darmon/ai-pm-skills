---
type: regex
pattern: '\b(labell?ed|gold(en)?|test|reference|benchmark)\b[^\n.]{0,20}\b(quer\w*|questions?)\b[^\n.]{0,120}\b(retriev\w*|(right|correct|expected) (source|document|chunk)s?|recall)\b|\b(retriev\w* (tests?|evals?|evaluations?|recall|hit rate|precision)|recall@\w*)[^\n.]{0,60}\b(quer\w*|questions?)\b|\b(quer\w*|questions?)\b[^\n.]{0,60}\b(expected|correct|right) (source|document|chunk)s?\b'
flags: i
---
