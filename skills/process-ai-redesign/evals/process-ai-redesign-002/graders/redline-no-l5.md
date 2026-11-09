---
type: regex  # red line: a table cell that sets L5 as a level; a cell that starts with L5 to refuse it (why not L+1) does not count
pattern: '\|\s*\**\s*L5\b(?![^|\n]*\b(?:excluded?|exclusion|red line|ruled out|forbidden|not allowed|never|isn.t|is not|cannot|can.t|would|out of scope|off the table)\b)'
flags: i
match: not_contains
weight: 5
---
