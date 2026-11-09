---
type: regex  # dimensions, style anchors or the distribution check grounded in real claims traffic
pattern: '(real|actual|logged|historical|past) (customer |policyholder )?(questions|calls|claims|emails|conversations|tickets|declarations)[^\n]{0,120}(dimensions?|ground|style|distribution|anchor)|dimensions?[^\n]{0,120}(real|actual|logged|historical)|(style|anchor\w*|distribution|compar\w*)[^\n]{0,80}\b(real|actual|logged|historical) (customer |policyholder )?(questions|calls|claims|emails|conversations|tickets|declarations|messages|traffic|chats)\b|\b(real|actual|logged|historical) (customer |policyholder )?(messages|traffic|chats)\b[^\n]{0,120}(dimensions?|ground|style|distribution|anchor)'
flags: i
---
