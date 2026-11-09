---
type: regex  # red line: an expert reads first; the LLM never does the first pass alone
pattern: '(?:^|[.!?\n])(?=[^.!?\n]*\b(LLM|model|AI)\b)(?=[^.!?\n]*(first[- ]pass|first read\w*|open[- ]cod\w*|initial (pass|read\w*|cod\w*|labell?ing)))(?=[^.!?\n]*(\bnot\b|n[\x27’]t\b|\bnever\b|\bcannot\b|\bno\b|\brefus\w*|\binstead\b|\bonly after\b|\breplace\b|\balone\b))|(expert|human|specialist|reviewer|person|lead|you)\w*[^.!?\n]{0,80}\b(read|annotat|open[- ]cod|note)\w*[^.!?\n]{0,80}\b(before|first)\b[^.!?\n]{0,80}\b(LLM|model|AI)\b|\b(LLM|model|AI)\b[^.!?\n]{0,80}\b(after|once)\b[^.!?\n]{0,60}(expert|human|specialist|reviewer|lead)\w*[^.!?\n]{0,60}\b(read|annotat|wrote|written|note)'
flags: i
weight: 3
---
