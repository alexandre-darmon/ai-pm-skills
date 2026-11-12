---
type: regex  # a worst-first queue over-counts failures
flags: i
---
(targeted|thumbs[- ]down|worst|negative)[^\n]{0,160}(over[- ]?(represent|count|state|weight)|bias|inflat|skew|not (a |the )?(rate|representative)|overstat|unrepresentative)|(bias|skew|inflat|overstat|over[- ]?represent)\w*[^\n]{0,100}(thumbs[- ]down|worst|targeted)
