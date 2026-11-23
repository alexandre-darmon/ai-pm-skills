---
type: regex  # the salary disclosure ranks high whatever its count, and its exposure goes to the DPO or counsel as a question, not into a frequency or a euro figure
pattern: '(salary|confidential|disclos\w*|privacy)[^\n]{0,200}\b(DPO|counsel|lawyers?|legal (team|department)|data protection officer|privacy (office|officer|team))\b|\b(DPO|counsel|data protection officer)\b[^\n]{0,120}(salary|confidential|disclos\w*|privacy)'
flags: i
---
