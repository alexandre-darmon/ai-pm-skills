---
type: regex  # tuples first, natural-language inputs in a separate step
pattern: 'tuples?[^\n]{0,160}(then|separately|separate|second|step 2|next step)|(separate|second|distinct)[- ](step|pass|stage|prompt|call)[^\n]{0,120}(tuples?|inputs?|questions?|messages?)'
flags: i
---
