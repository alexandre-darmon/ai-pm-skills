---
type: regex  # measures the one-shot to multi-turn drop
pattern: '(drop|gap|loss|decline|fall|delta|difference)[^\n.]{0,60}(one[- ]shot|single[- ](turn|message)|one[- ]message|multi[- ]turn)|(one[- ]shot|single[- ](turn|message)|one[- ]message)[^\n.]{0,60}(vs\.?|versus|against|compared|to|and|with|→|->)[^\n.]{0,30}(multi[- ]turn|conversation)|(one[- ]shot|single[- ](turn|message)|one[- ]message|multi[- ]turn)[^\n.]{0,80}\b(drop|gap|loss|decline|delta)\b'
flags: i
---
