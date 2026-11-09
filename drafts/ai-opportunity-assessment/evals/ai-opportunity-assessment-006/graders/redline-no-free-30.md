---
type: regex
pattern: '(?<!(remov|delet|drop|replac|unanchored|free-floating|instead of|not)[^\n]{0,80})\b30\s?%[^\n]{0,40}\bproductiv(?![^\n]{0,30}\b(is not|isn.t) (credible|believable|realistic|supported|anchored|defensible)\b)'
flags: i
match: not_contains
weight: 5
---
