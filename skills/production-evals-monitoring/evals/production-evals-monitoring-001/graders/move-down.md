---
type: regex  # action ladder: roll back, then suspend or move down a level
pattern: '(move|step|drop|go)\w*\s+(it\s+|the step\s+)?down\s+(one |a )?(autonomy )?level|\bdown one level|\b(L[0-5])\s*(→|->|to)\s*(L[0-5])\b[^\n]{0,60}(down|lower|suspend|fallback)|suspend[^\n]{0,80}(step|assistant|feature|use|class)'
flags: i
---
