---
type: regex  # TPR and TNR targets fixed before the re-test, not after
pattern: '(targets?|bars?|thresholds?|cut-?offs?|acceptance criteri\w+)\b[^\n]{0,120}\b(before|ahead of|prior to|in advance|beforehand|up ?front)\b|\b(before|ahead of|prior to)\b[^\n]{0,60}\b(re-?test\w*|test\w*|measur\w*|scor\w*|run\w*|see\w*|look\w*)\b[^\n]{0,80}\b(targets?|bars?|thresholds?)\b'
flags: i
---
