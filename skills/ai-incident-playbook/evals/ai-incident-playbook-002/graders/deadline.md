---
type: regex  # the art. 33 date computed (Fri 13 Nov, 10:00) and checked against today: it has passed, notify now with reasons
pattern: '(?:Fri(?:day)?\b|13 Nov(?:ember)?\b|Nov(?:ember)? 13\b)[^\n]{0,80}\b(?:passed|overdue|missed|expired|lapsed)\b|\bdeadline (?:has|had) (?:already )?(?:passed|expired|lapsed)|\bif (?:that|this|the) (?:date|deadline) has (?:already )?passed'
flags: i
---
