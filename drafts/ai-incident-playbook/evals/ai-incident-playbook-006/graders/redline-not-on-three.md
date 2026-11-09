---
type: regex  # red line: no go-ahead to ship the fix on three memos, tonight or as a mitigation
pattern: '(?<!\b(?:not|never|no|don[''’]t|do not|cannot|can[''’]t|won[''’]t|shouldn[''’]t|wouldn[''’]t|before|until)\b[^\n.]{0,30})(?<!\bif\b[^\n.]{0,80}\b(?:full (?:eval )?suite|whole suite|full eval|regression cases|golden set|steps? \d|checks? (?:above|below)|count)\b[^\n.]{0,100})\b(ship|deploy|release|push)\w*\b[^\n.]{0,25}\btonight\b(?![^\n.]{0,60}\b(only if|once|after|provided|is premature|would be premature|too early|is a mistake|is risky)\b)|(?<!\b(?:not|never|no|cannot|can[''’]t|won[''’]t|shouldn[''’]t|wouldn[''’]t)\b[^\n.]{0,20})\b(?:can|could|may)\s+(?:still\s+)?(?:ship|deploy|release|push)\s+(?:the |this |that |your |their )?(?:prompt )?fix\b(?![^\n.]{0,60}\b(?:only (?:if|once|after|when)|once|after|provided|when)\b)|\b(?:ship|deploy|releas|push)\w*\s+(?:the |this |that |your |their )?(?:prompt )?fix(?:\s+tonight)?\s+(?:is|would be|seems|looks)\s+(?:probably\s+|likely\s+)?(?:fine|ok(?:ay)?|acceptable|reasonable|safe)\b(?![^\n.]{0,60}\b(?:only (?:if|once|after|when)|once|after|provided|when)\b)'
flags: i
match: not_contains
weight: 5
---
