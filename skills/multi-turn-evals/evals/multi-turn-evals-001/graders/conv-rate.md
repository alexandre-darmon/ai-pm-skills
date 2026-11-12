---
type: regex  # turns 24 of 120 into the conversation failure rate
pattern: '\b20 ?%|\b80 ?%[^\n]{0,60}(conversations?|clean|pass)|one in five|1 in 5|0[.,]20?\b[^\n]{0,20}(conversation|fail)'
flags: i
---
