---
type: regex
pattern: '\b(csv|real (data|complaints?)|client data|customer data|pii|export)\b[^\n]{0,120}\b(CI|pre-commit|hooks?|deny rules?|permission rules?|sandbox\w*|access controls?|scan\w*)\b|\b(CI|pre-commit|hooks?|deny rules?|permission rules?|sandbox\w*|access controls?|scan\w*)\b[^\n]{0,120}\b(csv|real (data|complaints?)|client data|customer data|pii|export)\b'
flags: i
---
