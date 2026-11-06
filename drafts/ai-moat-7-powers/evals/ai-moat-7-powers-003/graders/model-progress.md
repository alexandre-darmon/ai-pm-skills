---
type: regex
pattern: '(?<!\b(?:rivals?|competitors?|anyone)\b[^\n.]{0,40})\b(model|platform|vendor|provider|lab|API)s?\b[^\n.]{0,80}\b(absorb\w*|ship\w*|releas\w*|add|adds|added|adding|bundl\w*)\b[^\n]{0,120}(assum\w*|\b20\d\d\b|\bQ[1-4]\b|\b\d+ (months?|quarters?)\b)|(assum\w*|\b20\d\d\b|\bQ[1-4]\b|\b\d+ (months?|quarters?)\b)[^\n]{0,120}(?<!\b(?:rivals?|competitors?|anyone)\b[^\n.]{0,40})\b(model|platform|vendor|provider|lab|API)s?\b[^\n.]{0,80}\b(absorb\w*|ship\w*|releas\w*|add|adds|added|adding|bundl\w*)\b|\b(model|platform|vendor|provider|lab)s?\b[^\n.]{0,60}\b(already|has|have) (shipped|released|added)'
flags: i
---
