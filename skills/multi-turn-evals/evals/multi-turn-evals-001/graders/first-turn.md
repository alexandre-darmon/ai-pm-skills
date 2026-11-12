---
type: regex  # locates where each failed conversation broke
pattern: 'first (failing|failed|bad|broken|wrong|faulty) (turn|reply|message|step|point)|(turn|reply|message) (where|at which|in which)[^\n.]{0,60}(drop|lost|los|forg|ignor|broke|fail|went wrong)|where (the|each) (conversation|constraint)[^\n.]{0,40}(drop|lost|forg|broke|went wrong)|(at which|at what) (point|turn|message|reply)[^\n.]{0,60}(drop|lost|los|forg|ignor|broke|fail|went wrong)|where in the (conversation|dialogue|exchange)[^\n.]{0,60}(drop|lost|los|forg|ignor|broke|fail|went wrong)'
flags: i
---
