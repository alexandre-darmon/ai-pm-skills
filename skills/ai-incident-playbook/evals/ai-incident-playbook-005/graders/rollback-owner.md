---
type: regex  # one named role owns the rollback (and can act alone), not a group
pattern: '\brollback (owner|authority)\b|\bowner of the (rollback|roll-back|kill[- ]switch)\b|\b(owns?|holds?)\b[^\n.]{0,15}\b(the )?(rollback|roll-back|kill[- ]switch)\b|\b(rollback|roll-back|kill[- ]switch)\b[^\n.]{0,20}\b(owned by|owner)\b|\bowner\b[^\n.]{0,50}\b(rolls? back|flips? the (kill[- ])?switch|switch(es)? (it )?off)\b'
flags: i
---
