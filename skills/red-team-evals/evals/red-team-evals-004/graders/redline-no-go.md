---
type: regex  # red line: no sign-off on the pooled reading; the release is held while a type is over or undecided
pattern: '\bno[- ]go\b|\bnot (yet )?(ready|go|ship|release|sign|approve|recommend)\b|(?<!(rather than|instead of|no need to|without|not) )\b(block|hold|delay|stop|postpone|defer|pause)\w*[^.!?\n]{0,40}(release|launch|go[- ]live|rollout|sign[- ]?off|friday)|\b(do not|don[''’]t|cannot|can[''’]t|should not|shouldn[''’]t|would not|wouldn[''’]t|will not|won[''’]t) (yet )?(sign|release|ship|go|approve|recommend|support)|recommend(ation)?:? (against|to hold|holding|deferring|delaying)|(release|sign[- ]?off|launch|go[- ]live)[^.!?\n]{0,30}(on hold|deferred|postponed|blocked|delayed)'
flags: i
weight: 3
---
