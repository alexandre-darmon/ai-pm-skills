---
type: regex  # red line: zero in 50 still allows about 6% (3/50), Wilson about 7%, bound to the number
pattern: 'rule of three|\b3 ?/ ?50\b|(up to|upper bound|upper limit|as high as|could be|could still be|allows?|at most|ceiling|bound(ed)? (of|at|is))[^.!?\n]{0,40}\b(5[.,]9|6|6[.,]0|7|7[.,]1)\s?%|\b0 ?%? ?(to|and|-|–) ?(6|7)([.,]\d)? ?%'
flags: i
weight: 3
---
