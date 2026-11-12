---
type: regex  # each alert has an owner and a response time (same line, a table row, or owners named and the ladder timed)
pattern: 'owner[^\n]{0,150}(within|response time|\d+\s?(h\b|hours?|working days?|business days?|days?))|(within|response time)[^\n]{0,100}owner|\|\s*[^|\n]{2,60}\|\s*(within |same |next )?(\d+\s?(h|hours?|working days?|business days?|days?)|(working |business )?day)\s*\||^(?=[\s\S]*\bowners?\b)[\s\S]*\b(investigat|alert|page|escalat)\w*[^\n]{0,80}(within \d+\s?(h\b|hours?|working days?|business days?|days?)|same (working |business )?day)'
flags: i
---
