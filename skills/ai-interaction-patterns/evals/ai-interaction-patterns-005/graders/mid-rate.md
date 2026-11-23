---
type: regex  # the middle bucket read with its interval (Wilson about 67.6% to 79.9% for 141 of 190), not only its 74% point rate
pattern: '(?<![\d.])(0\.)?6[5-9]([.,]\d+)? ?%?\s*(to|–|—|-|,)\s*(0\.)?(7[89]|8[01])([.,]\d+)? ?%|\b(at least|no more than|lower bound (of|is|at)( about)?) 6[5-9]([.,]\d+)? ?(%|in 100\b)|(?<![\d.])6[5-9] (in|out of) 100\b'
flags: i
---
