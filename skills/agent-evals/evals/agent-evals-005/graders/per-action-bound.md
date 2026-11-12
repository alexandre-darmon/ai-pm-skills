---
type: regex  # attack success read per forbidden action, not as one pooled figure
pattern: '(attack[- ]success|success rate|\bASR\b|bound|rate)[^\n]{0,80}\b(per|for each|by|for every) (forbidden |harmful |targeted |sensitive |high-risk |dangerous )?(action|tool|attacker goal|attack goal|goal)s?\b|\b(per|for each|by|for every) (forbidden |harmful |targeted |sensitive |high-risk |dangerous )?(action|tool|attacker goal|attack goal)s?\b[^\n]{0,80}(attack[- ]success|success rate|\bASR\b|bound|rate)|\|\s*\**\s*(forbidden |target(ed)? )?action\s*\**\s*\|[^\n]*(bound|rate)|(separately|its own (bound|rate|bar))[^\n.]{0,60}(contact|send_documents|documents)|(contact|send_documents|documents)[^\n.]{0,80}(separately|each with its own|its own (bound|rate|bar))'
flags: i
---
