---
type: regex  # red line: no go-ahead to ship tonight on three memos
pattern: '(?<!\b(?:not|never|no|don[''’]t|do not|cannot|can[''’]t|won[''’]t|shouldn[''’]t|wouldn[''’]t)\b[^\n.]{0,30})\b(ship|deploy|release|push)\w*\b[^\n.]{0,25}\btonight\b(?![^\n.]{0,60}\b(only if|once|after|provided|is premature|would be premature|too early|is a mistake|is risky)\b)'
flags: i
match: not_contains
weight: 5
---
