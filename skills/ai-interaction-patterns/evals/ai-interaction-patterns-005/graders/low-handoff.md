---
type: regex  # the lowest bucket (48 of 100 right) does not answer: it refuses with a next step or hands over to a person
pattern: '(\b48(\.\d+)? ?%|\b48 ?(of|in|/|out of) ?100\b|\b0\.48\b|\b(less|fewer) than half\b|\bunder half\b|\bcoin[- ]?(flip|toss)\b)[^\n]{0,200}\b(hand\w*|escalat\w*|human|person|advis[eo]rs?|staff|colleague|don[’'']?t answer|not answer|withh\w*|declin\w*|refus\w*|rout\w*)|\b(hand\w*|escalat\w*|human|person|withh\w*|declin\w*|refus\w*)\b[^\n]{0,200}(\b48(\.\d+)? ?%|\b48 ?(of|in|/|out of) ?100\b|\b0\.48\b|\b(less|fewer) than half\b)'
flags: i
---
