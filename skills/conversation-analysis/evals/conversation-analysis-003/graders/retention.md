---
type: regex  # how long masked text and classifier logs are kept
pattern: '\bretention\b[^\n]{0,80}(masked|logs?|text|transcripts?|outputs?|days|months|period)|(masked|logs?|transcripts?)[^\n]{0,80}\bretention\b|storage limitation|art(icle|\.)? ?5\(1\)\(e\)|(masked (text|data|conversations|transcripts)|logs?)[^\n]{0,60}(kept|stored|deleted|purged)[^\n]{0,40}(\d+ ?(days?|months?|years?)|period)|how long[^\n]{0,60}(kept|stored|keep|store)'
flags: i
---
