---
type: regex  # the approval stays
pattern: '(keep|keeping|retain|maintain)\w*[^\n.]{0,40}(approval|sign-?off|four[- ]eyes)|(approval|sign-?off)[^\n.]{0,40}(stays?|remains?|kept|in place)|(?<!go/)\bno[- ]go\b|not (yet )?(remove|drop|lift)\w*[^\n.]{0,30}(approval|sign-?off)|(do not|don.t|cannot|can.t|should not|shouldn.t)[^\n.]{0,20}(remove|drop|lift)\w*[^\n.]{0,30}(approval|sign-?off)'
flags: i
---
