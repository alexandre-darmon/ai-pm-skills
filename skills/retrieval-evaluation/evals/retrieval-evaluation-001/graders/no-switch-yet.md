---
type: regex  # regression guard: the switch waits for the diagnosis
pattern: '(not|n.t|hold off|premature|before)[^\n]{0,40}(switch|swap|chang|replac|mov)\w*[^\n]{0,30}(LLM|model)|(LLM|model) (switch|change)[^\n]{0,60}(not|premature|wait|later|only (if|when|after))|\b(not|n[\x27’]t|hold off on)\b[^\n]{0,15}\b(approve|endorse|recommend|fund|sign off)\b[^\n]{0,10}\bthe (LLM |model )?switch\b|\b(switch|swap|chang|replac|mov)\w* (to )?(the |a )?(larger |bigger |new )?(LLM|model)\b[^\n]{0,30}\bonly (if|when|after)\b'
flags: i
---
