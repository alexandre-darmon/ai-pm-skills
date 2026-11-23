---
type: regex  # faithfulness checked claim by claim with a strict rule for the costly claims: on deadlines, fees or amounts one unsupported claim fails the answer
pattern: '\b(one|a single|any|1) (unsupported|unbacked|invented|ungrounded|wrong) (claim|statement|deadline|fee|amount|figure)s?\b[^.!?\n]{0,40}\b(fails?|failing|counts as (a )?(fail\w*|wrong)|makes the (whole )?answer (fail|wrong))|\b(fails?|failing) the (whole )?(answer|case)\b[^.!?\n]{0,60}\b(one|a single|any) unsupported'
flags: i
---
