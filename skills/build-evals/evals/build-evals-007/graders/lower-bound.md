---
type: regex  # reads the queue on the lower bound: under the bar means not demonstrated, not a pass
pattern: 'lower (bound|limit|end)(?:[^.\n]|\.\d){0,100}\b(under|below|short of|beneath|less than)\b|lower (bound|limit|end)(?:[^.\n]|\.\d){0,40}(does not|doesn.t|didn.t|did not|fails to|never) (clear|reach|meet)|not demonstrated|(bar|threshold|9[57] ?%) (sits|lies|falls|is) (inside|within) (it\b|(the|its|that) (interval|range))|(can.t|cannot|can not|doesn.t|does not|too few to|not enough to) (show|establish|demonstrate)\w*[^.\n]{0,40}\b(clears?|meets?|at least|above|is|has|have|reach(es)?) (the )?9[57] ?%'
flags: i
---
