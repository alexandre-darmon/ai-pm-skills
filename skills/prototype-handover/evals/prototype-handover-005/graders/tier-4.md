---
type: regex  # the wanted autonomous level on pricing is tier 4
pattern: '\btier (?:4|four)\b|\btier\b[^\n.|]{0,20}?[:(|]\s*(?:4|four)\b|mission[- ]critical'
flags: i
---
