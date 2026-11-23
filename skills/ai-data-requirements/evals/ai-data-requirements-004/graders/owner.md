---
type: regex  # an owner column is generic; the skill makes the owner act: past expiry the owner re-certifies the source or it leaves the index
pattern: '\bowners?\b[^\n.]{0,30}\bre-?(certif|validat|approv|confirm|review)\w*|\bre-?certif\w*[^\n.]{0,60}\b(or|else|otherwise)\b[^\n.]{0,30}\b(leaves?|removed?|drop\w*|out of|de-?index\w*)\b|\b(past|after|beyond|at) (its |the |their )?expiry\b[^\n.]{0,60}\b(leaves?|removed?|drop\w*|de-?index\w*|re-?certif\w*)'
flags: i
---
