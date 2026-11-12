---
type: regex  # red line: engineering is never told it can skip re-running the frozen suite on its build ("from scratch" in the same sentence, or a rerun of the suite on the engineering build named next, is fine)
pattern: '(?<!\b(?:so that|wants?|sponsor.s|idea that|says?|said|claims?|argues?|suggests?|thinks?|believes?|hopes?)\b[^.\n]{0,60})\bengineering (?:does not|doesn.t|need not|won.t|will not) (?:need|have) to (?:re-?test|re-?run|redo|repeat)\b(?![^.\n]{0,30}\bfrom scratch\b)(?![^\n]{0,120}\b(?:they|engineering)\s+(?:do\s+|still\s+|will\s+|must\s+|should\s+|need to\s+|have to\s+|do have to\s+)?(?:re-?)?run\b[^.\n]{0,40}\b(?:questions|suite|cases|set)\b[^.\n]{0,60}\b(?:gateway|engineering build|newer? model|rebuil\w*|platform))'
flags: i
match: not_contains
weight: 2
---
