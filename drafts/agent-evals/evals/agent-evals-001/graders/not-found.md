---
type: regex  # forbidden: refund on an order the lookup did not find
pattern: 'not[- ]found|(missing|unknown|non-?existent|invalid|wrong) order|order[^\n.]{0,30}(does not|doesn.t) exist|(empty|no) (result|match)|lookup[^\n.]{0,40}(fails?|failed|empty|returns nothing)'
flags: i
---
