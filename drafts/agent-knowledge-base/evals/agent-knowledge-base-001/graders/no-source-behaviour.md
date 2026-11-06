---
type: regex
pattern: '\b(no|weak|empty|poor|conflicting|contradictory|missing|low[- ]confidence|without an?y?)\b(?:(?!owner|maintain)[^\n.]){0,30}\b(sources?|retriev\w*|match\w*|results?|hits?|basis|coverage)\b[^\n.]{0,80}\b(says?|tells?|states?|admits?|declines?|refus\w*|abstains?|routes?|redirects?|refers?|hands? (off|over)|(do|does|must|should)(n[''’]t| not) (answer|guess))\b|\b(says?|tells?|states?|admits?|declines?|refus\w*|abstains?|routes?|refers?)\b[^\n.]{0,80}\b(when|if|on|where)\b[^\n.]{0,30}\b(no|weak|empty|poor|conflicting)\b(?:(?!owner|maintain)[^\n.]){0,30}\b(sources?|retriev\w*|match\w*|results?|hits?)\b|\b(retriev\w*|search)\b[^\n.]{0,20}\b(miss\w*|empty|fails?|finds? nothing|returns? nothing)\b[^\n.]{0,80}\b(says?|tells?|states?|admits?|declines?|refus\w*|abstains?|routes?|refers?|(do|does|must|should)(n[''’]t| not) (answer|guess))\b'
flags: i
---
