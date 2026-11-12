---
type: regex  # expert review re-measures the judge in production
pattern: '\bTPR\b|\bTNR\b|true (positive|negative) rate|sensitivity[^\n]{0,40}specificity|(judge|evaluator)\w*[^\n]{0,100}(drift|re-?calibrat|re-?validat|re-?check|re-?measur|re-?test)|(re-?calibrat|re-?validat|re-?measur|re-?check)\w*[^\n]{0,60}(judge|evaluator)'
flags: i
---
