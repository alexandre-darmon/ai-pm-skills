---
type: regex  # the overdraft step decides on creditworthiness
pattern: '(?<!\b(not|n[''’]t|no|never)\b[^.\n]{0,60})(annex III[^\n]{0,60}\b5\s?\(b\)|annex III[^\n]{0,60}\b5b\b|\b(point|para(graph)?) 5\s?\(b\)|\b5\s?\(b\)[^\n]{0,40}annex)'
flags: i
---
