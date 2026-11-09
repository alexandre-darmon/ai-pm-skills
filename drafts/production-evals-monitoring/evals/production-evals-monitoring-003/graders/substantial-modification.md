---
type: regex  # a provider model change may be a substantial modification, or at least a release
pattern: 'substantial modification|43\s*\(4\)|new conformity assessment|(model|provider)[^\n]{0,80}\b(update|change|version|swap)\w*[^\n]{0,80}\b(release|re-?run|offline (gate|eval)|re-?assess)'
flags: i
---
