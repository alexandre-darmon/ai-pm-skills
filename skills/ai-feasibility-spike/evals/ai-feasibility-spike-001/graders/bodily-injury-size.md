---
type: regex  # the strict class is sized for its stop line (16 cases or more), not the usual 10 per class
pattern: 'bodily injury[^\n]{0,60}\b(1[6-9]|[2-9]\d)\b(?! ?%)(?![.,]\d)|\b(1[6-9]|[2-9]\d)\b(?! ?%)[^\n%]{0,20}(cases|emails|examples)[^\n]{0,30}bodily injury|\b(1[6-9]|[2-9]\d)\b (cases |emails )?(for|on|of|in) (the )?bodily injury|\b(1[6-9]|[2-9]\d)\b (cases )?(per|in each|for each) (class|category)[^\n]{0,200}(over-?represent\w*|more|extra)[^\n]{0,20}bodily injury'
flags: i
---
