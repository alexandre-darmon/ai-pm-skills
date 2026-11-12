---
type: regex  # the expert reads before any model suggestion
flags: i
---
anchor\w*|(expert|handler|reviewer)s?[^\n]{0,40}(read|label|judge|decide)s?[^\n]{0,20}(first|before|independently|blind)|(before|without)[^\n]{0,40}(seeing|any|the)[^\n]{0,20}(model|GPT|LLM|AI)[^\n]{0,20}(suggest|score|label|opinion)|\b(no|remove|drop|never)\b[^\n]{0,30}(model|GPT|LLM|AI)[- ]?(suggest|pre|score|label)
