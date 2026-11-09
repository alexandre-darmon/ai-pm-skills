---
type: regex  # specification failures are fixed, not judged
pattern: 'specification|spec(ification)?[- ](failure|gap|error|problem|issue)|(fix|change|update|add|pass|load)\w*[^\n]{0,100}(no|without|not|before|instead of|rather than)[^\n]{0,15}(an? |any )?(LLM )?(eval|evaluator|grader|judge)|(no|not|don.t need)[^\n]{0,20}(an? )?(LLM )?(judge|evaluator|eval)[^\n]{0,60}(fix|prompt|spec|load|pass)'
flags: i
---
