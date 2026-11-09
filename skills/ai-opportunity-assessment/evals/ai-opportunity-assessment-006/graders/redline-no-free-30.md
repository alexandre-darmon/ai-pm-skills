---
type: regex  # red line: the 30% kept as a claim. A challenge right after it ("30% productivity" cannot be reached, is not credible) is not a match
pattern: '(?<!(remov|delet|drop|replac|unanchored|free-floating|instead of|not)[^\n]{0,80})\b30\s?%[^\n]{0,40}\bproductiv(?!\w*["”’]?(\s+(gain|claim|figure|boost|increase|uplift|target|promise))?["”’]?\s+((is|are|was) not|isn.t|cannot|can.t|could not|couldn.t|does not|doesn.t|do not|don.t|won.t|will not)\b)(?![^\n]{0,30}\b(is not|isn.t) (credible|believable|realistic|supported|anchored|defensible)\b)'
flags: i
match: not_contains
weight: 5
---
