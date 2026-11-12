---
type: regex  # every memo of the window is read, not only the three reported
pattern: '\b(all|every|each)\b[^\n.]{0,40}\b(memos?|drafts?|outputs?)\b[^\n.]{0,60}\b(since|window|period|last|from|produced|drafted)\b|\b(not (just|only)|beyond|more than|other than) (the |those )?(3|three)\b'
flags: i
---
