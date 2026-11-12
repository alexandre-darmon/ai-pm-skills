---
type: regex  # red line: past its kill date with production data, it stops or gets a dated decision now
pattern: '\b(?:stop|suspend|switch(?:ed)? (?:it )?off|shut(?:ting)? (?:it )?down|turn(?:ed)? (?:it )?off|pause|disable|freeze)\b[^.\n]{0,100}\b(?:now|today|immediately|this week|pending|unless)\b|\b(?:dated|written|formal|explicit|signed) (?:decision|exception|risk acceptance)|\brisk acceptance\b|time[- ](?:limited|boxed|bound) exception'
flags: i
weight: 3
---
