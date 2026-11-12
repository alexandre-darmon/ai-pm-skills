---
type: regex  # a public list is likely already known or patched by the model provider
pattern: 'public (list|set|jailbreaks?|prompts?)[^\n.]{0,120}(known|patched|trained|tuned|stale|contaminat|memori|already|blocked|old|outdated)|contaminat\w*|already (known|patched|blocked|in the training)|well[- ]known|(stale|outdated|old) (jailbreaks?|prompts?|attacks?)|trained (on|against) (them|these|public)|already (tuned|trained|patched|hardened) (against|on)'
flags: i
---
