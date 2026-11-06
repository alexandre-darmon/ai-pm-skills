---
type: regex
pattern: '(?=[\s\S]*((rights?|licen[sc]\w*|consent|legal basis|allowed?|permi\w+)\b[^\n.]{0,60}\b(data|cases|claims|train\w*)|\b(data|cases|claims|train\w*)\b[^\n.]{0,60}\b(rights?|licen[sc]\w*|consent|legal basis|allowed?|permi\w+)))(?=[\s\S]*(feedback|learning) loop|[\s\S]*flywheel|[\s\S]*static|[\s\S]*new (labels|decisions|outcomes))(?=[\s\S]*\b(lift|holdout|held-out|baseline|measur\w+)\b)'
flags: i
---
