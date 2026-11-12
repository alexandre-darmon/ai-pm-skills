No: do not send the spike report as validation evidence, and do not cite 92.5% as the system's accuracy. A spike number is never release evidence.

Why: 37 of 40 is 92.5%, but the 95% interval is about 80% to 97%, so the 90% bar is not demonstrated. The 40 complaints were written by the team, not sampled from production traffic. The definition of correct changed twice during the run (criteria drift), so the bar was judged against moving criteria. And the harness was throwaway, not the engineering build.

What the spike does support: a go to PRD for this classifier.

What build-evals must do before go-live at L3: real complaints sampled from production traffic per category; each category sized for the margin between its expected rate and the 90% bar, since it meets the bar only when its lower bound does: expecting 92.5%, that is about 430 real complaints per category, or a lower bar signed before the run; the definition of correct frozen from the spike's drift log; a private holdout; thresholds signed before the run; run on the engineering build, gated by release-to-production with a shadow run.

Paragraph for model risk: "The feasibility spike (37 of 40 synthetic cases, interval about 80% to 97%) supported a decision to invest; it is not validation evidence. The validation pack will come from an eval suite sampled from production traffic, sized per category, with frozen criteria, run on the engineering build. We will send it before the March go-live."
