---
type: regex
pattern: '(?<!\b(?:not|never|no|non|nothing|neither|nor|cannot|whether|[a-z]+n[^a-z\s]t)\b(?:(?!\b(?:and|but)\b)[^\n.,;:]){0,40})\b(is|are|be|fully|already) compliant\b'
flags: i
match: not_contains
weight: 5
---
