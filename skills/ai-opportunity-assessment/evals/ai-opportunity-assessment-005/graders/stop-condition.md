---
type: regex  # a stop condition with a number or a bracket to settle, not only a success criterion
pattern: '\b(stop\w*|kill|halt|terminate|abandon|discontinue|wind down|shut down)\b[^\n]{0,60}\b(if|when|unless|below|under|fewer|less than)\b[^\n]{0,160}(\d|\[[^\]\n]+\])|\b(if|when|should)\b[^\n]{0,160}(\d|\[[^\]\n]+\])[^\n]{0,120}\b(stop\w*|kill|halt|terminate|abandon|discontinue|wind down|shut down)\b'
flags: i
---
