---
type: regex
pattern: '(?<!\b(?:not|never|no|don[\''’]t|do not|cannot|without)\b[^\n.]{0,30})\b(spot[- ]check|asking a few|a few questions by hand|manual check)\w*[^\n.]{0,30}\b(is|are|will be)? ?(enough|sufficient|fine)\b'
flags: i
match: not_contains
weight: 5
---
