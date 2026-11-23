---
type: regex  # abstention is specified as a measurable expected answer: a plain "not found" with a route to a person, on questions whose answer is in no procedure
pattern: '(expected|correct|right|target) (answer|response|output) (is|=|:|should be)[^\n]{0,20}"?not (found|in|covered)|"?not found[^\n]{0,50}\b(ask|route|contact|refer\w*|person|owner|team|escalat\w*|human|colleague)\b'
flags: i
---
