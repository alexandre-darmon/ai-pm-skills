---
type: regex  # the interval is computed on the random stream
flags: i
---
random[^\n]{0,80}(Wilson|interval|± ?\d|\+/- ?\d)|(Wilson|interval)[^\n]{0,60}\brandom|\b(main|random|representative) (sample|stream)s? only\b[^\n]{0,100}(Wilson|interval|± ?\d|\+/- ?\d)
