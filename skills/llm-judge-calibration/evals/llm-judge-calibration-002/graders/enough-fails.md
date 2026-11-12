---
type: regex  # 9 expert fails cannot estimate TNR; the test needs many more
pattern: '(only|just) (9|nine) (expert |real )?(fails?|failures|failing|negatives?|positives?|missed exclusions?|bad summaries|omissions?)\b[^\n]{0,120}(too few|very few|not enough|cannot|can[’'']?t|indicative|wide|unreliable|imprecise|small|little|interval|lower bound)|(rests?|based|relies|depends) on (only|just) (9|nine)\b|\b(9|nine) (fails?|failures|failing|negatives?|positives?|missed exclusions?|bad summaries|omissions?|summaries (missing|with))[^\n]{0,100}(too few|very few|not enough|cannot|can[’'']?t|wide|indicative|small)|(at least|≥|>=|about|around|aim (for|at)|target of|minimum of)\s*\d{2,3}(\s*(–|-|to)\s*\d{2,3})?\+?\s*(expert[- ]|real[- ]|true[- ])?(fails?|failures|failing|negatives?|positives?|missed[- ]exclusion|summaries (that|which|with|missing)|bad|omission|with an? (missed|missing) exclusion)'
flags: i
---
