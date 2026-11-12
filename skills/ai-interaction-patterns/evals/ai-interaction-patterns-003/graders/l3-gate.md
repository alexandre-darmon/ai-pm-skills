---
type: regex  # the ladder's L3 gate is a measured fact (shadow run, tested escalation path), not an acceptance rate
pattern: 'shadow[- ]?(run|mode|period|test|phase)|run\w* (it |the tool |the assistant )?in shadow|escalation path[^.\n]{0,30}\btest(ed)?\b|\btest(ed|ing)? (the )?escalation path'
flags: i
---
