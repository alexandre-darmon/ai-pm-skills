---
type: regex  # the failed answers already graded are split by first failing stage
pattern: '\b58\b|(each|every|the) (\w+ )?(failed|wrong|incorrect)[^\n]{0,30}answers?[^\n]{0,150}(top[- ]?5|retriev\w*|passages?|pieces?|chunks?|stage|context)'
flags: i
---
