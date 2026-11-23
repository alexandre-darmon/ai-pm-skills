---
type: regex  # the entry covers the whole version bundle: model snapshot, parameters, tools, knowledge base stated or flagged unconfirmed, not only the prompt
pattern: '\bsnapshot\b|version bundle|\b(model|model version|parameters|tools|knowledge base)\b[^\n]{0,80}\b(unchanged|did not change|didn[’'']t change|not (stated|confirmed) as changed|not stated|unconfirmed)'
flags: i
---
