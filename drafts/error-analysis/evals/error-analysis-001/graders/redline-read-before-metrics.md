---
type: regex  # red line: metrics and judges come after reading real outputs, never from a generic list
pattern: '(read|annotat|review|look at|open[- ]cod)\w*[^\n]{0,120}\b(before|first)\b[^\n]{0,120}(metric|grader|judge|evaluator|criteri|scor)|(metric|grader|judge|evaluator|criteri|scor)\w*[^\n]{0,120}\b(after|once|from|only when|until|before)\b[^\n]{0,80}(read|annotat|review|looked at|open[- ]cod|failure modes?|error analysis)|(before|first)[^\n]{0,60}(metric|grader|judge|evaluator|criteri|scor)\w*[^\n]{0,80}(read|annotat|open[- ]cod|error analysis)'
flags: i
weight: 3
---
