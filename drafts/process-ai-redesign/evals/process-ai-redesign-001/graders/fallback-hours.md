---
type: regex
pattern: '\b\d[\d,.]*\s*review\w*[- ]hours?\b|(review|validat|fallback|queue|takeover|escalat)\w*[^\n]{0,100}\b\d[\d,.]*\s*(FTE\b|(review\w*|person|staff|analyst)[- ]hours?\b|(h|hrs?|hours?)\s*(/|per |a |each |every )\s*(month|week|day|mo\b|wk\b))|\b\d[\d,.]*\s*(FTE\b|(review\w*|person|staff|analyst)[- ]hours?\b|(h|hrs?|hours?)\s*(/|per |a |each |every )\s*(month|week|day|mo\b|wk\b))[^\n]{0,100}(review|validat|fallback|queue|takeover|escalat)'
flags: i
---
