---
type: regex  # logs guardrail hits
flags: i
---
guardrail[^\n]{0,40}(hit|trigger|fire|block|event|flag|outcome|result)
