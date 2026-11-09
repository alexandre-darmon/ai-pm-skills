---
type: regex  # dimensions grounded in real claims traffic
pattern: '(real|actual|logged|historical|past) (customer |policyholder )?(questions|calls|claims|emails|conversations|tickets|declarations)[^\n]{0,120}(dimensions?|ground|style|distribution|anchor)|dimensions?[^\n]{0,120}(real|actual|logged|historical)'
flags: i
---
