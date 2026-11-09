---
type: regex  # the wrong refunds become regression cases before the fixed agent goes back up
pattern: '(regression|eval|test|golden)[- ](cases?|set|suite)\b[^\n]{0,160}\b(before|prior to|ahead of|until)\b[^\n]{0,60}\b(fix\w*|re-?enabl\w*|redeploy\w*|ship\w*|release\w*|restor\w*|back to L4|return\w* to L4|go(es|ing)? back)|\b(before|prior to|ahead of|until)\b[^\n]{0,60}\b(fix\w*|re-?enabl\w*|redeploy\w*|ship\w*|release\w*|restor\w*|back to L4|return\w* to L4)\b[^\n]{0,160}(regression|eval|test|golden)[- ](cases?|set|suite)'
flags: i
---
