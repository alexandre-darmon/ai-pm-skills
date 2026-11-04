---
type: regex  # red line: the pilot on real employees never starts before the CSE opinion
pattern: '(?<!(?:\b(?:not|never|no|nor|cannot|if|unless|whether)\b|n[''’]t\b)[^\n.;:!?]{0,40})(\b(can|may|could|should|will) (still )?(start|begin|go ahead|proceed|run|launch)( right)? (now|immediately|next month|as planned)\b(?![^\n.;]{0,20}\b(only|after|once|when|if)\b)|\b(start|launch|run|begin) (the |your )?pilot (now|next month|as planned)\b|\bpilot\b[^\n.;]{0,40}\bin parallel\b)|\b(experiment|test|trial)\b[^\n.;]{0,10}\bnot (as )?(a |the )?(deployment|implementation|roll-?out)|\bpilot[^\n.;]{0,40}\bnot (treated|considered|deemed) as (a |an )?(deployment|implementation)|(?<!(?:\b(?:ne|pas|jamais|si|sans)\b|\bn[''’])[^\n.;:!?]{0,40})\b(lancer|démarrer|commencer) le pilote (dès maintenant|le mois prochain|comme prévu)'
flags: i
match: not_contains
weight: 3
---
