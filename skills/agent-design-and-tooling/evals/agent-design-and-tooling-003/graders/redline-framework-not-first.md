---
type: regex  # red line: no framework pick up front (first 600 characters), and no unconditional pick anywhere
pattern: '(?<!\b(?:not|never|no|don[\''’]t|do not|cannot|without)\b[^\n.]{0,30})\b(?:pick|choose|go with|start with|recommend)\w*\b[^\n.]{0,15}\b(?:LangGraph|CrewAI)\b(?!\s*[,—–-]?\s*(?:but )?(?:only |just )?(?:if|when|once|where|after|provided|in case)\b)|^[\s\S]{0,600}?(?<!\b(?:not|never|no|don[\''’]t|do not|cannot|without)\b[^\n.]{0,30})\b(?:pick|choose|go with|start with|recommend)\w*\b[^\n.]{0,15}\b(?:LangGraph|CrewAI)\b'
flags: i
match: not_contains
weight: 5
---
