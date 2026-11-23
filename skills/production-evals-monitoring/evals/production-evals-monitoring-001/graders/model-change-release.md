---
type: regex  # a silent provider model change is detected: alert when the model that answered (gen_ai.response.model) changes, not only "pin the version"
pattern: 'gen_ai\.response\.model|\b(alert|page|flag|notify|detect|warn)\w*\b[^\n]{0,80}\b(model (that|which) (answered|responded|served)|answering model|(served|returned|responding) model|model (name|id|version) (returned|in the response|reported))|\bmodel (that|which) (answered|responded)\b[^\n]{0,60}\b(chang|differ)|\bmodel (id|name|version|field)s?\b[^\n]{0,40}\b(response|returned|reported|served)\b[^\n]{0,80}\b(alert|page|flag|differs?|mismatch\w*|changes?)\b|\b(alert|page|flag)\w*\b[^\n]{0,60}\b(response|returned|served)[’'']?s? model\b'
flags: i
---
