---
type: regex  # red line: the spike score is never accepted as release or go-live evidence, nor said to stand for the build (reading it as the baseline, floor or an indicative figure is fine)
pattern: '(?<!(?:\b(?:not|never|cannot|no|nor|whether|if|unless|until|before)\b|n.t\b)[^.:;!?\n]{0,60})(?:\b95\s?%|\b38/40|\b38 of 40|\bprototype (?:result|score)s?)(?:(?!n.t\b|\bnot\b)[^.\n]){0,60}?\b(?:(?:can|may|could|is fine to|is enough to)\s+(?:be\s+)?(?:used|go|serve|stand|count|reused|relied on|kept)|will\s+(?:be\s+)?(?:used|serve|stand|count|reused|relied on))\b(?![^.\n]{0,40}\b(?:baseline|floor|indicative|only as|prototype result)\b)|(?<!(?:\b(?:not|never|no|nor|whether|if|unless|until)\b|n.t\b)[^.:;!?\n]{0,60})\bprototype (?:result|score)s? (?:stands|still stands|holds)\b'
flags: i
match: not_contains
weight: 2
---
