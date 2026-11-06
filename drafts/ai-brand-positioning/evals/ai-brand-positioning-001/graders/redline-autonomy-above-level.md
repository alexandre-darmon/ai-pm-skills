---
type: regex
pattern: '(?:^|\n)[#*>_\s|]*(?:after\s*(?:[:*|—(-]|\n)|rewrit(?:e|ten)\s*(?:[:*|—(-]|\n)|(?:the )?(?:new|revised|final|rewritten|proposed|suggested|updated) (?:[\w-]+ )?(?:copy|text|version|page|post|announcement)\b)[^\n]*(?:\n[^\n]*){0,6}?(?<!(?:\bnot?\b|\bnever\b|\bnothing\b|\bneither\b|\bwithout\b|n[\x27’]t\b|\bremov|\bdrop|\bcut\b|\bdelet|\binstead\b|\bbefore\b|\bbanned\b|\bavoid|\bout\b)[^\n]{0,60})(?<!["“‘«\x27])\b(?:autonomous(?:ly)?|agents?|replaces? (?:your|the)[^\n]{0,20}(?:review|team)|on its own|by itself|no (?:human |manual |analyst )?review)\b(?![^\n]{0,30}\b(?:claim|figure|number|wording|is gone|removed)\b)'
flags: i
match: not_contains
weight: 5
---
