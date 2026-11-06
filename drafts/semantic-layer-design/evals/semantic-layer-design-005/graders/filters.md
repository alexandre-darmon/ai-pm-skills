---
type: regex
pattern: '\b(standing|mandatory|default|always[- ]on|permanent|implicit|status|paid|missing|required)\s+filters?\b|\b(needs?|lacks?|no|without)\b[^\n]{0,20}\bfilters?\b|\bfilters?\b[^\n]{0,60}\b(test|internal|fraud|cancel\w*|unpaid|paid|credit|refund\w*|void\w*|none known)\b|\bexclud\w*[^\n]{0,40}\b(test|internal|cancel\w*|credit|refund\w*|unpaid|void\w*|fraud)\b|\b(time ?zones?|nulls|null (values?|handling|amounts?)|refresh lag|credit notes?|refunds?)\b'
flags: i
---
