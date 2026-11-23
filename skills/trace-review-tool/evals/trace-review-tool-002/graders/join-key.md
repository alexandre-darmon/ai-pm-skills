---
type: regex  # a key that joins each trace to the loan outcome (decision, default), not just an application id
flags: i
---
(loan|application|case|credit|decision)[ _-]?(id|identifier|number|reference)\b[^\n]{0,120}(outcome|default|repaid|repayment|arrears|approv|declin|final decision)|join[ _-]?key[^\n]{0,100}(outcome|default|repay|approv|declin|decision)|(outcome|default|repayment|arrears)[^\n]{0,60}\b(join|link)
