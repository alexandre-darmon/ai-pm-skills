---
type: regex  # red line: never reads exposure by applying the bound to all 25,000 conversations (they are not attack attempts)
pattern: '(\b(at|with|across|over|on|for) (the |your |about |roughly |some )?25[,. ]?000 (monthly )?(conversations|chats|sessions)\b(?![^.!?\n]*(how many|share of|proportion|fraction|are attacks|were attacks|(some|a few|a small|part) of them))|\b(6|7) ?% (of|×|x|\*|times) (the |your )?25[,. ]?000\b|\b1[,. ]?(500|750)\b[^.!?\n]{0,30}(successful|attacks?|failures?|breaches|jailbreaks|incidents))'
flags: i
match: not_contains
weight: 3
---
