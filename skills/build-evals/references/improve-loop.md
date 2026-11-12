# Improve loop

Load this once the set, the graders, the thresholds and the frozen baseline exist (SKILL.md steps 1 to 8) and the feature misses a bar. It turns "try things until the score looks better" into runs whose result means something. Every run uses the same set, the same graders and the same judge as the baseline.

The ideas come from controlled experiments (kohavi-experiments: one change against a fixed control, the decision and stopping rules written before the data) and from error analysis (husain-shankar-evals: fixes ranked by the failure modes seen in outputs), applied to offline eval runs.

## 1. Rank fixes by failure share

Start from the failed cases of the last run, not from ideas. Give each failed case one failure mode (the first step that went wrong, for a pipeline: references/component-evals.md), count the cases per mode, and work on the mode with the largest share in the class with the highest cost. A fix aimed at a mode that holds 3 of 40 failures can raise the score by at most 3 cases, whatever it does: say so before spending a run on it. A mode nobody has seen in the outputs is not on the list.

## 2. Record a prediction before each run

Before the run, write down in the eval plan: the change (prompt, model, retrieval setting, tool description), the mode it targets, the cases expected to flip from fail to pass, and the classes that must not move. After the run, compare. A run that flips cases nobody predicted, or flips the predicted ones and breaks others, is read before anything ships: the change did something other than what was intended. A prediction written after the result is not a prediction.

## 3. One variant against the frozen baseline

Change one thing per run and compare it with the frozen baseline on the same cases, paired (references/eval-statistics.md §5). Two changes in one run cannot be told apart; a comparison against the previous experiment instead of the baseline lets small drifts add up unseen. A gap inside the noise is a tie, and a tie does not ship. The regression suite stays near 100% on every variant; a variant that trades a regression case for a capability case is a loss on a costly class.

## 4. Stop rule

Fix it before the first run, in the plan, with who signs it:
- **Stop and ship** when every class clears its gate (the lower bound for a costly class) and the regression suite holds.
- **Stop and change approach** after a fixed number of variants (three to five is typical) with no gain outside the noise on the target mode: the fix belongs in the data, the spec, the pipeline cut or the autonomy level (references/autonomy-ladder.md), not in another prompt edit.
- **Stop and escalate** when the run budget (judge calls, labelling hours) is spent: report the best variant with its intervals and what is still not demonstrated.

Each loop on the same cases also tunes the system to them. Check the final variant once on the private holdout before it gates anything; a score that drops there was fitted to the set.
