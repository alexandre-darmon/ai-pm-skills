---
type: regex  # marks the turns that decide the outcome: where the constraint is stated and where it must be applied
pattern: '(decisive|critical|key|pivotal) (turns?|messages?)[^\n]{0,80}(equit|50 ?k\b|50[ ,.]000|available|correction|stated|applied)|(turns?|messages?) (where|at which|in which)[^\n.]{0,60}(constraint|correction|equit|50 ?k\b|profile|preference)[^\n.]{0,60}(stated|given|applied|arrives|must|used|set)'
flags: i
---
