---
type: regex  # red line: synthetic cases come with a stated share or a flag
pattern: 'synthetic[^\n]{0,120}(share|ratio|proportion|\d+ ?%|flagged|provisional)|(share|proportion|\d+ ?%|provisional)[^\n]{0,120}synthetic'
flags: i
weight: 3
---
