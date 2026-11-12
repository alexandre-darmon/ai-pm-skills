---
type: regex  # the real suite is drawn from production traffic, not written by the team
pattern: '(sampl\w*|drawn|taken|pulled|selected)[^\n.]{0,50}(production|live|real|actual|incoming)[^\n.]{0,25}(traffic|complaints|volumes?|flows?|cases|data)|\breal complaints\b|from (production|live) traffic'
flags: i
---
