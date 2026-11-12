---
type: regex  # what the skill adds: near 96.7% the lower bound clears 95% only with several hundred cases (about 650), so more cases will not settle it quickly; 100 to 300 cases is the model-alone guess
pattern: '\b([4-9]\d\d|[1-9],?\d\d\d)\b[^.\n]{0,40}\b(cases|examples|labell?ed|test cases)|\bn ?[=≈~] ?([4-9]\d\d|[1-9],?\d\d\d)\b|(more|extra|additional|new) (labell?ed )?(cases|examples)[^.\n]{0,60}\b(will not|won[''’]?t|cannot|can[''’]?t|do not|don[''’]?t|does not|doesn[''’]?t)\b[^.\n]{0,30}\b(settle|fix|close|change|get there|clear)'
flags: i
---
