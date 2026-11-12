---
type: regex  # names classes never tried: indirect injection, other customers' data, prompt leak
pattern: 'indirect (prompt )?injection|another customer|other customers[''’]? (data|balances|accounts|transfers)|cross[- ]customer|(data|account) (leak|exfiltrat)\w*|system[- ]prompt (leak|extraction|disclosure)|excessive agency'
flags: i
---
