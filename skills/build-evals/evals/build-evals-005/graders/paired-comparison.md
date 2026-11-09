---
type: regex  # old and new on the same cases, paired, before the swap
pattern: '\bpaired\b|same (\d+ )?(cases|invoices|set|documents)[^.\n]{0,60}(old|new|both|current|candidate)|(old|current) and (the )?new[^.\n]{0,60}same (\d+ )?(cases|invoices|set)|2\s?√\s?d'
flags: i
---
