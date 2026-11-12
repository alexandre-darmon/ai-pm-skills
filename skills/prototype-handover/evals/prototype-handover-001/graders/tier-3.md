---
type: regex  # business-critical: complaints and fraud signals touch customer outcomes
pattern: '\btier (?:3|three)\b|\btier\b[^\n.|]{0,20}?[:(|]\s*(?:3|three)\b|business[- ]critical'
flags: i
---
