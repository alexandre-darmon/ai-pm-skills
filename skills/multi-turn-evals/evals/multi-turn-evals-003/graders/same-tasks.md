---
type: regex  # reuses the existing 200 questions given over several turns
pattern: '(same|existing|those|these|the|all|each of the) 200\b[^\n]{0,120}(turns|multi[- ]turn|conversation|split|spread|one fact|shard)|(split|spread|shard|break|rewrite|convert|turn)\w*[^\n.]{0,40}(the |those |these |same |existing |all )200\b|(same|identical|existing) (one[- ]message |one[- ]shot |single[- ]turn )?(tasks|questions|cases|items)[^\n]{0,100}(turns|multi[- ]turn|split|spread|one fact|shard)'
flags: i
---
