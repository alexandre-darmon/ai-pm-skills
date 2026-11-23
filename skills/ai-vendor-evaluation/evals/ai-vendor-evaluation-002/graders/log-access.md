---
type: regex
flags: i
---
\b(logs?|traces?)\b[^\n|]{0,100}(model[- ]versions?|timestamps?|versions? (used|of the model))|per[- ](request|call|query|email) (logs?|traces?)
