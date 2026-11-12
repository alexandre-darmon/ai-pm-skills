---
type: regex  # asks whether review labels and critiques count as logs
flags: i
---
(label|critique|review)\w*[^\n]{0,60}(count|treated|kept|qualif)\w*[^\n]{0,20}(as )?(logs?|records?)|logs?[^\n]{0,40}(include|cover)\w*[^\n]{0,30}(label|critique)
