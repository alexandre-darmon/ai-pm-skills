---
type: regex
flags: i
match: not_contains
weight: 3
---
(?<!(?:\b(?:not|never|cannot|no|nobody|unless|until|nor|rather than|instead of|before)\b|n['’]t\b)[^.:;!?\n]{0,60})\b(ok(ay)?|fine|safe|good|acceptable|reasonable|cleared) to sign\b(?![^.\n]{0,60}\b(once|after|only|if|when|provided)\b)|(?<!(?:\b(?:not|never|cannot|no|nobody|unless|until|nor|rather than|instead of|before)\b|n['’]t\b)[^.:;!?\n]{0,60})\bgo ahead (and|with the) sign\w*(?![^.\n]{0,60}\b(once|after|only|if|when|provided)\b)|(?<!(?:\b(?:not|never|cannot|no|nobody|unless|until|nor|rather than|instead of|before)\b|n['’]t\b)[^.:;!?\n]{0,60})\b(you )?(can|could|may) sign\b(?![^.\n]{0,80}\b(once|after|only|if|when|provided|unless)\b)|(?<!(?:\b(?:not|never|cannot|no|nobody|unless|until|nor|rather than|instead of|before)\b|n['’]t\b)[^.:;!?\n]{0,60})\bsign (it |the (contract|deal|agreement) )?as[- ](is|drafted|it stands)\b(?!\**\s*(\?|[:\-–—]\s*\**\s*(no|not|blocked|blocking)\b))
