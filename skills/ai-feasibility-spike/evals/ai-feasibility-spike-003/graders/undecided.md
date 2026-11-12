---
type: regex  # the disputes interval straddles the 75% stop line: undecided (or inconclusive), neither a pass nor a drop
pattern: '\bundecided\b|\binconclusive\b|straddl\w*|\b(lower (bound|end|limit)|low end|interval|range)\b[^\n.]{0,80}\b(below|under|beneath|crosses|spans|includes|reaches|dips)\b[^\n.]{0,30}(stop line|75 ?%|0[.,]75|drop line|(drop|stop) threshold)|\bas low as 6\d([.,]\d)? ?%[^\n.]{0,40}\b(below|under)\b[^\n.]{0,40}75 ?%|(stop line|drop line|75 ?%)[^\n.]{0,40}\b(inside|within) (the |its |that )?(interval|range)'
flags: i
---
