---
type: regex  # red line: cost per outcome divides by successes, never by all conversations
pattern: '(÷|/|divided by|\bover\b)\s*\(?\s*(the |all |total |monthly |number of |count of |# ?|n_)*((volume|conversations?|sessions?|requests?|\d[\d.,]*)\s*(×|x|\*|·)\s*\(?(quality|resolution[ _]rate|success[ _]rate|% ?(correct|resolved)|share (of )?(\w+ )?(correct|resolved|success)|(correct|resolved)[\w -]{0,24} (rate|share)|accuracy|q\b|0?[.,]\d+|\d{1,3}([.,]\d+)? ?%)|(successful|correct(ly)?|resolved|success(es)?)(?![a-z]))'
flags: i
weight: 2
---
