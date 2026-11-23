---
type: regex  # rollback made real: rehearsed and timed while the old model exists, or automatic triggers set as numbers
pattern: '\b(rehears\w*|dry[- ]runs?|drills?)\b[^\n]{0,150}\b(rollback|roll(ing)? back)\b|\b(rollback|roll(ing)? back)\b[^\n]{0,150}\b(rehears\w*|dry[- ]runs?|drills?)\b|\b(rollback|roll(ing)? back)\b[^\n]{0,60}\b(tested|verified|exercised|practi[cs]ed|timed)\b|\b(test|verify|exercise|practi[cs]e|time)\w*\s+(the\s+|that\s+|a\s+|your\s+)?(rollback|roll(ing)? back)\b|(automatic|numeric|numerical)[^.\n]{0,20}\b(rollback|roll[- ]?back) (triggers?|thresholds?|criteria|rules?)|\b(rollback|roll[- ]?back) (triggers?|thresholds?|criteria)\b[^.\n]{0,30}\b(as numbers?|numeric|numerical)'
flags: i
---
