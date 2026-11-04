---
type: regex  # each KB action has an owner
pattern: '(?<!\bno )owner[^\n]{0,60}\b(KB|knowledge base|base)s?\b|\b(KB|knowledge base)s?\b[^\n]{0,60}owner|\|\s*(KB )?owner\s*\||\|\s*base\s*\|\s*owner'
flags: i
---
