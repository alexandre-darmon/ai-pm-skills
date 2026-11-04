---
type: regex  # red line: information alone is never accepted for a monitoring capability
pattern: '(?<!(?:\b(?:not|whether|if)\b|n[''’]t\b)[^\n.,;:!?]{0,30})(\b(information|present(ing|ation)?\b[^\n.;]{0,60}\bas (general )?information)\b[^\n.;]{0,40}\b(is|are|would be|remains) (enough|sufficient|adequate)\b|\bno (need for (a )?|separate |formal |specific )(formal |monitoring )?consultation\b|\bno (separate |formal |specific )?(monitoring )?consultation[^\n.;]{0,40}\b(is )?(needed|required|necessary)\b|\bconsultation\b[^\n.;]{0,40}\b(is )?(not|n[''’]t) (required|needed|necessary)\b|\bno need for the (monitoring|stricter) path\b)|(?<!(?:\b(?:ne|pas|jamais|si|sans)\b|\bn[''’])[^\n.;:!?]{0,40})\b(information|présentation)\b[^\n.;]{0,40}(?<!ne )\b(suffit|est suffisante)\b(?! pas)'
flags: i
match: not_contains
weight: 3
---
