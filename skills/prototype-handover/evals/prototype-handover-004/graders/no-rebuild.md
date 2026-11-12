---
type: regex  # a rebuild is not what tier 2 asks for
pattern: '\bno (?:\w+ ){0,2}rebuil|(?:not|n.t) (?:need|require)\w*[^.\n]{0,40}rebuil|\bnot (?:a )?rebuil|rebuil\w*[^.\n]{0,40}\b(?:not (?:needed|required|necessary|justified|warranted)|unnecessary|overkill|disproportionate)|without (?:a )?rebuil|instead of (?:an? )?(?:IT |full )?rebuil|\b(?:don.t|do not|not|no need to)\s+(?:(?:hand|send|give)\s+it\s+(?:\w+\s+){0,2}(?:to|for)\s+(?:\w+\s+){0,4}|(?:start|commission|launch|request)\s+(?:an?\s+|the\s+)?(?:[\w-]+\s+){0,2}|ask\s+\w+\s+to\s+)rebuil'
flags: i
---
