---
type: regex  # the gap's paired interval, not its point estimate, must sit inside the tolerance (about ±12 points at 9 discordant pairs of 50); a ± on each rate alone or a proposed tolerance does not count
pattern: '(\bgap|difference|\bpaired\b|discordant|disagree\w*)(?:(?!\b(each|rates?|tolerances?|either|both|tighten|widen)\b)(?:[^.!?\n]|\.(?=\d))){0,100}(±|\+/-|plus or minus) ?1[0-3]([.,]\d+)? ?(%|points?|pts|pp|percentage)|(−|-|–|minus )[4-7]([.,]\d+)? ?(%|points?|pts|pp)? ?(to|and|–|—|,) ?\+?1[5-9]([.,]\d+)?|(interval|\bCI\b|error bars?|uncertainty|margin)[^\n.]{0,80}(exceed|outside|beyond|wider than|larger than|bigger than|cross|spill|extend|goes past|runs past|not (fully |entirely )?(inside|within))\w*[^\n.]{0,40}(tolerance|±8|8 points|8 pp|\+8)|(whole|entire|full) (confidence |95 ?% )?interval[^\n.]{0,60}(inside|within)|point estimate[^\n.]{0,80}(not enough|insufficient|is not the test|does not validate|doesn.t validate|not the right test)'
flags: i
weight: 2
---
