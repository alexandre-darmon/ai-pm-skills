---
type: regex  # the stop rule is operational: a minimum volume before the reopen rate counts, or who restarts and after what, not a TODO
pattern: '\b(at least|minimum|min\.?|once there are|fewer than|below)\b[^\n]{0,60}?\b\d{2,4}\s+(closures|tickets|closed tickets)\b|\b\d{2,4}\s+(closures|tickets)\b[^\n]{0,20}\b(in|within) the (window|period)\b|\b(restart|resum\w*|re-?enabl\w*)\b[^\n]{0,60}\b(manager|owner|lead)\b[^\n]{0,40}\bafter\b'
flags: i
---
