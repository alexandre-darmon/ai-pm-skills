---
type: regex  # an alarm on an AI quality signal, not uptime alone (also a heading line followed by its first bullet)
pattern: '\b(uptime|availability|200 OK|healthy)\b[^\n]{0,100}\b(wrong|incorrect|quality|accuracy|silent\w*|not enough|miss\w*)\b|\bsilent(ly)?\b[^\n]{0,60}\b(wrong|fail\w*|errors?|misrout\w*|degrad\w*)\b|\b(alerts?|alarms?)\b[^\n]{0,60}\b(accuracy|override|overturn\w*|quality|fallback rate|correction rate|misrout\w*)\b|\b(accuracy|override|overturn\w*|quality|fallback rate|correction rate|misrout\w*)\b[^\n]{0,60}\b(alerts?|alarms?)\b|\b(alerts?|alarms?)\b[^\n]{0,60}:\s*\n\s*([-*]|\d+\.)\s[^\n]{0,80}\b(accuracy|override|overturn\w*|quality|error rate|correction rate|misrout\w*)\b|\b(is|looks|stays|can be|remains)\s+(up|green|healthy|running)\b[^\n]{0,40}\b(while|but|yet)\b[^\n]{0,40}\b(wrong|incorrect|bad|misrout\w*)\b'
flags: i
---
