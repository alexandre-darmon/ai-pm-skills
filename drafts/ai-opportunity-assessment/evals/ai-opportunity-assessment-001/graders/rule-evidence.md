---
type: regex
pattern: '\b(?:rule|rules|query|filter|coverage|criteria)\b[^\n]{0,120}(?:\bunmeasured\b|\bnot (?:yet )?(?:been )?(?:measured|tested|checked|verified)\b|\bnot a measurement\b|\bno sample\b|\b\d+\s*(?:of|out of)\s*\d+\b)|(?:\bunmeasured\b|\bnot (?:yet )?(?:been )?(?:measured|tested|checked|verified)\b|\bnot a measurement\b|\bno sample\b|\b\d+\s*(?:of|out of)\s*\d+\b)[^\n]{0,120}\b(?:rule|rules|query|filter|coverage|criteria)\b'
flags: i
---
