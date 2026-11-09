Not yet. The 94% is measured on the same 60 summaries you tuned the prompt on, four of them pasted in as examples: it describes the tuning, not the judge.

1. Split before going further. Keep the 60 as the few-shot pool and dev split. Have the senior handler label a fresh test split of about 150 summaries never used for tuning, enriched with likely omissions so it holds at least 50 missed-exclusion summaries.
2. With only 9 fails today, TNR cannot be estimated: even 9 caught out of 9 only shows TNR ≥ 70%.
3. Set and sign TPR and TNR targets before scoring the test split: TPR ≥ 0.80 and TNR ≥ 0.85, since a missed exclusion leads to a wrong payout.
4. Report TPR and TNR with their Wilson intervals, not agreement: with 85% fine summaries, a judge that passes everything agrees 85%.
5. The weekly pass rate goes into the pack as a corrected pass rate, (observed + TNR − 1) ÷ (TPR + TNR − 1), with its interval, never the judge's raw rate.
6. Pin the judge model version and re-test on any change of model or prompt.
