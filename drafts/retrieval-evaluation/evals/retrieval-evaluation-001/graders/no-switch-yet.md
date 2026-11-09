---
type: regex  # regression guard: the switch waits for the diagnosis
pattern: '(not|n.t|hold off|premature|before)[^\n]{0,40}(switch|swap|chang|replac|mov)\w*[^\n]{0,30}(LLM|model)|(LLM|model) (switch|change)[^\n]{0,60}(not|premature|wait|later|only (if|when|after))'
flags: i
---
