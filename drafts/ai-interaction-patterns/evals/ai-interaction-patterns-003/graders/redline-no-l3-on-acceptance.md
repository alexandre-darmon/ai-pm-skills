---
type: regex  # red line: acceptance rate is not a gate to stop one-by-one validation
pattern: '\b(not|no|never|don[''’]?t|hold off|too early|premature|keep)\b[^.\n]{0,80}\b(L3|one[- ]by[- ]one validation|validat\w* (every|each))|\bL3\b[^.\n]{0,60}\b(not yet|premature|too early|wait|until|is not justified|cannot)\b|(acceptance|97 ?%)[^.\n]{0,60}\b(is not|isn[''’]t|does not|doesn[''’]t)\b[^.\n]{0,30}(gate|evidence|proof|show)'
flags: i
weight: 3
---
