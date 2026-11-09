---
type: regex  # each alert has an owner and a response time
pattern: 'owner[^\n]{0,150}(within|response time|\d+\s?(h\b|hours?|working days?|business days?|days?))|(within|response time)[^\n]{0,100}owner|\|\s*[^|\n]{2,60}\|\s*(within )?\d+\s?(h|hours?|working days?|business days?|days?)\s*\|'
flags: i
---
