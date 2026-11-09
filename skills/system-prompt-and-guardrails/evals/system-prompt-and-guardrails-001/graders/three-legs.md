---
type: regex
pattern: '(?=[\s\S]{0,400}\b(private|personal|customer|sensitive) (data|information|records?)\b)(?=[\s\S]{0,400}\b(untrusted|attacker[- ]controlled)\b)(?=[\s\S]{0,400}\b(external|outbound|exfiltrat\w*|outside)\b)[\s\S]'
flags: i
---
