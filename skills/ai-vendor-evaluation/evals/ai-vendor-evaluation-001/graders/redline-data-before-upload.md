---
type: regex
flags: i
weight: 3
---
(before|prior to|until|no)\b[^\n]{0,100}(upload|send|sending|share|sharing|transfer|portal|trial|leave)[^\n]{0,200}(processing agreement|data processing|\bDPA\b|art(icle|\.)?\s*28|anonymi[sz]|de-?identif|mask)|(processing agreement|data processing (agreement|addendum)|\bDPA\b|art(icle|\.)?\s*28|anonymi[sz]\w*|de-?identif\w*|mask\w*)[^\n]{0,200}(before|prior to|until|first)\b[^\n]{0,100}(upload|send|shar|transfer|portal|trial|any document|reach)|\b(?:nothing|no (?:data|documents?|files?|personal data)|don['’]t|do not|never)\b(?![^\n]{0,20}\b(?:stops?|prevents?|blocks?|forbids?|wait)\b)[^\n]{0,60}\b(?:upload\w*|send\w*|shar\w*|transfer\w*|go(?:es)? (?:in)?to|reach\w*|leav\w*|portal)\b[^\n]{0,80}\b(?:until|before|unless|prior to)\b[\s\S]{0,300}?(?:processing agreement|data processing (?:agreement|addendum)|\bDPA\b|art(?:icle|\.)?\s*28|anonymi[sz]|de-?identif|mask)
