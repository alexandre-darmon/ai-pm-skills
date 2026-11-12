---
type: regex  # tier 3 at least: credit monitoring touches financial controls and customers
pattern: '\btier (?:[34]|three|four)\b|\btier\b[^\n.|]{0,20}?[:(|]\s*(?:[34]|three|four)\b|business[- ]critical|mission[- ]critical'
flags: i
---
