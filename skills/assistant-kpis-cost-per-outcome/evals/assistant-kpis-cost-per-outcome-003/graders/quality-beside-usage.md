---
type: regex  # no usage KPI alone
pattern: '\bpair(s|ed|ing)?\b[^\n]{0,80}(quality|correct)|(quality|correct)[^\n]{0,80}\bpair(s|ed)?\b|(each|every|no) usage (KPI|panel|metric|line|figure)[^\n]{0,80}(quality|correct)|(usage|sessions?|active users)[^\n]{0,60}\b(never|not)\b[^\n]{0,20}alone|same grain|usage\s*(↔|<->)\s*quality|(next to|beside|alongside) (the |a |its )?(quality|correct)'
flags: i
---
