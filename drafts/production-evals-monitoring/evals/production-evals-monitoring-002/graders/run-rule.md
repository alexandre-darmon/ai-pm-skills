---
type: regex  # the run rule: several periods in a row on one side
pattern: '\b(consecutive|in a row|run of|successive|straight)\b[^\n]{0,60}\b(weeks?|periods?|points?|samples?|readings?)\b|\b(weeks?|periods?|points?|readings?)\b[^\n]{0,30}\b(in a row|consecutive(ly)?|running)\b|run rule'
flags: i
---
