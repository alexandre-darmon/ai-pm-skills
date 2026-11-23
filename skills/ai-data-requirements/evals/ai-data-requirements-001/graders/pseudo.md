---
type: regex  # a pseudonymisation plan says where the re-identification key or mapping is held, not only that fields are masked
pattern: '\b(key|mapping|lookup table|token vault)\b[^\n|]{0,50}\b(lives?|held|kept|stored|sits?|stays?|resides?)\b|\b(held|kept|stored)\b[^\n|]{0,30}\b(key|mapping)\b'
flags: i
---
