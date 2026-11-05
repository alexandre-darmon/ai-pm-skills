---
type: regex
pattern: '(?<!\b(?:not|never|no)\b[^\n.]{0,30})\b(single|one|shared|same) (index|vector store|collection)\b[^\n.]{0,40}\b(is )?(fine|ok|acceptable|works)\b'
flags: i
match: not_contains
weight: 5
---
