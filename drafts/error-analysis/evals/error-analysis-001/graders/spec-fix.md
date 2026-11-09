---
type: regex  # specification failures are fixed, not evaluated
pattern: 'specification|generali[sz]ation failure|(prompt|instructions?|spec|system prompt)[^\n]{0,60}never (asked|asks|said|says|told|mentions?|required|gave|gives|give|provided|passed)|\bfix\w*\b[^\n]{0,60}\b(cause|failure|problem|error)\b[^\n]{0,20}\bin the (spec|prompt|instructions?|inputs?)\b|fix[^\n]{0,80}(prompt|spec|KB|knowledge base|retrieval)[^\n]{0,80}(no|without|not|before)[^\n]{0,20}(eval|grader|judge|evaluator)'
flags: i
---
