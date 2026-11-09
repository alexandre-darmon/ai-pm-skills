I won't write that prompt as planned: if Model X writes the gold answers and then grades Model X, the eval measures its agreement with itself, and the 90% proves nothing.

1. Expected answers are written or approved by claims handlers, each citing the procedure and section it comes from.
2. Ground the questions in real claims traffic: read past policyholder calls and emails, derive dimensions (claim type, stage, channel, style, missing information) and generate from tuples.
3. Add questions not covered by the procedures (a peril the policy excludes, a claim from another product), with "not found, call your adviser" expected.
4. Use a generator and a judge from another model family than Model X, and calibrate the judge on expert labels (TPR and TNR) first.
5. Claims handlers review every question; record the rejection rate.
6. Flag every case as synthetic and state the synthetic share per class in the go-live review.
