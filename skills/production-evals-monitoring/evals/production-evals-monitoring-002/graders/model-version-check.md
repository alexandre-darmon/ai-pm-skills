---
type: regex  # a silent provider change is checked on the model that actually answered in the traces, or met by pinning and re-running the gate (not only a changelog or alias question)
pattern: 'gen_ai\.response\.model|\bmodel( ID| id| name| version)? (that|which) (actually )?(answered|responded|served)|\bpin(s|ned|ning)?\b[^\n]{0,60}\b(model|version|snapshot)\b[^\n]{0,80}\b(re-?run|re-?test|offline|golden|test set|gate|eval)'
flags: i
---
