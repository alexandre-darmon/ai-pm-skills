---
type: regex  # generation measured on the same stored contexts
pattern: '(fixed|frozen|same|gold|oracle|stored?|saved|held[- ]constant|identical)[^\n]{0,30}(contexts?|passages|pieces|chunks)|\b(frozen|fixed|stored) inputs\b|(contexts?|passages)[^\n]{0,30}(held constant|frozen|fixed)'
flags: i
---
