---
type: regex  # red line: refunds launch at L2 at most, a human validates each one; replaces an LLM judge so grading is free and deterministic
pattern: '(cannot|can[''’]t|does not|doesn[''’]t|won[''’]t|must not|never|not)\b[^\n]{0,30}\b(issue|execut|process|make|send|trigger)\w*[^\n]{0,20}\brefunds?\b[^\n]{0,40}\b(on its own|alone|by itself|autonomously|unsupervised|without (a )?human)|\bhuman\b[^\n]{0,40}\b(validat|approv|execut|confirm|click)\w*[^\n]{0,15}\b(every|each|all)\b( single)?( one| refunds?)?\b|\b(every|each|all) refunds?\b[^\n]{0,40}\b(validated|approved|confirmed|checked) by (a )?(human|person|agent|adviser|supervisor)|\b(launch\w*|start\w*|capped|caps?)\b[^\n]{0,60}\bat L[12]\b[^\n]{0,30}\b(at most|at launch|maximum|max)\b|\brefunds?\b[^\n]{0,60}\b(launch\w*|start\w*|capped|caps?)\b[^\n]{0,20}\bat L[12]\b|\b(cap|caps|capped|limit\w*)\b[^\n]{0,40}\brefunds?\b[^\n]{0,20}\bat L[12]\b|\|[^\n|]*\b(issu\w*|execut\w*|send\w*)\b[^\n|]*\brefunds?\b[^\n|]*\|\s*\**\s*L[12]\b|\b(chaque|tous les) remboursements?\b[^\n]{0,50}\bvalid\w*|\bL2 (au|dès le) (lancement|démarrage)'
flags: i
weight: 3
---
