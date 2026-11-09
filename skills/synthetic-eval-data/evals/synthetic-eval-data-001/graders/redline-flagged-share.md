---
type: regex  # red line: synthetic cases flagged, share stated
pattern: 'synthetic[^\n]{0,120}(share|ratio|proportion|\d+ ?%|flag|tagg|marked|origin)|(share|proportion|flag\w*|tagg\w*|marked|origin)[^\n]{0,120}synthetic'
flags: i
weight: 3
---
