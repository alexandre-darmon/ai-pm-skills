---
type: regex  # not high-risk, with the Annex III employment point checked down to its letter (4(a) or 4(b))
pattern: '^(?=[\s\S]*?(minimal[- ]risk|limited[- ]risk|not (a )?high[- ]risk|isn[''’]?t high[- ]risk|(outside|not (in|listed in|covered by)) (the )?(annex III|high[- ]risk)|no annex III|none of the annex III))[\s\S]*?(\b4\s?\([ab]\)|\b4[ab]\b|point 4[^\n]{0,30}\([ab]\))'
flags: i
---
