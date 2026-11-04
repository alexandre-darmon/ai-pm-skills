---
type: regex  # red line: no full PRD; any of its usual sections as a heading (numbered or bold too) counts
pattern: '^(#{1,3} *|\*\*)(\d+(\.\d+)*\.? *)?(Summary|Goals|Non-goals|Users|Personas|Scope|(Functional |Non-functional )?Requirements|Failure (paths|modes)|Rollout|Launch plan|Delivery|Risks)\b'
flags: im
match: not_contains
weight: 5
---
