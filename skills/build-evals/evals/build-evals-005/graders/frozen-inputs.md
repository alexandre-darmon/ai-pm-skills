---
type: regex  # score a step on stored upstream output, so two changes do not move at once
pattern: '(frozen|freeze|fixed|stored|saved|same) (OCR|upstream|input|text|output)s?[^.\n]{0,60}(extract|LLM|model|step)|(extract\w*|LLM|model)[^.\n]{0,60}\b(on|from) (the )?(same|frozen|stored|fixed|saved) (OCR|upstream|input|text)'
flags: i
---
