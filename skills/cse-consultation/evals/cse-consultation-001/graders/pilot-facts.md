---
type: regex  # asks, as a fact for legal, whether the pilot's output reaches real clients
pattern: '\b(whether|if|does|do|will|would|can)\b[^\n]{0,40}(outputs?|drafts?|repl(y|ies)|answers?|letters?|emails?)[^\n]{0,40}\b(reach(es)?|go(es)? (out )?to|(sent|shown|delivered) to|seen by|received by)\b[^\n]{0,30}\b(clients?|customers?)\b|\b(si|est-ce que)\b[^\n]{0,40}(sorties?|brouillons?|réponses?)[^\n]{0,40}(parvien\w*|arriv\w*|envoy\w*)[^\n]{0,30}\bclients?\b'
flags: i
---
