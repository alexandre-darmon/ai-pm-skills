---
type: regex
pattern: '(?<!\b(?:not|no|never|instead of|rather than)\b[^\n.]{0,40})\b(roll[- ]?out|deploy\w*) (to|across|for) (all|every|the whole|9[, ]?000)'
flags: i
match: not_contains
weight: 5
---
