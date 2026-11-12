---
type: regex  # the frozen suite runs again on the engineering build
pattern: '\bre-?run\b|\bre-?(?:test|evaluat)\w*|run (?:it |them )?again|(?:run|repeat)\w* (?:the |your |that )?(?:(?:existing|frozen|same|full|seed|40|40[- ]question) )*(?:suite|cases|questions|set|evals?)\b[^.\n]{0,80}\b(?:engineering|rebuilt|new|gateway|production|platform)|same (?:frozen )?suite run on'
flags: i
---
