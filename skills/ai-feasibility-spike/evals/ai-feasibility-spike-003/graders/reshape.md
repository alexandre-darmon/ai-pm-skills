---
type: regex  # two more weeks for more dispute cases is a reshape: a new spike with its own appetite and kill date, signed again, not an extension
pattern: '\breshap\w*|\bnew (spike|appetite)\b|\b(second|separate|follow-?up|fresh) spike\b|\bnew (time ?box|kill date|end date)\b[^\n.]{0,80}\b(sign\w*|appetite|ceiling)\b|\bits own (time ?-?box|appetite|kill date|end date|cost ceiling|budget|deadline)\b[^\n.]{0,80}\b(sign\w*|time ?-?box|appetite|kill date|end date|cost ceiling|budget|deadline)\b|\bnot an? extension\b'
flags: i
---
