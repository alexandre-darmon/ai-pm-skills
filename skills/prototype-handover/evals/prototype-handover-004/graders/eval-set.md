---
type: regex  # a small eval set before sharing
pattern: 'eval(?:uation)? (?:suite|set|cases)|test (?:set|cases)|golden set|light evals?\b|(?:set|handful|dozen|\d+(?: to \d+)?)\s+(?:of\s+)?(?:saved|reference|reviewed|past)\s+(?:inputs?|reports|examples|cases|summaries)[^\n]{0,120}\b(?:baseline|score[sd]?|compare|regress\w*|re-?run|worse|benchmark)\b|\bbaseline\b[^\n]{0,80}\b(?:set|handful|dozen|\d+(?: to \d+)?)\s+(?:of\s+)?(?:saved|reference|reviewed|past)\s+(?:inputs?|reports|examples|cases|summaries)|\b\d+ (?:test )?cases\b'
flags: i
---
