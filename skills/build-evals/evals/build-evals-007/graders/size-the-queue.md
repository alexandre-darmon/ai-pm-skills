---
type: regex  # what the skill adds: with a one-point gap (true 98%, bar 97%) the lower bound clears only at about 1,100 cases, so more cases before Thursday will not settle it
pattern: '\b([89]\d\d|[1-9],?\d\d\d)\b[^.\n]{0,40}\b(cases|claims|examples|labell?ed)|(a|over a|more than a|about a|around a|roughly a) thousand|(more|extra|additional|new) (labell?ed |test )?(cases|claims|examples)[^.\n]{0,60}\b(will not|won[''’]?t|cannot|can[''’]?t|do not|don[''’]?t|does not|doesn[''’]?t)\b[^.\n]{0,30}\b(settle|fix|close|change|get there|clear)'
flags: i
---
