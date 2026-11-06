---
type: regex  # the run is graded on what it did: the resulting state, and actions that must never occur
pattern: '^(?=[\s\S]*(end[- ]state|final state|outcome state|resulting state|(system|ledger|database|db|payment)[- ](state|record)|state of the (system|order|ledger|database|refund)|what actually (happened|changed)|actually (issued|executed|went through|happened)|refund[^\n.]{0,30}(really |actually )?exists|(check|verify|assert|confirm)[^\n.]{0,50}(ledger|database|payment system|refund record)))(?=[\s\S]*(forbidden|prohibited|disallowed|must never|never (allowed|acceptable|issue|call|refund)|\b(skip\w*|bypass\w*|without|no)\b[^\n.]{0,40}(approval|sign-off|manager)|(approval|sign-off)[^\n.]{0,30}(skipp|bypass|missing)))'
flags: i
---
