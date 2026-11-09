---
type: regex  # a judge per mode is checked against expert labels before scoring the 5,000
pattern: 'calibrat\w*|\bTPR\b|\bTNR\b|true[- ]positive|sensitivity|specificity|agree\w*[^\n]{0,40}(expert|human)(\x27s)?[- ]?(labels?)'
flags: i
---
