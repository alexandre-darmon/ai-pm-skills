---
type: regex  # tokens and cost per call
flags: i
---
token\w*[^\n]{0,60}(cost|EUR|€)|(cost|EUR|€)[^\n]{0,60}token
