---
type: regex
pattern: '(standing|always[- ]on|default|mandatory|standard|global)[- ](filter|exclusion)\w*[^\n]{0,100}\b(golden|pairs?|cases?|fail\w*|missing|omit\w*|dropp\w*)\b|\b(golden|pairs?|cases?|fail\w*|missing|omit\w*|dropp\w*)\b[^\n]{0,100}\b(test|internal|cancel\w*|fraud\w*|standing|default|mandatory|standard)\b[^\n]{0,30}\b(filter|exclusion)|\b(filter|exclusion)s?\b[^\n]{0,40}\b(test|internal|cancel\w*|fraud\w*)\b[^\n]{0,60}\b(missing|omit\w*|dropp\w*|forgot\w*)'
flags: i
---
