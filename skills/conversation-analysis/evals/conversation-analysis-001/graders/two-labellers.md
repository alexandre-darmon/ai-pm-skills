---
type: regex  # two labellers on a shared subset, and their agreement read as the ceiling a classifier can reach, not only as label reliability
pattern: '(?:^|\n)(?=[^\n]*\b(both|two|second|same|shared|overlap\w*|double[- ]label\w*)\b)(?=[^\n]*\b(agreement|kappa|agree)\b)(?=[^\n]*(\b(ceiling|upper bound|upper limit)\b|\b(classifier|model|automat\w*)\b[^\n]{0,40}\b(can(no|[''’])?t|won[''’]t|will not|unlikely to) (beat|exceed|do better|reach higher|outperform)))'
flags: i
---
