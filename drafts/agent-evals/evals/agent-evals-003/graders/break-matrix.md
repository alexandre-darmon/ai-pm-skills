---
type: regex  # failures counted in a last-success by first-failure matrix
pattern: '(matrix|cross[- ]?tab|grid)[^\n]{0,100}(last|first)[- ](successful|good|failing|failed)|(last|first)[- ](successful|good|failing|failed)[^\n]{0,100}(matrix|cross[- ]?tab|grid)|last success\w*[^\n]{0,30}(×|\bx\b|vs\.?|versus|by|against)[^\n]{0,30}first fail|last[- ](successful|good|correct|passing)[- ]?(step|call)?[^\n]{0,60}first[- ](failing|failed|bad|broken|wrong)[- ]?(step|call)|first[- ](failing|failed|bad|broken|wrong)[- ]?(step|call)[^\n]{0,60}last[- ](successful|good|correct|passing)'
flags: i
---
