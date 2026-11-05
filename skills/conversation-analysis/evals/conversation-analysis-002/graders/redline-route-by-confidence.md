---
type: regex  # red line: neither model alone; route by confidence
pattern: '(?<!(n[''’]t|not|never) )rout\w* (by|on) confidence|confidence threshold|threshold (on|for|of) (the |its )?confidence|confidence\s*(≥|>=|>|<|≤)\s*0?[.,]\d|confidence[^\n]{0,80}\b(above|below|under|exceeds?)\b|\b(above|below|under|over) (a|the|its|that|this|your) (\w+ )?threshold|(?<!(n[''’]t|not|never|bother with|skip|avoid|without) )confidence[- ]based (rout|cascad)|(?<!(n[''’]t|not|never|bother with|skip|avoid|without) )\brout\w*[^\n]{0,30}\bby confidence|(?<!(n[''’]t|not|never|bother with|skip|avoid|without) )\bconfidence[- ]routing\b|\b(keep|use)s?\b[^\n]{0,60}\bonly when (its )?confidence is (high|above)|confidence is (high|low)[^\n]{0,80}\b(send|route|escalat\w*|hand)\b[^\n]{0,40}(frontier|human|review)'
flags: i
weight: 2
---
