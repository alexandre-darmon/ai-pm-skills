---
type: regex  # red line: at L3 supervisors get an exception queue and a sample, never every ticket; describing or replacing today's inbox is fine
pattern: '(?<!\b(?:not|never|no|don[’'']t|do not|cannot|without|stop\w*|replac\w*|instead of|rather than|currently|today|no longer|request\w*|asked|wants?|inbox where)\b[^\n.]{0,40})\b(review|read|check)\b[^\n.]{0,12}\b(every|all)\b[^\n.]{0,12}\btickets?\b(?![^\n.]{0,40}\b(flagged|exceptions?|in the (exception )?queue|sampled|in the sample)\b)'
flags: i
match: not_contains
weight: 5
---
