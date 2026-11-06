---
type: regex  # when the project ends, with a number; rollout gates and a kill switch do not count
pattern: '(stop (condition|criteri|rule)|kill (criteri|condition)|\b(end(ing)?|(stop|abandon|kill|cancel|shut down|retire|withdraw|decommission|sunset|terminate|drop)\w*)( the| this)? (project|feature|initiative|pilot|investment))[\s\S]{0,300}?\d|\d[^\n]{0,200}\b(end(ing)?|(stop|abandon|kill|cancel|shut down|retire|withdraw|decommission|sunset|terminate|drop)\w*)( the| this)? (project|feature|initiative|pilot|investment)'
flags: i
---
