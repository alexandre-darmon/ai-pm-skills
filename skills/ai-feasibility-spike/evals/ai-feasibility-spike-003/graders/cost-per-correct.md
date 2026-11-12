---
type: regex  # 4.20 EUR over 100 correct routings, not over 110 chats; 0.04 fails on purpose (too rounded to tell from 0.038 per chat)
pattern: '\b0[.,]042\b|\b4[.,]2 ?(cents?|ct|euro ?cents?)\b|4[.,]20? ?(EUR|€)? ?(/|÷|divided by|over) ?100\b'
flags: i
---
