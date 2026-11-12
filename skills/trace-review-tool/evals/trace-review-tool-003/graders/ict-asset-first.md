---
type: regex  # the app is identified as an ICT asset before it loads production-derived data
flags: i
---
(identif|regist|record|document|approv|declar|inventor)\w*[^\n]{0,80}(ICT asset|EUC|end[- ]user computing)|(ICT asset|EUC|end[- ]user computing)[^\n]{0,120}(before|first|prior)|(before|first|prior)[^\n]{0,80}(ICT asset|EUC|end[- ]user computing)
