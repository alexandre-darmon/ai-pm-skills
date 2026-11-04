---
type: regex
pattern: 'cost per (correct|successful|resolved|right|accurate) (outcome|answer|request|conversation|resolution|claim|ticket)s?\b[^\n]{0,60}(÷|/|divided by|\bover\b)\s*\(?\s*(the |all |total |monthly |number of |count of |# ?|n_)*((volume|conversations?|sessions?|requests?|\d[\d.,]*)\s*(×|x|\*|·)\s*\(?(quality|resolution[ _]rate|success[ _]rate|% ?correct|share correct|accuracy|q\b|0?[.,]\d+|\d{1,3}([.,]\d+)? ?%)|(successful|correct(ly)?|resolved|success(es)?)(?![a-z]))'
flags: i
---
