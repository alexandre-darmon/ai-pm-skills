---
type: regex  # the change of definition is logged with its date and reason (it goes to build-evals), not just mentioned; "when and why" counts only next to a change or definition noun
pattern: '\bdrift log\b|\b(log|record|document|write (down|up)|note)\w*\b[^\n.]{0,60}\b(revision|change|changed|definition|criteria|rule)s?\b[^\n.]{0,80}\b(date|dated|reason|why)\b|\b(revision|change|changed|definition|criteria|rule)s?\b[^\n.]{0,60}\b(date|when)\b[^\n.]{0,20}\b(and|,|\+) (the )?(reason|why)\b'
flags: i
---
