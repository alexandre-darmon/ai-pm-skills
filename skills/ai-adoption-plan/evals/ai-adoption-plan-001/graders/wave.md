---
type: regex  # waves are gated: a wave opens when the previous one meets its outcome targets, not on a calendar date
pattern: '\bwaves?\b[^.!?\n]{0,60}\b(opens?|starts?|begins?|proceeds?|unlocks?|goes live)\b[^.!?\n]{0,40}\b(on|when|once|only (if|when|after)|after)\b[^.!?\n]{0,60}\b(targets?|results?|thresholds?|criteria|gates?|pass mark)|\bnot on a (calendar )?date\b|\bon (results|outcomes|targets),? not (on )?(a |the )?(calendar|date)'
flags: i
---
