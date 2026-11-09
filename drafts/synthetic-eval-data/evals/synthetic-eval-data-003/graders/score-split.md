---
type: regex  # 94% read as a score on synthetic cases, real reported apart
pattern: '94 ?%[^\n]{0,120}(synthetic|not representative|overstat|inflat|optimistic|says little|tidy|clean)|(separately|apart)[^\n]{0,60}(real|synthetic)|(real|synthetic)[^\n]{0,60}(separately|apart)|(real|synthetic)[^\n]{0,20}(vs|versus|and)[^\n]{0,20}(real|synthetic)[^\n]{0,30}scores?|94 ?%[^\n]{0,40}mislead\w*|(separated)[^\n]{0,60}(real|synthetic)|(real|synthetic)[^\n]{0,60}(separated)'
flags: i
---
