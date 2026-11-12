---
type: regex  # personal data masked before the external judge
pattern: '(mask|pseudonymi[sz]|redact|anonymi[sz])\w*[^\n]{0,120}\b(before|prior to)\b[^\n]{0,80}(judge|LLM|model|evaluat|external|API|vendor|provider|reviewer)|(judge|evaluator)s?[^\n]{0,80}\b(only|never)\b[^\n]{0,60}(masked|pseudonymi|redact|unmasked)'
flags: i
---
