---
type: regex  # performance data collected from deployers (art. 72(2), 26(5))
pattern: 'deployers?\b[^\n]{0,120}\b(data|feedback|reports?|logs?|shar\w*|send\w*|provid\w*|collect\w*|inform\w*|feed)\b|\b(data|feedback|logs?|reports?)\b[^\n]{0,60}\bfrom (the |your |each |our )?deployers?'
flags: i
---
