---
type: regex
pattern: '^(?=.*(?:\||\baccount|\bemail|\bsender|\btransaction))(?=.*\b(?:logs?|logging|traces?)\b)(?=.*\b(?:evals?|evaluation|test set|golden set)\b)(?=.*\b(?:train\w*|fine-tun\w*)\b)(?=.*\b(?:vendors?|providers?|processors?|third part\w*)\b)|^(?=(?:[^\n]*\n){0,8}?[\s|*-]*(?:[\w-]+ ){0,2}(?:logs?|logging|traces?)\b)(?=(?:[^\n]*\n){0,8}?[\s|*-]*(?:[\w-]+ ){0,2}(?:evals?|evaluation|test set|golden set)\b)(?=(?:[^\n]*\n){0,8}?[\s|*-]*(?:[\w-]+ ){0,2}(?:train\w*|fine-tun\w*)\b)(?=(?:[^\n]*\n){0,8}?[\s|*-]*(?:[\w-]+ ){0,2}(?:vendors?|providers?|processors?|third part\w*)\b)'
flags: im
---
