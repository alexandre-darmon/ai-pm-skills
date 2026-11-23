---
type: regex  # the restart decision is taken with IT risk (IT risk's call), not a written extension by the sponsor alone
pattern: '\bdecision\b[^.\n]{0,40}\b(?:with|by|from|of|for)\b[^.\n]{0,15}\b(?:IT|ICT|operational) risk\b|\b(?:IT|ICT|operational) risk(?:[''’]s)?\b[^.\n]{0,30}\b(?:decides?|decision|call|to decide)\b|\b(?:decides?|decision|call)\b[^.\n]{0,30}\bfor (?:the )?(?:IT|ICT|operational) risk\b|\b(?:IT|ICT) risk function\b[^.\n]{0,30}\bdecid'
flags: i
---
