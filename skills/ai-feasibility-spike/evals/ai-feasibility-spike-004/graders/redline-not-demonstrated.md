---
type: regex  # red line: a point estimate at the bar on 10 cases is not "meets the bar"; the negation must sit next to the verb
pattern: '(?:^|[!?\n]|\.(?=\s))(?=(?:(?!\.\s)[^!?\n])*?(registry|9 ?(of|/|out of) ?10|both|neither|either|the bar|90 ?%))(?=(?:(?!\.\s)[^!?\n])*?(\b(not|never|neither|nor|cannot|can.t|isn.t|aren.t|doesn.t|don.t|didn.t|won.t)\b|no evidence|insufficient|too (few|small))[^\n.!?]{0,25}(demonstrat|establish|prov(e|en)\b|\bshows?\b|shown|support|\bmeets?\b|\bmet\b|clear|confirm))'
flags: i
weight: 4
---
