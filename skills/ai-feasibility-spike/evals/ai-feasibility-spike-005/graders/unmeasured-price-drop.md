---
type: regex  # a future price drop is a hypothesis to test, not a result
pattern: '(price|cost|model)[^\n.]{0,80}\b(hypothes\w+|assumption|unmeasured|not (yet )?(a )?(measured|result|evidence)|speculat\w*|cannot (be )?count\w*|can.t count|test (it )?in (a|the) (new|next) spike)|(hypothes\w+|assumption|not (a )?(result|measured))[^\n.]{0,60}(price|cheaper|next (model|generation))'
flags: i
---
