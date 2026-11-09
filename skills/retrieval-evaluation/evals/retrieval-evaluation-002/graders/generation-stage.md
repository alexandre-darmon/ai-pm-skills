---
type: regex  # the diagnosis places the failure in generation
pattern: '(generation|generator|prompt)[^\n]{0,80}(problem|issue|stage|cause|failing|fails|at fault|culprit|side)|(points?|lies|sits|is) (to|in|on) (the )?generation|not (a )?retrieval (problem|issue|failure)|retrieval (is|works|looks) (fine|ok|good|healthy|not the)'
flags: i
weight: 2
---
