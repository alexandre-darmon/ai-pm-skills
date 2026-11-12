---
type: regex  # grades whether stated constraints are kept
pattern: '(constraint|fact|preference|instruction|condition)s?[^\n.]{0,30}(kept|retained|retention|respected|carried|remembered|held|maintained)|(kept|keep|retain|respect|carr|remember|hold|maintain)\w*[^\n.]{0,30}(stated|given|earlier|previous)[^\n.]{0,20}(constraint|fact|preference|condition)s?|(constraint|fact|preference|condition)s? (stated|given|set|expressed)[^\n.]{0,20}(earlier|before|previously|at the start)'
flags: i
---
