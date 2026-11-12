---
type: regex  # names the classes this setup adds: transaction data of others, ticket misuse, indirect injection
pattern: 'another customer|other customers[''’]? (data|transactions|accounts)|cross[- ](customer|account)|excessive agency|indirect (prompt )?injection|(ticket|dispute)s?[^\n.]{0,50}(abuse|misuse|spam|forg|false|fraud|fake|unauthori[sz]ed)|(misuse|abuse|fraudulent|fake|false)[^\n.]{0,40}(tool|ticket|dispute)'
flags: i
---
