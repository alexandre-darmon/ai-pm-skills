---
type: regex
pattern: 'max\w*[ -](number of )?steps?\W{0,6}\d+|\btoken budget\W{0,6}\d|\d[\d,.]*\s?k? tokens? (per|a|each) run|\b\d+ (model and tool |model\/tool )?(steps|calls|iterations) (per run|max|at most)|\b(at most|no more than|up to|a maximum of|a max of|capped at) \d+ (model and tool |model\/tool |tool )?(steps|calls|iterations|turns)\b'
flags: i
---
