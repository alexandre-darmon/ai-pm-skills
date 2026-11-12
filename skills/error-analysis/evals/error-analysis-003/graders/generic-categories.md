---
type: regex  # categories come from the notes, not a generic list
pattern: '(the |your |these |four )?categor\w* (are|were) (just |only )?(a )?guess\w*|(generic|predefined|pre-defined|off[- ]the[- ]shelf|ready[- ]made|a priori|up[- ]?front|in advance|before (reading|anyone reads|looking))[^\n]{0,80}(categor\w*|labels?|taxonom\w*|list|buckets|metrics)|(categor\w*|labels?|modes|taxonom\w*|buckets)[^\n]{0,80}(come|emerge|derived?|built|grow|grown|drawn)[^\n]{0,30}(from|out of) (the )?(notes|reading|traces|conversations)|(categor\w*|labels?|taxonom\w*|buckets)[^\n]{0,40}\b(a guess|guesse?s|guessed)\b[^\n]{0,40}\bbefore\b|categor\w*[^\n]{0,30}\b(that|which) (the )?(reading|notes|expert) (produces?|yields?|gives?|surfaces?)|categor\w* (are|were) (just |only )?(a |mere )?hypothes[ie]s|\bgeneric guess\w*|(from|out of) (someone|a person|an? (domain )?expert|people|a human) reading'
flags: i
---
