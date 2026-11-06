---
type: regex  # covers what happens when employees type sensitive content into the tool
pattern: '(sensitive|health(?! and safety)|harass|dispute|grievance|santé(?! et)|harcèlement|litige)[^\n]{0,80}\b(typed?|typing|enter(ed|s|ing)?|paste[ds]?|saisi\w*)\b|\b((employees?|handlers?|users?|staff|people|they) types?|typed|typing|enter(ed|s|ing)?|paste[ds]?|saisi\w*)\b[^\n]{0,80}(sensitive|health(?! and safety)|harass|dispute|grievance|santé(?! et)|harcèlement|litige)|\bprompts?\b[^\n]{0,60}(sensitive|health(?! and safety)|harass|dispute|grievance)'
flags: i
---
