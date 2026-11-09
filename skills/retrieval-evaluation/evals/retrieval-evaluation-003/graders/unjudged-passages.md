---
type: regex  # passages the new model surfaces are judged before comparing
pattern: '\bpool\w*|unjudged|(not yet|never|un)[- ]?(labell?ed|judged)[^\n]{0,60}(passages|sections|results|chunks)|(new|newly)[^\n]{0,30}(retrieved|surfaced|returned)[^\n]{0,80}(label|judg|review)'
flags: i
---
