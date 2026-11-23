---
type: regex  # forbidden: the same order refunded twice; seeds the timeout that did commit apart from the one that did not
pattern: 'time[sd]?[ -]?outs?\b[^\n|]{0,80}\b(commit\w*|went through|was (written|executed|applied)|landed)|\b(commit\w*|went through|was (written|executed|applied)|landed)\b[^\n|]{0,80}time[sd]?[ -]?outs?\b'
flags: i
---
