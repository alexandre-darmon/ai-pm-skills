---
type: regex  # turns the first-failing-step counts into the most a model swap can recover
pattern: '(recover|gain|win|fix|improve|add|lift|move)\w*[^.\n]{0,40}\bat most\b|\bat most\b[^.\n]{0,30}\b(points?|invoices|cases)\b|\bceiling\b|can(no|’|'')?t (take|get|push|lift|move) (you|it|the score|accuracy)? ?(past|beyond|above)|(upper bound|maximum|max) (on|of|for) (the|any)? ?(gain|improvement|uplift)'
flags: i
---
