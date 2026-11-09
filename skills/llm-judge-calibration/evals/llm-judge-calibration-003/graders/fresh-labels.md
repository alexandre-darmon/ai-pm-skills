---
type: regex  # fresh expert labels on production memos, which also re-validate the judge
pattern: '(label|review|grade)\w*\s+(\w+\s+){0,4}?(fresh|new|current|recent|this month[’'']?s?|last month[’'']?s?|production)\s+(sample|memos|batch|set)\b|\b(fresh|new|current|recent)\s+(\w+\s+){0,2}?(labels|labell?ed (sample|memos|set))\b|\bre-?validat\w*|\brevalidat\w*|\bre-?test\w*'
flags: i
---
