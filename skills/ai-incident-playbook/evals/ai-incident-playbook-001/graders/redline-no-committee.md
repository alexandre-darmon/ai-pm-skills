---
type: regex  # red line: the rollback waits on a committee, meeting or vote; saying the meeting does not decide is fine
pattern: '(?<!\b(?:not|never|no|nothing|don[''’]t|do not|doesn[''’]t|does not|cannot|can[''’]t|won[''’]t|without|instead of|rather than)\b[^\n.]{0,30})\b(?:committee|the meeting|steering group|the group|a vote)\b(?:(?!\b(?:not|never|no|nothing|don[''’]t|do not|doesn[''’]t|does not|cannot|can[''’]t|won[''’]t|without|instead of|rather than)\b|n[''’]t\b)[^\n.]){0,30}\b(?:decides?|should decide|to decide|approves?|to approve|signs? off|votes? on)\b(?!\s+(?:nothing|later)\b)'
flags: i
match: not_contains
weight: 5
---
