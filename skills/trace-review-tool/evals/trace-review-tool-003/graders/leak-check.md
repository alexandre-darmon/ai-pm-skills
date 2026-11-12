---
type: regex  # checks masking by hand for leaks
flags: i
---
(residual|leak)\w*[^\n]{0,60}(check|rate|sample|review|test)|(check|read|inspect|review|test)\w*[^\n]{0,60}(leak|residual)
