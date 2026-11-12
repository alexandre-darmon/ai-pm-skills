---
type: regex  # a silent provider model or judge change is checked
pattern: 'gen_ai\.response\.model|(provider|model)[^\n]{0,80}\b(silent(ly)?|alias|snapshot|version|updated?|changed?|deprecat)\w*|(silent(ly)?|unannounced)[^\n]{0,60}(model|provider|update|change)|judge[^\n]{0,80}\b(version|model|rubric|changed?|updated?)\b'
flags: i
---
