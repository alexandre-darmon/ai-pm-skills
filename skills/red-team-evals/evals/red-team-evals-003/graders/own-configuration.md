---
type: regex  # an own campaign on the configured system: our prompt, tools and data
pattern: '(our|your) (own )?(deploy\w*|configur\w*|system prompt|prompts?|tools?|integration|setup|instance|data)[^\n]{0,100}(test|attack|campaign|red[- ]?team)|(test|attack|campaign|red[- ]?team)\w*[^\n]{0,100}(our|your|the) (own |actual |configured |deployed )?(deploy\w*|configur\w*|system prompt|tools?|integration|setup|instance)|(?<!\b(vendor|vendor[''’]s|their|its)\b[^.!?\n]{0,60})\b((our|the|an?) (own )?(campaign|red[- ]?team\w*)|(our|an?) own (test\w*|attacks?))[^.!?\n]{0,60}\b(versions?|system|configuration|build|setup) (we|you) (intend to |will |plan to )?(ship|deploy|release|go live with)\b'
flags: i
---
