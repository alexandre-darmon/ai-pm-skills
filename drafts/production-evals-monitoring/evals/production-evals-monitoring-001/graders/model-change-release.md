---
type: regex  # a provider model change is a release, re-gated offline
pattern: '(model|provider|embedding)[^\n]{0,80}(update|change|version|swap)[^\n]{0,100}(release|re-?run|offline (gate|eval)|golden set|regression)|pin\w*[^\n]{0,40}(model|version|snapshot)|gen_ai\.response\.model'
flags: i
---
