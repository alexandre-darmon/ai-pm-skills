---
type: regex  # raw agreement explained by imbalance: a judge passing everything agrees 88% here
pattern: '(pass(es|ing)? (everything|every|all)|always (says? |answers? |returns? )?[\"“'']?(pass|correct|ok)|never flag\w*|flags? nothing|rubber[- ]stamp|constant|(says?|answers?|returns?|outputs?) [\"“'']?correct[\"”'']? (to |for )?(everything|every|all)|(does|did|doing) nothing)[^\n]{0,150}(?<![\d.])88(\.0)? ?%|(?<![\d.])88(\.0)? ?%[^\n]{0,150}(pass(es|ing)? (everything|every|all)|always (says? |answers? )?[\"“'']?(pass|correct)|never flag\w*|flags? nothing|rubber[- ]stamp|constant|(says?|answers?) [\"“'']?correct[\"”'']? (to |for )?(everything|every|all)|(does|did|doing) nothing)'
flags: i
---
