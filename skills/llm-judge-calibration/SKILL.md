---
name: llm-judge-calibration
description: Check if an LLM judge can be trusted on a failure mode and correct the pass rate it reports. Use for "can we use LLM-as-judge?", a judge's agreement with experts, a judge change or drift.
license: CC-BY-4.0
metadata:
  stage: "evaluate"
  version: "0.2.0"
  status: "tested"
  eval_threshold: "0.80"
  autonomy_relevant: "true"
  depends_on: "error-analysis"
  feeds: "build-evals, production-evals-monitoring, release-to-production"
  sources: "husain-shankar-evals, shankar-validators, zheng-llm-judge, yan-llm-evaluators, rogan-gladen, cohen-kappa, wilson-interval, efron-bootstrap, anthropic-evals, own-golden-sets"
---

# llm-judge-calibration

## When to use
- Someone asks "can we use an LLM-as-judge for this?", or a judge is about to gate a release or a level change (references/autonomy-ladder.md).
- A judge is defended by its agreement with experts: "it agrees 85% with the experts, is that good enough?"
- A judge prompt is being written or revised, or the judge's model or prompt changes.
- A judge scores production samples and its pass rate is read as the quality figure, or drift is suspected.
- Do not use before the failure modes are known: with traces and no criterion yet, start with `error-analysis`.
- Do not use to design the whole eval plan (classes, set, thresholds, baseline) or to choose a model on a suite whose judge is already validated: that is `build-evals` or `model-selection`.

## Inputs
Mandatory: the failure mode the judge grades and its written pass/fail criterion; the expert labels (who labelled, how many, how many pass and how many fail) and what each label was used for (writing the prompt, few-shot examples, testing); the judge's verdicts on the labelled answers, or the counts; the decision the judge feeds (release gate, level gate, production rate, dashboard).
Ask if missing: judge model and version, prompt version, the judge's pass rate on unlabelled traffic with its sample size, cost per judge call, whether the judge and the system under test come from the same model family.
With no expert labels at all, start at step 2: no judge figure means anything before labels exist.

