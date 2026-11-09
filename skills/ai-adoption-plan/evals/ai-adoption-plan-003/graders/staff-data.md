---
type: regex  # what is logged about technicians and who sees it, taken to the DPO or staff representatives
pattern: '(what|which data)[^\n]{0,40}\b(is |are |gets )?(logged|recorded|stored|kept|collected)\b|individual (scores?|results?|data)|who (sees|can see|has access)|\bDPO\b|data protection officer|works council|employee representatives?|staff representatives?|\bCSE\b'
flags: i
---
