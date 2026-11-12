---
type: regex  # score a step on stored upstream output, so two changes do not move at once
pattern: '(same|frozen|stored|fixed|saved) (OCR|upstream) (outputs?|text)\b|(frozen|freeze|fixed|stored|saved|same) ((frozen|stored|fixed|saved) )?(OCR|upstream|input|text|output)s?[^.\n]{0,60}(extract|LLM|model|step)|(extract\w*|LLM|model|step|stage|component)[^.\n]{0,80}\b(on|from|with|using|and) (the )?(same|frozen|stored|fixed|saved) ((frozen|stored|fixed|saved) )?(OCR|upstream|input|text)'
flags: i
---
