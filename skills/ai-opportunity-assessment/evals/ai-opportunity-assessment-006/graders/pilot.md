---
type: regex  # the ask becomes a pilot that carries a stop condition with a number or a bracket to settle
pattern: '^(?=[\s\S]*?\bpilot\b)[\s\S]*?(\b(stop|halt|kill|end)s?\b[^\n]{0,20}\b(if|when|unless)\b|\b(stop|kill|exit)[- ](condition|criteri\w+|rule)s?\b)[^\n]{0,160}(\d|\[[^\]\n]+\])'
flags: i
---
