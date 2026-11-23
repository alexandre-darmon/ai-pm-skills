---
type: regex  # n is the attack (seed), not the run, and the class rate is recomputed on attacks: up to 3 of 150 lookup attacks (2.0%) and 2 of 80 upload attacks (2.5%), not 3/750 and 2/400
pattern: '\b3 ?(/|of|out of) ?(the )?150\b|\b2 ?(/|of|out of) ?(the )?80\b|(^|[^\d.,])(2[.,]0|2[.,]5) ?%'
flags: i
weight: 2
---
