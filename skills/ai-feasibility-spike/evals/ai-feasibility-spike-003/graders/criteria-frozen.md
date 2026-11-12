---
type: regex  # the moving definition of correct is why the number does not transfer, and it must be frozen
pattern: 'criteria drift|(criteria|definition|rubric|scoring rules)[^\n.]{0,120}\b(froz\w*|freeze|fixed|locked|stable)\b|\b(froz\w*|freeze|lock\w*)[^\n.]{0,40}(criteria|definition|rubric|scoring rules)|\bfix\w*[^\n.]{0,20}(criteria|definition|rubric|scoring rules)[^\n.]{0,80}\bbefore\b|moving (the )?(target|goalposts?)'
flags: i
---
