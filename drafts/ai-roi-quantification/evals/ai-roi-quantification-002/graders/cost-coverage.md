---
type: regex
pattern: '(?=[\s\S]*\b(monitoring|eval\w* (upkeep|maintenance)|prompt (and source )?maintenance|exception handling|human review|compliance evidence)\b)[\s\S]*(\b(build[- ](cost|effort|work|phase)|engineering|integration|labell?ing)\b[^\n]{0,100}\b(includ\w+|missing|exclud\w+|confirm\w*|not counted|not (given|stated|provided|known)|unknown)\b|\b(includ\w+|missing|exclud\w+|confirm\w*|not counted|not (given|stated|provided|known)|unknown)\b[^\n]{0,100}\b(build[- ](cost|effort|work|phase)|engineering|integration|labell?ing)\b)'
flags: i
---
