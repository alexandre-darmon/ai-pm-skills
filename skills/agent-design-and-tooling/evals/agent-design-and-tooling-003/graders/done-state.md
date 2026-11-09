---
type: regex
pattern: '\bdone\b[^\n.]{0,30}\b(when|means|state|is)\b|(done|completion) (criteria|criterion|condition|state)|(run|agent|loop|task)[^\n.]{0,20}\b(is (done|complete|finished)|ends|finishes|completes|exits)\b[^\n.]{0,10}\bwhen\b|success(ful)? (exit|end)|\bexits?\W{0,4}success'
flags: i
---
