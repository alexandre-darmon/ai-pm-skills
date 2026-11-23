---
type: regex  # an upstream model change itself is raised as a possible substantial modification (art. 43(4)), not any change in general
pattern: '\bmodel\b[^\n]{0,40}\b(update|change|version|swap)\w*\b[^\n]{0,80}\bsubstantial modification|substantial modification[^\n]{0,80}\n?[^\n]{0,80}\bmodel\b[^\n]{0,40}\b(update|change|version|swap)|43\s*\(4\)[^\n]{0,80}\bmodel\b'
flags: i
---
