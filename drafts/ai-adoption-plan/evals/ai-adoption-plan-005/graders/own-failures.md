---
type: regex
pattern: '(failed|failing)[- ](evals?|tests?|cases?)|\bevals?\b[^\n.]{0,20}\bfail|fail\w*[^\n.]{0,20}\b(evals?|test set|golden set)\b|(past|previous|prior|real|recorded|logged|actual)[- ]incidents?|incidents?[- ](logs?|records?|reports?|cases?|reviews?|files?|history)|near[- ]miss|(QA|audit|error)[- ](logs?|findings?)'
flags: i
---
