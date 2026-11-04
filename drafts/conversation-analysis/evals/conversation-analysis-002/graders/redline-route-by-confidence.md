---
type: regex  # red line: neither model alone; route by confidence
pattern: '(?<!(n[''’]t|not|never) )rout\w* (by|on) confidence|confidence threshold|threshold (on|for|of) (the |its )?confidence|confidence\s*(≥|>=|>|<|≤)\s*0?[.,]\d|confidence[^\n]{0,80}\b(above|below|under|exceeds?)\b|\b(above|below|under|over) (a|the|its|that|this|your) (\w+ )?threshold|(?<!(n[''’]t|not|never|bother with|skip|avoid|without) )confidence[- ]based (rout|cascad)'
flags: i
weight: 2
---
