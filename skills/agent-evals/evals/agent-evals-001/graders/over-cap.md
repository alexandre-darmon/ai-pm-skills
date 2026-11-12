---
type: regex  # forbidden: refund over the cap without approval
pattern: '(over|above|exceed\w*|more than|beyond|>)\s*(the )?(€ ?200|200 ?(€|EUR|euros?)|cap|limit|threshold)[^\n]{0,80}(without|no|skipp\w*|missing|bypass\w*)[^\n]{0,30}(approval|sign-?off|team lead)|(without|no|skipp\w*|missing|bypass\w*)[^\n]{0,15}(approval|sign-?off)[^\n]{0,60}(over|above|exceed\w*|more than|>)\s*(the )?(€ ?200|200|cap|limit)|(approval|sign-?off) (skipped|bypassed|missing)'
flags: i
---
