---
type: regex
pattern: '\b(uptime|availability|200 OK|healthy)\b[^\n]{0,100}\b(wrong|incorrect|quality|accuracy|silent\w*|not enough|miss\w*)\b|\bsilent(ly)?\b[^\n]{0,60}\b(wrong|fail\w*|errors?|misrout\w*|degrad\w*)\b|\b(alerts?|alarms?)\b[^\n]{0,60}\b(accuracy|override|overturn\w*|quality|fallback rate|correction rate|misrout\w*)\b|\b(accuracy|override|overturn\w*|quality|fallback rate|correction rate|misrout\w*)\b[^\n]{0,60}\b(alerts?|alarms?)\b'
flags: i
---
