---
type: regex  # a baseline names the judge model and the date, not only a score
pattern: 'judge(''s)?\W{1,3}model[^.;]{0,60}?(?<!release |ship |launch |go-live )\bdate\b|(?<!release |ship |launch |go-live )\bdate\b[^.;]{0,40}judge(''s)?\W{1,3}model|\bmodel,? (the )?judge,? (and )?(the )?date'
flags: i
---
