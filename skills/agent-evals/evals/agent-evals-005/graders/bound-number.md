---
type: regex  # the attack-success bound (about 2.5% for 0 of 120) is read against the attacks expected a month, not all 5,000 emails
pattern: '\b(attacks?|attack (emails?|attempts?)|malicious (emails?|messages?)|injection (attempts?|emails?)|injected emails?|hostile emails?)\b[^\n|.]{0,40}\b(a|per|each|every) month\b|\b(a|per|each) month\b[^\n|.]{0,20}\b(attacks?|attack emails?|malicious emails?|injection attempts?)\b'
flags: i
---
