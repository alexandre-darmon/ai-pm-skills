---
type: regex  # production failures become test cases for the assistant
pattern: '\b(?:(?:add|turn|feed|hand|promot|convert|include|put|become)\w*|use[ds]?)\b[^\n]{0,100}\b(golden[- ]set|golden (cases|dataset)|evals?( \w+)? (set|suite|cases?|dataset)|evaluation (set|suite|cases?|dataset)|regression (set|suite|tests?|cases?)|test (set|suite|cases))\b|\b(golden[- ]set|evals?( \w+)? (set|suite|cases?|dataset)|evaluation (set|suite|cases?|dataset)|regression (set|suite|tests?|cases?)|test (set|suite|cases))\b[^\n]{0,100}(from|candidate|these conversations|this cluster|the sample)'
flags: i
---
