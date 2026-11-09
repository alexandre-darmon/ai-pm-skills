---
type: regex  # why the raw rate is off: wrong fails of good memos outweigh wrong passes of bad ones
pattern: 'understat\w*|underestimat\w*|under-?report\w*|too (low|harsh|strict|pessimistic)|biased (down\w*|low)|pessimistic|(lower|less) than the (true|real|actual)|below the (true|real|actual)'
flags: i
---
