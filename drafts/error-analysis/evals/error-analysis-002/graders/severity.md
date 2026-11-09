---
type: regex  # the salary disclosure ranks high whatever its count
pattern: '(salary|confidential|colleague|privacy|personal data)[^\n]{0,200}(severity|severe|red line|regardless|whatever (its|the) (count|frequency)|despite|even (once|one|a single)|one (case|occurrence|trace) is enough|top priority|highest|critical)|(severity|red line|regardless|critical|highest)[^\n]{0,120}(salary|confidential|colleague|privacy)'
flags: i
---