## Method
1. **One judge per failure mode, pass or fail.** Each judge checks one failure mode found by `error-analysis`, never "overall quality". It writes its critique, then its verdict. A 1–5 score is not a gate: rewrite it as a binary criterion, or keep it out of any decision. The domain expert writes the criterion after reading real outputs and revises it while grading: criteria shift as people grade. Name the costlier error for this decision: a false pass (a bad answer let through) or a false fail.
2. **Labels from an accountable expert.** One domain expert who owns the risk labels, or two who overlap on 50+ answers with Cohen's kappa ≥ about 0.6 (references/eval-statistics.md §7). Below that, the criterion is unclear: rewrite it before blaming the judge. Labels are made without seeing the judge's verdicts.
3. **Split the labels before writing the prompt.** A small pool (10–20%) for few-shot examples, a dev split (about 40%) to iterate the prompt, a test split (about 40%) scored once per judge version. Aim at 100+ labels with enough expert fails: TNR's interval depends on the number of fails, not the total. Under 20 fails in the test split, TNR is indicative only; with 60, a TNR of 80% is known to about ±10 points (references/judge-tests.md). If fails are rare, enrich the sample with likely fails from the `error-analysis` notes. TPR and TNR are measured within each expert class, so the class mix does not bias them, but enriched fails may be easier or harder to catch than typical ones: draw them from several sources and keep a random part. A rate on traffic needs a random sample, or weights for what was enriched. A figure measured on the pool or the dev split describes the tuning, never the judge.
4. **Set the targets before measuring.** Write TPR and TNR targets, dated and signed by the owner of the decision, before the test split is scored. Derive them from the cost of each error in this decision: stricter on the costly side for a legal, financial or irreversible class, and gate on the lower bound of the interval when a false pass is costly (references/eval-statistics.md §4). No target given? Do not present any figure as usual or default: propose one with its reason, marked as a proposal for the owner to sign. Until a target is signed and met, the judge is not a gate.
5. **Measure on the test split.** Fill the four cells (expert pass or fail × judge pass or fail); given agreement and class counts, rebuild the cells from them. Report TPR (share of expert passes the judge passes) and TNR (share of expert fails the judge fails), each with its Wilson 95% interval (references/eval-statistics.md §2). Never report raw agreement or correlation as the result: when 90% of answers pass, a judge that passes everything agrees 90% with TNR 0. Say what agreement a pass-everything judge would get on this split. Run this skill's `scripts/judge_metrics.py test.csv --tpr-target T --tnr-target T` with the signed targets (columns `human,judge`, values `pass`/`fail`): it prints the counts, TPR and TNR with intervals against the targets, agreement flagged as insufficient, and kappa between judge and expert. Without Python, compute the Wilson interval by hand.
6. **Test the biases that apply.** Position: in pairwise judging, swap the order; the verdict must hold. Verbosity: plot verdict against answer length, and judge length-matched pairs that differ only on the criterion. Self-preference: when the judge and the system come from the same model family, re-judge a sample with another family. Prompt sensitivity: re-run the test split with a paraphrased instruction. Pin the judge model version: an alias that moves is a new judge. Protocols: references/judge-tests.md.
7. **Decide the status.** Both targets met → the judge can gate this failure mode. One missed → not a gate yet, whatever the deadline: read every disagreement with the expert, revise the criterion and rubric (split vague clauses, add a pass and a fail example of the cases it got wrong), then re-test on fresh labels never used for the revision, with enough expert fails (step 3), under targets written before. Meanwhile a human reviews what the judge would have decided; aim review at the costly error: if false passes are costly, review what the judge passes, not only what it fails. Do not assume the current human check catches everything: compare with its error rate when known. A test split whose disagreements were read to revise the prompt has become dev data.
8. **Correct the pass rate on unlabelled traffic.** The judge's observed rate mixes good answers it passes with bad answers it lets through: observed = true × TPR + (1 − true) × (1 − TNR). Say which way it leans by comparing shares of traffic, not error rates: good answers it fails, c × (1 − TPR), pull it down; bad ones it passes, (1 − c) × (1 − TNR), push it up (c the corrected rate). Corrected = (observed + TNR − 1) ÷ (TPR + TNR − 1), clipped to 0–100% (Rogan–Gladen). The interval must carry the uncertainty of TPR and TNR: `python3 scripts/judge_metrics.py test.csv --observed-pass K --observed-n N` bootstraps the labelled rows and the sample together; give the user this command. Without the script, give an approximate 95% interval, marked approximate: c ± 1.96 × √(p(1−p)/n + c²·TPR(1−TPR)/n₊ + (1−c)²·TNR(1−TNR)/n₋) ÷ (TPR + TNR − 1), with p the observed rate on n answers, c the corrected rate, n₊ and n₋ the expert passes and fails of the test split. To name the main source of uncertainty, compute the three terms and cite the largest; never assume it is the smaller class. When TPR + TNR − 1 is below 0.5, the correction is unstable: do not use this judge for a rate. Compare any threshold with the interval, never with the raw rate: a bar inside the interval is neither met nor missed. When proposing more labels to settle it, give the interval width they would yield, never a promise that they will decide.
9. **Re-validate, cost it, hand over.** Re-test on fresh labels after any change of judge model, prompt or criterion, and on a schedule with production labels (for example 50 a month, fails included) because traffic drifts away from the answers the test split was drawn from. Report cost per judge call and per month at the sampling volume. The judge's place in the eval plan goes to `build-evals`; its use on production samples, alerts included, to `production-evals-monitoring`.

## Output
A judge calibration report following `templates/judge-calibration-report.md`: criterion and failure mode, labellers and kappa, label splits, targets with date and signer, confusion counts, TPR and TNR with intervals against targets, bias checks, corrected rate with its interval, status (gate or not a gate yet), next revision, re-validation triggers, cost. A section that cannot be filled says what is missing and who provides it.

## Rules and red lines
- Never accept a judge as a release or level gate on raw agreement or correlation, or when TPR or TNR on the held-out test split is below the target set before measuring.
- Never report a judge's accuracy measured on labels used to write, tune or illustrate its prompt.
- Never gate on a Likert (1–5) judge score without a binary criterion.
- Targets are written, dated and signed before the test split is scored, never after.
- Never report a judge's pass rate on traffic as the quality figure without its correction and interval.
- Below target, the judge is not a gate: a human reviews meanwhile.
- A new judge model or prompt is a new judge: re-test before it gates anything.

## Links
references/eval-statistics.md · references/evals-as-evidence.md · references/autonomy-ladder.md · references/judge-tests.md · scripts/judge_metrics.py · error-analysis · build-evals · production-evals-monitoring · release-to-production

## Sources
- husain-shankar-evals: one binary judge per failure mode, critique before verdict, few-shot/dev/test splits, TPR and TNR against expert labels, correcting the observed rate.
- shankar-validators: criteria drift, so criteria are written after reading outputs and revised.
- zheng-llm-judge: position, verbosity and self-preference biases; swapping the order in pairwise judging.
- yan-llm-evaluators: judge quality read as classification metrics, not correlation.
- rogan-gladen: the corrected pass rate from the judge's sensitivity and specificity.
- cohen-kappa: chance-corrected agreement between two labellers.
- wilson-interval: intervals for TPR and TNR on small classes.
- efron-bootstrap: the interval of the corrected rate, resampling the labels and the sample.
- anthropic-evals: where a model-graded check fits among cheaper graders.
- own-golden-sets: the judge revision loop and re-validation on fresh labels, from client eval work (method only).
