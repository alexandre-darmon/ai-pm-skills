---
type: regex  # binary is tied to each failure mode (a pass/fail definition or judge per mode), not a binary question in general
pattern: '\bfailure (modes?|types?|categor\w*)\b[^\n.]{0,40}\b(pass/fail|pass[- ]or[- ]fail|yes/no|binary)\b|\b(pass/fail|pass[- ]or[- ]fail|yes/no|binary)\b[^\n.]{0,30}\bper (failure )?(modes?|types?|categor\w*)\b|\bbinary failure (modes?|types?|categor\w*)\b|\b(each|every) (failure )?(mode|type|categor\w*)\b[^\n.]{0,30}\b(pass/fail|pass[- ]or[- ]fail|yes/no|binary)\b'
flags: i
---
