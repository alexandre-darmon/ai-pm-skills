---
type: regex  # real pilot cases brought in to replace synthetic ones, with a target share or a date for the switch
pattern: '\b(retir|replac|phas|swap|drop)\w*( out)?[^\n]{0,60}\bsynthetic\b[^\n]{0,120}\b(date|deadline|by (the )?(end of )?\w+ \d|target|by (week|month|quarter)|\bQ[1-4]\b|\d+\s?%)|\b(target|date|deadline)\b[^\n]{0,100}\b(retir|replac|phas(e|ing) out|swap)\w*[^\n]{0,40}\bsynthetic\b'
flags: i
---
