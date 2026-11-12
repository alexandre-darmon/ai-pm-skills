---
type: regex  # red line: at L1 no one-click path from the raw draft to the CRM; restating or rejecting Product's request is fine
pattern: '(?<!\b(?:not|never|no|don[’'']t|do not|cannot|without|request\w*|asks?|asked|wants?|wanted|propos\w*|suggest\w*|idea)\b[^\n.]{0,40})\b(add|keep|include|show)\b[^\n.]{0,20}\bsend to CRM\b[^\n.]{0,20}\b(on|directly|right)\b(?![^\n.]{0,80}\b(would|skips?|breaks?|bypass\w*|violat\w*|defeats?|rejected)\b)'
flags: i
match: not_contains
weight: 5
---
