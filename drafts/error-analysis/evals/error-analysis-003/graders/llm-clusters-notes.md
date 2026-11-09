---
type: regex  # the LLM clusters the expert's notes, afterwards
pattern: '\b(LLM|model|AI)\b[^\n]{0,100}(cluster|group|sort|organi[sz]e|merge|propos|suggest|consolidat)\w*[^\n]{0,80}(notes|annotations|comments|observations)|(notes|annotations|observations)[^\n]{0,100}\b(LLM|model|AI)\b[^\n]{0,60}(cluster|group|sort|organi[sz]e|merge|consolidat)'
flags: i
---
