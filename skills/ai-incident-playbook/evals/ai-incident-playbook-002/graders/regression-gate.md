---
type: regex  # the leak becomes a regression case shown to fail on the faulty version, and it gates the fix
pattern: '\bfail\w*\b[^\n.]{0,25}\b(on|against|with|before|under)\b[^\n.]{0,10}\b(faulty|current|old|unfixed|vulnerable|broken|pre-?fix|existing|live|previous|leaking)\b|\breproduc\w*\b[^\n.]{0,40}\b(leak|injection|failure|incident)\b[^\n.]{0,40}\b(current|faulty|old|unfixed|vulnerable|before the fix)\b|\b(fix|patch|assistant|system|service)\b[^\n.]{0,30}\b(ships?|goes (back|live)|re-?enabl\w*|restor\w*|returns?)\b[^\n.]{0,20}\bonly (when|once|after)\b[^\n.]{0,40}\b(regression|golden|injection|new|those) (eval )?(cases|tests)\b'
flags: i
---
