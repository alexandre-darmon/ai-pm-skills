---
type: regex  # no rollback on this point alone: a negation tied to the verb (at most two words between, not "wait"), a rollback called premature or unjustified, or an answer that opens with "No"
pattern: '\b(do not|don[’'']t|not|no|never|shouldn[’'']t|wouldn[’'']t|should not|would not|hold off( on)?|avoid|against|recommend against)\s+((?!wait|delay)\w+\s+){0,2}(roll(ing)?[- ]?back|revert(ing)?)\b|\b(roll(ing)?[- ]?back|revert(ing)?)\b[^\n.]{0,40}\b(isn[’'']t|is not|not (yet )?(justified|warranted|the (safe|right) (default|move|call))|premature|unjustified|unwarranted)|^[\s*#>_]*(no|not yet|not today)\b[*_]*[,.:;!]'
flags: i
---
