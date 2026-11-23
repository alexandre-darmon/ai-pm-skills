---
type: regex  # owner-or-out: a source with no named owner is a blocker, excluded or escalated, not just a column to fill
pattern: '\bno (named )?owner\b|\bowner\b[^\n.]{0,80}\b(or (it|they)(''re| are| is)? out|(is|are|stays?) out|blocker|blocked|exclud\w*|escalat\w*)|\b(blocker|exclud\w*|escalat\w*)\b[^\n.]{0,60}\b(no|without an?|named|missing) owner'
flags: i
---
