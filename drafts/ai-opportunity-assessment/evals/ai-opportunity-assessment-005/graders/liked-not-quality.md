---
type: regex  # testers liking it is not evidence that answers are correct
pattern: '\b(lik(ed|ing)|satisf\w*|enjoy\w*|positive feedback|thumbs)\b[^\n]{0,100}(\bnot\b|n[’'']t\b|\bnever\b|\bno\b)[^\n]{0,60}\b(correct\w*|quality|accura\w*|evidence|proof|prove\w*|right)\b|(\bnot\b|n[’'']t\b)[^\n]{0,40}\b(evidence|proof|quality)\b[^\n]{0,60}\b(lik(ed|ing)|satisf\w*)'
flags: i
---
