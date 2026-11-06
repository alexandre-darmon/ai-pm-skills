---
type: regex  # a forbidden action is taken out of the agent's reach, not only asked of the prompt
pattern: '\bnever\b[^\n.]{0,160}\b(tools?|tool ?set|credentials?|permissions?|endpoints?)\b|\b(removed|absent|excluded|left out|withheld) from\b[^\n.]{0,40}\b(tools?|tool ?set|credentials?|permissions?)\b|\b(has|have|gets?|given|with) no (tool|endpoint|credential|permission|write access)|\bnot exposed\b[^\n.]{0,40}\b(tool|agent|model)|\bcredentials?\b[^\n.]{0,20}\bscoped\b|\bscoped\b[^\n.]{0,20}\bcredentials?\b|\bonly the\b[^\n.]{0,30}\btools?\b[^\n.]{0,20}\bexposed\b|\b(minimum|least)[- ](permission|privilege)'
flags: i
---
