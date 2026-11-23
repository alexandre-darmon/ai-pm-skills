---
type: regex  # "constraints kept" is a conversation outcome with its own bar, the strictest of the gate (a dropped "no equities" or liquidity floor is a suitability issue), not only a metric reported
pattern: '\bconstraints?\b[^\n]{0,150}\b(strictest|tightest|highest) (bar|threshold|target|gate)|\b(strictest|tightest|highest) (bar|threshold|target)\b[^\n]{0,60}\bconstraints?\b|\bconstraints?\b[^\n]{0,150}\b(carry|get|gets|has|have|deserve) the (strictest|tightest|highest)\b|\bstrictest\b[^\n]{0,40}\bconstraints?\b|\bconstraints?\b[^\n]{0,80}\b(zero[- ]tolerance|(bar|threshold|target|gate) (of|at) 100 ?%)|\bzero[- ]tolerance\b[^\n]{0,60}\bconstraints?\b'
flags: i
---
