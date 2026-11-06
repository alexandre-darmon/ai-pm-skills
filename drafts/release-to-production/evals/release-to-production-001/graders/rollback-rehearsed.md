---
type: regex
pattern: '\b(rehears\w*|dry[- ]runs?|drills?)\b[\s\S]{0,250}\b(rollback|roll(ing)? back)\b|\b(rollback|roll(ing)? back)\b[\s\S]{0,250}\b(rehears\w*|dry[- ]runs?|drills?)\b|\b(rollback|roll(ing)? back)\b[^\n]{0,60}\b(tested|verified|exercised|practi[cs]ed|timed)\b|\b(test|verify|exercise|practi[cs]e|time)\w*\s+(the\s+|that\s+|a\s+|your\s+)?(rollback|roll(ing)? back)\b'
flags: i
---
