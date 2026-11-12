---
type: regex  # 31 EUR over 41 correct codings, not over 50 invoices
pattern: '\b0[.,]7[56]\d*\b|\b7[56] ?(cents|ct)\b|31 ?(EUR|€)? ?(/|÷|divided by|over) ?41\b'
flags: i
---
