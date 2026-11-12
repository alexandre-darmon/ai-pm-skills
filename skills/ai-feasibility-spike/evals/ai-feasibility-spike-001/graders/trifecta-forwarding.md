---
type: regex  # the outbound leg (forwarding) is removed in code: the prototype suggests a route, a handler forwards
pattern: '\b(remov\w*|drop\w*|disabl\w*|strip\w*|no|without)\b[^\n.]{0,40}\b(forward\w*|outbound|send\w*|e-?mails? out)|\b(forward\w*|send\w*)\b[^\n.]{0,60}\b(remov\w*|disabl\w*|by (a )?(human|handler)s?|handlers?|human)\b|\b(suggest\w*|propos\w*)\b[^\n.]{0,30}\b(route|routing|team)'
flags: i
---
