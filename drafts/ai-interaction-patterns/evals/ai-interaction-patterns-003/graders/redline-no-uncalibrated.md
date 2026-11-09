---
type: regex  # red line: the uncalibrated score shown. "Once calibrated, show the score" and "keep the score hidden" are not a match
pattern: '(?<!\b(?:not|never|no|don[\''’]t|do not|cannot|without|(?:if|once|when|after)\b[^\n.]{0,25}calibrat\w*)\b[^\n.]{0,30})\b(show|display|keep)\b[^\n.]{0,20}\b(92\s?%|the score|confidence)\b(?![^\n.]{0,30}\b(once|after|until|only if|hidden|off)\b)'
flags: i
match: not_contains
weight: 5
---
