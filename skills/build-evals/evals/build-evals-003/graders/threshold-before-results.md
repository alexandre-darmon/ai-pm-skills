---
type: regex  # the bar is fixed before the run it judges, and someone answers for it
pattern: '^(?=[\s\S]*((thresholds?|bars?|gates?|cut-?offs?|pass lines?)\b[^\n]{0,120}\b(before|ahead of|prior to)\b[^\n.]{0,40}\b(runs?|results?|scores?|see\w*|eval)\b|\b(before|ahead of|prior to)\b[^\n.]{0,40}\b(runs?|results?|scores?|seeing)\b[^\n]{0,100}\b(thresholds?|bars?|gates?|cut-?offs?)\b|(thresholds?|bars?|gates?|cut-?offs?)\b[^\n]{0,80}\b(never|not|no)\b[^\n.]{0,20}\b(after|once)\b[^\n.]{0,30}\b(results?|scores?|seeing|run)\b))(?=[\s\S]*(\bsign(s|ed|er|ing)?\b|\bsign-?off|\bowners?\b|\bapprov\w+|\baccountable\b|\brelax))'
flags: i
---
