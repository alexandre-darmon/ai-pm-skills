---
type: regex  # red line: 0.08 EUR per conversation is not a cost per outcome
pattern: '(÷|/|divided by|\bover\b)\s*\(?\s*(the |all |total |monthly |number of |count of |# ?|n_)*((volume|conversations?|sessions?|requests?|\d[\d.,]*)\s*(×|x|\*|·)\s*\(?(quality|resolution[ _]rate|success[ _]rate|% ?correct|share correct|accuracy|q\b|0?[.,]\d+|\d{1,3}([.,]\d+)? ?%)|(successful|correct(ly)?|resolved|success(es)?)(?![a-z]))'
flags: i
weight: 2
---
