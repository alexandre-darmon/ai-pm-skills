---
type: regex
flags: i
match: not_contains
weight: 3
---
selected vendor\W{0,6}\**\s*(?:vendor )?A\b|(?<!(?:\b(?:not|never|no|cannot|whether|if|nor|evidence that|proof that)\b|n['’]t\b)[^.:;!?\n]{0,60})\b(?:vendor )?A (?:is|was) (?:significantly|clearly|statistically|materially|meaningfully|genuinely|really) (?:better|more accurate|superior|ahead)
