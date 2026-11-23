---
type: regex
pattern: 'atomic\w*[^\n|]{0,40}\bcaps?\b|\bcaps?\b[^\n|]{0,40}\batomic|\bcaps?\b[^\n|]{0,100}(same transaction|in one transaction|parallel runs?|concurrent (runs|calls|sessions))|(system of record|ledger)[^\n|]{0,60}\bcaps?\b[^\n|]{0,60}(transaction|atomic)'
flags: i
---
