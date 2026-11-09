Not yet: three memos do not verify the fix. Do not ship it tonight.
1. Error-analysis note: read every memo drafted since the faulty version went live, not only the three, and name the failure mode and the classes it hits.
2. Add the wrong memos as regression cases to the golden set; they must fail on the current version.
3. Run the fix on the full suite, per class, against the previous version on the same cases.
4. Record the incident, the fix and the eval delta in the model card changelog. Then the fix ships.
