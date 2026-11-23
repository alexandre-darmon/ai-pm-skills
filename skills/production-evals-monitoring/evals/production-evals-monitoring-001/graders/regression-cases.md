---
type: regex  # confirmed failures become regression cases only once masked (personal data stays out of the golden set)
pattern: '(mask|pseudonymi[sz]|anonymi[sz]|redact|de-?identif)\w*[^\n]{0,100}\b(golden|regression|test|eval(uation)?) (set|suite|cases?)\b|\b(golden|regression|test|eval(uation)?) (set|suite|cases?)\b[^\n]{0,80}\b(mask|pseudonymi[sz]|anonymi[sz]|redact|de-?identif)'
flags: i
---
