---
type: regex  # the vendor's claim does not cover the deployer's duties
pattern: '(vendor|provider|supplier)[^\n]{0,120}(does not|doesn[''’]t|do not|don[''’]t|cannot|can[''’]t|won[''’]t|not)[^\n]{0,60}(cover|transfer|replace|discharge|relieve|remove|apply to you|your (duties|obligations))|(your|our) (own )?(deployer )?(duties|obligations)[^\n]{0,80}(remains? (yours|with you|your own|in place)|stays? (yours|with you)|regardless|whatever)|(duties|obligations)[^\n]{0,60}\b(are (still )?yours|(sit|rest|stay|remain)s? with you)\b|\bstill (carry|bear|own|hold)\b[^\n]{0,40}(duties|obligations)'
flags: i
---
