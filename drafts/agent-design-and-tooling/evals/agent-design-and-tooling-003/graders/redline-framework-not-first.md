---
type: regex
pattern: '(?<!\b(?:not|never|no|don[\''’]t|do not|cannot|without)\b[^\n.]{0,30})\b(pick|choose|go with|start with|recommend)\w*\b[^\n.]{0,15}\b(LangGraph|CrewAI)\b'
flags: i
match: not_contains
weight: 5
---
