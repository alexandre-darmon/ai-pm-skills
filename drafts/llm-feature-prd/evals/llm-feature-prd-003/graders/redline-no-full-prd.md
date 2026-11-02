---
type: regex  # red line: no full PRD (numbered or bold section headings count too)
pattern: '^(#{1,3} *|\*\*)(\d+\.? *)?(Failure (paths|modes)|Rollout|Launch plan)'
flags: im
match: not_contains
weight: 5
---
