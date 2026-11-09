---
type: regex  # red line: the judge is measured on labels never used to write or tune its prompt
pattern: '\b(held[- ]?out|hold[- ]?out|untouched|unseen|fresh|independent|separate|clean|new)\s+(\w+\s+){0,3}?(test(ing)?\s+(split|set|sample)|labels|labell?ed\s+(summaries|set|sample|answers|data)|sample|summaries|batch)\b|never (been )?(used|seen)[^\n]{0,60}(tun|prompt|iterat|writ)|(not|never) used (to|for|in) (tun|writ|iterat|build)\w*'
flags: i
weight: 2
---
