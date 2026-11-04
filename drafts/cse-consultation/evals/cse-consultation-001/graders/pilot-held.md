---
type: regex  # the pilot waits for the CSE opinion
pattern: 'pilot[^\n]{0,120}\b(after|once|only when|until|must wait for|not before|(cannot|can[''’]t|must not|mustn[''’]t|should not|may not|do not|don[''’]t|never) (start|begin|launch|run|go ahead|proceed)[^\n]{0,20}\bbefore)\b[^\n]{0,60}(opinion|avis|end of the delay)|(do not|don[''’]t|never|cannot|can[''’]t|must not|no)\b[^\n]{0,40}pilot[^\n]{0,80}\bbefore\b[^\n]{0,60}(opinion|avis)|pilot[^\n]{0,100}\b(counts as|is treated as|is deemed( to be)?|qualifies as|amounts to|constitutes|is)\b (itself )?(a |an |the )?(first |de facto )?(deployment|implementation|mise en (œ|oe)uvre|roll-?out)|(opinion|avis|consultation (must be |is )?(completed|closed|finished|over))[^\n]{0,60}\b(before|prior to|ahead of) (the |any )?pilot|pilote[^\n]{0,80}\b(constitue|vaut|est)\b (une )?(première )?mise en (œ|oe)uvre|pilote[^\n]{0,60}\b(après|pas avant)\b[^\n]{0,40}\bavis'
flags: i
---
