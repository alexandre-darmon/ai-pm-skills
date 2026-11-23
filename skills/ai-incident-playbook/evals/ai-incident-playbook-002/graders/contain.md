---
type: regex  # containment by slice: one part stops, the rest keeps running, or a level drop from and to
pattern: '\bslices?\b|\b(?:keep\w*|leav\w*|stay\w*|remain\w*|continu\w*)\b[^.\n]{0,60}\b(?:running|live|online|available|in service)\b|\bL[0-5]\b[^.\n]{0,10}\bto L[0-5]\b'
flags: i
---
