---
type: regex  # the cost ceiling is derived from what the 4 handler minutes are worth, in money, or from those minutes times the loaded hourly cost the brief does not give
pattern: '\b(4|four)[- ]?min(ute)?s?\b[^\n]{0,150}(\b(loaded|hourly)\b[^\n]{0,20}\b(cost|rate)|\bcost per hour\b)|\b(loaded|hourly)\b[^\n]{0,40}\bcost\b[^\n]{0,150}\b(4|four)[- ]?min|\d[\d.,]* ?(EUR|€)[^\n]{0,100}\b(4|four)[- ]minutes?|\b(4|four)[- ]minutes?[^\n]{0,100}(\d ?(EUR|€)|(EUR|€) ?\d)|(handler|staff|labou?r)[^\n]{0,40}(cost|rate|time|hour)[^\n]{0,60}(\d ?(EUR|€)|(EUR|€) ?\d)'
flags: i
---
