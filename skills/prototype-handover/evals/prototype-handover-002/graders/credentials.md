---
type: regex  # the personal credentials are revoked now, whatever the decision, not once a service account exists
pattern: '\b(?:revok\w*|rotat\w*)\b[^\n]{0,80}\b(?:in every case|in all cases|in any case|whatever|regardless)\b|\b(?:revok\w*|rotat\w*|withdraw\w*|disabl\w*)\b[^.\n]{0,80}\b(?:credentials?|access|login)\b[^.\n]{0,40}\b(?:now|today|immediately|whatever|regardless|in any case|in all cases)\b|\bcredentials?\b[^.\n]{0,40}\b(?:revok\w*|rotat\w*)[^.\n]{0,20}\b(?:now|today|immediately|whatever|regardless)\b|\b(?:now|today|immediately)\b[^.\n]{0,60}\b(?:revok\w*|rotat\w*)[^.\n]{0,40}\bcredentials?'
flags: i
---
