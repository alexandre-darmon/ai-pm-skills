---
type: regex  # the customer-facing figure is worded as a frequency no higher than the top bucket's lower bound (88.7%): "at least 88 in 100", not "about 9 in 10" or 92%
pattern: '(?<![\d.])8[0-8] (in|out of) (every )?100\b|\bat least 8[0-8]([.,]\d)? ?%|(?<![\d.])8[0-8]([.,]\d)? ?% or (more|higher|better)\b|(≥|>=) ?8[0-8]([.,]\d)? ?%|(no higher than|at or below|at most|not above|capped at|rounded down to)[^.\n]{0,15}lower (bound|end|limit)|lower (bound|end|limit)[^.\n]{0,30}rounded down'
flags: i
---
