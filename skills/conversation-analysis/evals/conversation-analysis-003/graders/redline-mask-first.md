---
type: regex  # red line: masking comes before any model call
pattern: '(mask|pseudonymi[sz]|redact|anonymi[sz])\w*[^\n]{0,100}(before|prior to) (any |the |a |sending |each )?(model|LLM|call|classif|taxonom|label|send|annotat|processing)|(mask|pseudonymi[sz]|redact|anonymi[sz])\w*[^\n]{0,30}\bfirst\b|(mask|pseudonymi[sz]|redact|anonymi[sz])\w*[^\n]{0,60}\b(blocks?|gates?)\b|nothing[^\n]{0,60}until[^\n]{0,60}(mask|pseudonymi[sz]|redact|anonymi[sz])\w*|(before|until)[^\n]{0,80}(mask|pseudonymi[sz]|redact|anonymi[sz])\w*[^\n]{0,30}(done|complete|checked|in place|passe)|step 0[^\n]{0,40}(mask|pseudonymi[sz]|redact|anonymi[sz])\w*'
flags: i
weight: 2
---
