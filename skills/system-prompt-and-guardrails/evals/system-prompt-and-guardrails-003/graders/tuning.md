---
type: regex  # tuning comes before go-live (tune, re-run, then launch), not a launch now in shadow mode with tuning later
pattern: '\b(?:tun\w*|recalibrat\w*)\b[^.\n]{0,40}\b(?:and|then)\b[^.\n]{0,30}\bre-?(?:run|test)\w*\b[^.\n]{0,20}\b(?:first|before)\b|\b(?:tun\w*|recalibrat\w*)\b[^.\n]{0,80}\bbefore\b[^.\n]{0,40}\b(?:go(?:ing)?[- ]live|launch\w*|ship\w*|release)\b|\b(?:no|not|don.t|do not)\b[^.\n]{0,20}\b(?:go[- ]live|launch|ship)\w*\b[^.\n]{0,40}\buntil\b[^.\n]{0,60}\b(?:tun\w*|recalibrat\w*|re-?run)'
flags: i
---
