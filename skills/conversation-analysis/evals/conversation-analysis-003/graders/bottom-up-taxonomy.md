---
type: regex  # with no real draft, classes are derived from a larger masked sample, not from the three examples
pattern: '(sample|\b\d{2,4}\b[^\n]{0,30}conversations)[^\n]{0,160}\b(free[- ](form|text)|open[- ]cod\w*|cluster\w*|affinity)\b|\b(free[- ](form|text)|open[- ]cod\w*|cluster\w*|affinity)\b[^\n]{0,160}(sample|conversations|notes)'
flags: i
---
