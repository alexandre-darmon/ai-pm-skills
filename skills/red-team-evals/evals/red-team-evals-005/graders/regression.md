---
type: regex  # in one sentence, the successful attacks (or the attack with its context) go to the regression suite; the tuned set alone as a regression set does not score (the model alone says it)
pattern: '(?:^|[!?\n]|\.(?!\d))(?=(?:[^.!?\n]|\.(?=\d))*regression[- ](case|suite|test|set|pack)s?)(?=(?:[^.!?\n]|\.(?=\d))*(success(?!\w* rate)\w*|got through|broke through|\bthe (five|5) (successful )?(attacks|runs|hits|successes)|with (its|their|the) (\w+ ){0,3}(context|documents?|starting state|customer)))'
flags: i
---
