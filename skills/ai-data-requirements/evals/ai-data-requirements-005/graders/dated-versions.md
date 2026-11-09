---
type: regex
pattern: '\b(previous|prior|earlier|old(er)?|past|superseded|replaced|last year\S*|historical)\b[^\n.]{0,80}\b(versions?|polic\w+|rules?|editions?)\b[^\n.]{0,120}\b((?<!\b(not|never|no longer)( be)? )retrievable|(stays?|remains?) searchable|questions? (about|on|for|from|covering)|(for|to|in) (that|its|their|the earlier|the relevant) (period|year|date))\b|\beffective[- ]dat\w+ ranges?\b|\beffective[- ]from\b[^\n.]{0,40}\beffective[- ](to|until)\b|\bversions?\b[^\n.]{0,40}\bvalidity (period|range|window)\b'
flags: i
---
