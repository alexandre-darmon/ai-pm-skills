---
type: regex  # registered at its tier (or as a team tool / EUC) as the outcome, not just "put it on an inventory"
pattern: '\bregist\w*\b[^.\n]{0,40}\b(?:at (?:EUC )?tier|as an? (?:\w+ ){0,2}(?:tool|EUC)|tier (?:[12]|one|two)|EUC|end[- ]user[- ]computing|ICT asset)|\b(?:tier (?:[12]|one|two)|team tool)\b[^.\n]{0,40}\bregist'
flags: i
---
