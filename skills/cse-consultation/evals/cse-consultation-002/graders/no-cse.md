---
type: regex  # no CSE below 11 employees for 12 consecutive months
pattern: '\bno CSE\b|\b(not|n[''’]t) (have|need|required to (have|set up|elect)|set up|elect)[^\n]{0,20}\b(a |any )?CSE\b|\bno (legal )?(obligation|requirement|duty) to (have|set up|elect|hold|inform or consult|consult)[^\n]{0,40}\b(CSE|employee representatives|representatives)\b|\bCSE[^\n]{0,60}(not (required|mandatory)|only ((required|mandatory|compulsory) )?(from|at|once|when)[^\n]{0,40}\b11\b|from 11 employees|(starts|kicks in|applies|becomes (mandatory|compulsory|required)|threshold is) (only )?(at|from)?[^\n]{0,15}\b11\b)|\b(below|under|fewer than|less than) (the )?((CSE )?threshold of )?11\b|\bpas de CSE\b|\baucun CSE\b|moins de (11|onze) salariés'
flags: i
---
