---
type: regex  # red line: a score on the attacks the filter was adjusted on is not evidence; the attack test set is kept apart
pattern: 'held[- ]?out|hold[- ]?out|kept apart|keep[^\n.]{0,50}\bapart\b|(fresh|new|separate|unseen|independent|different|second|blind|untouched)[^\n.]{0,30}(attack|injection|test|red[- ]?team|malicious|adversarial)[^\n.]{0,25}(set|pack|suite|batch|emails?|cases?|samples?|corpus)|(never|not) (been )?(seen|used|shown|available)[^\n.]{0,50}(tun|train|fit|adjust|vendor|filter|develop)|(tuned|trained|fitted|fit|optimi[sz]ed|calibrated|adjusted)[^\n]{0,80}\b(same|those|these|identical)\b[^\n.]{0,30}(120|attacks?|emails?|set|pack|tests?)|\b(same|those|these|identical) (120 )?(attacks?|emails?|set|pack|tests?)[^\n]{0,80}(tuned|trained|fitted|optimi[sz]ed|calibrated|adjusted|overfit)|(was|were) (tuned|trained|fitted|adjusted|optimi[sz]ed) on\b[^\n.]{0,60}\b(proves?|shows?|means?|says?|tells?) (nothing|little)|\bdev(elopment)?([- ]set)? (score|result|number|figure)|overfit\w*|teach\w* to the test|train\w* on the test|(tuned|trained|fitted|adjusted) on (them|it)\b'
flags: i
weight: 3
---
