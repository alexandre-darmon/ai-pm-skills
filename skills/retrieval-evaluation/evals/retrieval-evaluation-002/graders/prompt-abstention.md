---
type: regex  # prompt fix: answer only from passages, cite, abstain
pattern: 'abst(ain|ention)|(say|answer|reply)[^\n]{0,20}("?not found|it (doesn.t|does not) know|no (basis|answer))|cite[^\n]{0,40}(passage|source)[^\n]{0,30}(each|every|per) (claim|statement|sentence|fact)|(only|strictly) from the (passages|context|retrieved)'
flags: i
---
