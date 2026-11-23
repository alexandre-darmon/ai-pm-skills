---
type: regex  # the entry's approval field is filled honestly: approver not recorded / to be provided, never invented
pattern: '\b(approv\w*|sign(ed)?[- ]?off)( by)?\b[^\n]{0,40}\b(not recorded|not known|unknown|missing|none recorded|not documented|not on file|not named|not given|to be (provided|confirmed|filled)|TBD|TBC)'
flags: i
---
