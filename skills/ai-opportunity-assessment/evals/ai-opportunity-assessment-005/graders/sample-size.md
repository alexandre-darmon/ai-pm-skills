---
type: regex  # the evidence plan says on how many sampled answers quality is read
pattern: '\b(sampl\w*|label+ed|grad\w*|review\w*|test\w*|eval\w*|check\w*)\b[^\n]{0,40}\b\d{2,4}\s+(?:[\w-]+\s+){0,2}?(questions|cases|answers|conversations)\b|\b\d{2,4}\s+(?:[\w-]+\s+){0,2}?(questions|cases|answers|conversations)\b[^\n]{0,60}\b(sampl\w*|label+ed|graded|reviewed|per (class|topic|category|domain))\b'
flags: i
---
