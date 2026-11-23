---
type: regex  # wrong-country policy is the largest mode (7), and on the same line it is traced to its cause: the country is never passed, a specification gap to fix
pattern: '(?:^|\n)(?=[^\n]*\b(7|seven)\b)(?=[^\n]*\b(countr|entit|jurisdiction))(?=[^\n]*\b(specification|spec (gap|failure)|fix (it )?(first|now)|never (passed|told|given|sent)|not (passed|told|given|sent)|isn.t (passed|told|given|sent)|(pass|passing|send|sending|inject\w*)\b[^\n]{0,20}\b(the |employee.s |their |user.s )?country\b))'
flags: i
---
