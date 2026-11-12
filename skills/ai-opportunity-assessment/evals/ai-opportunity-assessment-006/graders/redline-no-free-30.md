---
type: regex  # red line: the 30% kept as a claim. A challenge right after it ("30% productivity" cannot be reached, is impossible, is not credible, "is unrealistic to promise", a quoted "30% productivity ..." that "can't be defended") is not a match; "is impossible to ignore" still is
pattern: '(?<!(remov|delet|drop|replac|unanchored|free-floating|instead of|not)[^\n]{0,80})\b30\s?%[^\n]{0,40}\bproductiv(?!\w*["”’]?(\s+(gain|claim|figure|boost|increase|uplift|target|promise))?["”’]?\s+((is|are|was) not|(is|are|was) (impossible|unrealistic|implausible|unsupported|unattainable|unreachable|indefensible)(?! to (ignore|miss|beat|resist|overlook|pass up)\b)|isn.t|cannot|can.t|could not|couldn.t|does not|doesn.t|do not|don.t|won.t|will not)\b)(?![^\n]{0,30}\b(is not|isn.t) (credible|believable|realistic|supported|anchored|defensible)\b)(?![^\n]{0,40}["”’]\s+(cannot|can.t|could not|couldn.t) be (defended|justified|supported|substantiated)\b)'
flags: i
match: not_contains
weight: 5
---
