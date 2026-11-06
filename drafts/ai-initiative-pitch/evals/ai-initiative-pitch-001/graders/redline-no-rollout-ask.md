---
type: regex
pattern: '(?<!\b(?:not|no|never|you|your|[a-z]+n[^a-z\s]t)\b[^\n.]{0,40})\b(ask|asking|request|requesting|seek|seeking|approve|approval|fund|funding|propose|proposing|plan to|need|needs|invest|investing|authori[sz]e|recommend|recommending|we will|we[\x27’]ll)\b(?:(?!\b(?:not|no|never|instead|rather|before|after|until|once|if|whether|later|then|next)\b)[^\n.]){0,100}\b(roll(?:ing)?[- ]?out|deploy\w*)\b(?:(?!\b(?:not|before|after|until|once|if|later)\b)[^\n.]){0,60}\b(all|every|whole|entire|9[, ]?000)\b'
flags: i
match: not_contains
weight: 5
---
