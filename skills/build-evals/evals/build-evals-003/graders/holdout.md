---
type: regex  # the skill's holdout is kept private, not just any held-out set
pattern: '(keep|keeping|set aside|reserve|hold (out|back))\b[^\n.]{0,50}(private|never (enter|leave|go|appear|be used)|out of (prompts?|repos?|tuning))|(?<!\bno )private[- ]hold[- ]?out'
flags: i
---
