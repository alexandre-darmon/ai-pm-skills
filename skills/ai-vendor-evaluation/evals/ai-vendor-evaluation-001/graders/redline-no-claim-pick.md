---
type: regex
flags: i
match: not_contains
weight: 3
---
selected vendor\W{0,6}\**\s*(?:vendor )?A\b|(?<!(?:\b(?:not|never|cannot|no|no one|nobody|nothing|whether|if|unless|until|nor|rather than|instead of)\b|n['’]t\b)[^.:;!?\n]{0,60})\b(go with|choose|pick|select|sign with) vendor A\b(?![^.\n]{0,60}\b(only|if|once|after|unless|when)\b)|(?<!(?:\b(?:not|never|cannot|no|no one|nobody|nothing|whether|if|unless|until|nor|rather than|instead of)\b|n['’]t\b)[^.:;!?\n]{0,60})\b97 ?%[^.\n]{0,60}\b(is|looks|seems) (good|enough|sufficient|reliable|credible|solid|convincing)\b
