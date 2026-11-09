---
type: regex  # confirmed failures become regression cases in the golden set
pattern: 'regression (case|test|set|suite)s?|(golden|eval(uation)?|test) (set|suite)[^\n]{0,80}\b(add|new|grow|feed|append)|\b(add|feed|append|turn|become|join)\w*[^\n]{0,80}(golden|eval(uation)?|regression) (set|suite|case)'
flags: i
---
