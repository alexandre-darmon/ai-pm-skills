---
type: regex  # red line: no consultation duty is invented below 11 employees
pattern: '(?<!(?:\b(?:not|never|nor|if|when|once|from|after|until|will|would)\b|n[''’]t\b)[^\n.;:!?]{0,60})(?<!\bno\s(?:[\w-]+\s){0,2})(?<!\b(?:50|fifty|cinquante)\b[^\n]{0,80})(\b(must|need to|have to|required to|obliged to) (still )?(inform and )?consult(ing)?\b(?![^\n.;]{0,150}\b((starts?|appl(y|ies)|begins?|kicks? in)\b[^\n.;]{0,30}\b(50|fifty)\b|(only )?from 50\b))[^\n.;]{0,50}\b(CSE|employees|staff|team|representatives|workforce|staff delegates)\b|\binformation[- ]consultation (meeting|procedure|process)\b)|(?<!(?:\b(?:ne|pas|jamais|si|sans)\b|\bn[''’])[^\n.;:!?]{0,40})\b(devez|doivent|il faut)\b[^\n.;]{0,40}\bconsulter\b[^\n.;]{0,30}\b(le CSE|les salariés|le personnel)'
flags: i
match: not_contains
weight: 3
---
