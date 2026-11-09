---
type: regex  # 9 expert fails cannot estimate TNR; the test needs many more
pattern: '(only|just) (9|nine)\b[^\n]{0,120}(too few|not enough|cannot|can[’'']?t|indicative|wide|unreliable|imprecise|small|little|nothing)|\b(9|nine) (fails?|failures|failing|negatives?|missed exclusions?|bad summaries|omissions?|summaries (missing|with))[^\n]{0,100}(too few|not enough|cannot|can[’'']?t|wide|indicative|small)|(at least|≥|>=|about|around|aim (for|at)|target of|minimum of)\s*\d{2,3}\s*(expert[- ])?(fails?|failures|failing|negatives?|missed[- ]exclusion|summaries (that|which|with|missing)|bad|omission)'
flags: i
---
