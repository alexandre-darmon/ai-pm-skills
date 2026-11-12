---
type: regex  # the user's task is still measured on attacked inputs, not only whether the attack got through
pattern: 'utility under attack|under attack[^\n.]{0,60}(utility|task|pass|success|complet|correct)|(utility|task (success|completion)|pass rate|completion rate|success rate)[^\n.]{0,50}\b(under|during|with|on|for) (the |an |each )?(attack|injected|poisoned|attacked|planted)|(attacked|injected|poisoned|planted)[^\n.]{0,20}(variants?|versions?|copies|tasks|emails|runs|cases)[^\n.]{0,80}\b(still|correctly|completed?|legitimate|genuine|right action|approved action|intended action)|still (does|do|completes?|handles?|performs?|gets?|takes?)[^\n.]{0,60}\b(when|while|with|despite|even)\b[^\n.]{0,40}(attack|inject|planted|poison)'
flags: i
---
