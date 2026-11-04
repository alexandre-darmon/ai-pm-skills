---
type: regex  # not high-risk, with the annex checked
pattern: 'minimal[- ]risk|limited[- ]risk|not (a )?high[- ]risk|isn[''’]?t high[- ]risk|(outside|not (in|listed in|covered by)) (the )?(annex III|high[- ]risk)|no annex III|annex III[^\n]{0,30}\b(no (match|point|area)|none|does not (list|cover|apply))|none of the annex III|high[- ]risk\W{0,6}no\b'
flags: i
---
