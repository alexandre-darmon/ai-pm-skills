---
type: regex  # sizes the rare legal class for its threshold (about 140-200+ warranty cases), not by traffic share
pattern: '(cases|sample)[^.\n]{0,30}\b(its|the|their) (threshold|bar|gate) (needs|requires)|warranty[^.\n]{0,40}\b(1[4-9]\d|[2-9]\d\d|1,\d{3})( ?(to|–|-) ?\d[\d,]*)? (real |labell?ed )?(cases|examples|conversations)|\b(1[4-9]\d|[2-9]\d\d)\+? (real |labell?ed )?warranty (cases|examples|conversations)|±\s?\d+ points?[^.\n]{0,30}\b\d+ cases'
flags: i
---
