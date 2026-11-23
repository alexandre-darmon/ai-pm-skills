---
type: regex  # which way it leans, by shares of traffic (about 7% good memos wrongly failed vs about 2% bad ones passed), not by error rates
pattern: '(?<![\d.,])[67]([.,]\d+)? ?(%|points?)(?![\d])[^\n]{0,100}?(?<![\d.,])[12]([.,]\d+)? ?(%|points?)(?![\d])'
flags: i
---
