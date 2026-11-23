---
type: regex  # someone with authority (the sponsor or a governance lead) is the one who names the owner or accepts the loss, not the data team
pattern: '\b(sponsor|steering|governance)\w*\b[^\n.]{0,80}\b(names?|naming|nominat\w*|appoint\w*|assign\w*|decid\w*|accepts?|designat\w*)\b|\b(escalat\w*|decided? by|who decides|decision)\b[^\n.]{0,40}\b(sponsor|steering|governance)'
flags: i
---
