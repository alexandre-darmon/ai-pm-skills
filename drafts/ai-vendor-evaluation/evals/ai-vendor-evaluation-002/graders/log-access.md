---
type: regex
flags: i
---
(access|right)[^\n]{0,60}\b(logs?|traces?)\b|\b(logs?|traces?)\b[^\n]{0,60}\baccess|audit (and|&) access|right to audit|(access|audit|inspection)[, ]+(inspection|audit)( and audit)? rights?
