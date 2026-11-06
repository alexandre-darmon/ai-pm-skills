---
type: regex
pattern: '\b(autonomy|fallback)\b[^\n]{0,120}([\w/-]+\.md\b|\b(not (stated|specified|given|defined|provided|covered|in the prd)|unresolved|tbc|to be confirmed|unstated|excluded|absent)\b)|\bautonomy\b[^\n]{0,120}\b(missing|open)\b|\b(missing|open)\b[^\n]{0,120}\bautonomy\b|\b(unresolved|tbc|to be confirmed|unstated|absent)\b[^\n]{0,120}\b(autonomy|fallback)\b'
flags: i
---
