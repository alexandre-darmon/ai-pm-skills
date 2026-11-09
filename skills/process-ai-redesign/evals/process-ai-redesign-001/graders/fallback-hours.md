---
type: regex
pattern: '\b\d[\d,.]*\s*review\w*[- ]hours?\b|(review|validat|fallback|queue|takeover|escalat)\w*[^\n]{0,100}\b\d[\d,.]*\s*(FTE\b|(review\w*|person|staff|analyst)[- ]hours?\b|(h|hrs?|hours?)\s*(/|per |a |each |every )\s*(month|week|day|mo\b|wk\b))|\b\d[\d,.]*\s*(FTE\b|(review\w*|person|staff|analyst)[- ]hours?\b|(h|hrs?|hours?)\s*(/|per |a |each |every )\s*(month|week|day|mo\b|wk\b))[^\n]{0,100}(review|validat|fallback|queue|takeover|escalat)|(human )?fallback[^\n]{0,80}\breview\w*[- ]hours?\s*(=|\(|is|are)|\breview\w*[- ]hours?\s*=\s*[^\n]{0,40}(items?|files?|volume|cases?)|\breview\w*[- ]hours?,? formula|formulas?[^\n]{0,80}\bsizing the (human )?fallback|\breview\w*[- ]hours?\s*(/|per )\s*(month|week|day)\s*\|\s*\**\s*\d|time per item\s*=\s*review\w*[- ]hours?'
flags: i
---
