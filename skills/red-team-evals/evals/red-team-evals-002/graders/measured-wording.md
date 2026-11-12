---
type: regex  # rewrites the sentence as a measured result
pattern: '\b0 ?(successes|successful attacks?)? ?(of|out of|in|/) ?(the )?50\b|\bzero (successful )?(attacks?|successes)[^\n.]{0,40}\b50\b|\bno success(ful attack)?s? in 50\b|\b50 (direct )?(jailbreak )?(prompts?|attempts?|attacks?)[^\n.]{0,60}(upper bound|up to|95 ?%)'
flags: i
---
