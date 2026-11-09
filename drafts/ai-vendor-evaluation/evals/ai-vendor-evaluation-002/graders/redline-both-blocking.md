---
type: regex
flags: i
weight: 3
---
^(?=[\s\S]*(?:(?:model|version|§ ?7\.2|7\.2)[\s\S]{0,400}\b(block\w*|deal[- ]?breakers?|show[- ]?stoppers?|non[- ]negotiable|must[- ]haves?)\b|\b(block\w*|deal[- ]?breakers?|show[- ]?stoppers?|non[- ]negotiable|must[- ]haves?)\b[\s\S]{0,400}(?:model change|model|version|§ ?7\.2|7\.2)))(?=[\s\S]*(?:(?:train\w*|§ ?9\.4|9\.4|customer content)[\s\S]{0,400}\b(block\w*|deal[- ]?breakers?|show[- ]?stoppers?|non[- ]negotiable|must[- ]haves?)\b|\b(block\w*|deal[- ]?breakers?|show[- ]?stoppers?|non[- ]negotiable|must[- ]haves?)\b[\s\S]{0,400}(?:train\w*|§ ?9\.4|9\.4|customer content)))
