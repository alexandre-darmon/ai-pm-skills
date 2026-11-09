---
type: regex
pattern: '(?<!\b(?:not|never|no|don[\''’]t|do not|cannot|without)\b[^\n.]{0,30})\b(send|issue|rely on)\b[^\n.]{0,15}\bmemo\b[^\n.]{0,30}\b(enough|sufficient|reassure|explain)\b'
flags: i
match: not_contains
weight: 5
---
