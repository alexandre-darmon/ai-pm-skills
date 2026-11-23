---
type: regex  # owner-or-out: the ownerless table is excluded or blocked until an owner is named, not just flagged as a risk
pattern: '\b(no (named )?owner|unowned|ownerless|without an? (named )?owner)\b[^\n]{0,60}\b(out|exclud\w*|blocker|blocked)\b|\b(is out|are out|(stays?|kept|left|remains?) out|exclud\w*|blocked)\b[^\n]{0,20}\b(until|pending|unless)\b|\buntil\b[^\n]{0,40}\bowner\b[^\n]{0,40}\b(out|exclud\w*|blocked|not used)\b'
flags: i
---
