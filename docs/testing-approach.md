# How the skills are tested

Status on 2026-11-10. No single test is enough, so each mode answers a different question. Step-by-step details: [evaluation.md](evaluation.md).

| Test mode | The question it answers | Cost | Weakness | Here | Seen elsewhere |
| --- | --- | --- | --- | --- | --- |
| Structure check | Is the skill well formed? | Free | Says nothing about quality | Yes, in CI | phuryn, product-on-purpose |
| Grader tests (good and bad answer) | Does the marking rule work? | Free | Examples partly written by hand | Yes | Not seen |
| Regex graders | Does the answer contain this element? | Free per answer | Checks words, not meaning | Yes, the main mode | Not seen as a main mode |
| Red lines | Does the forbidden mistake appear? | Free per answer | False positives on correct answers | Yes | vishalhabib99 commits its gates before the run |
| Triggering and negative case | Does the skill fire when it should, and only then? | Paid | Few cases | Yes, partly | product-on-purpose |
| With and without the skill | Does the skill beat the model alone? | Paid | An easy opponent | Yes | ChanMeng666, vishalhabib99, product-on-purpose |
| Three runs per case | Is the result stable? | Paid, three times the cost | Still a small sample | Every catalog skill | vishalhabib99 |
| Template-only control | Does the method beat its format? | Paid | Depends on the template used | The 6 catalog skills | product-on-purpose |
| Routing between neighbours | Does the right skill fire, such as DPIA or AI Act? | Paid | Does not test quality | Not yet | product-on-purpose |
| LLM judge | Is the advice good on substance? | Low | Noisy, can be confidently wrong | 5 skills: blind, information only, not calibrated, not on legal skills | ChanMeng666, product-on-purpose |
| Blind scoring | Is the grader biased by the arm? | Varies | Heavier to organise | Judge only | ChanMeng666, on part of its scenarios |
| Expert human review | Would a PM or a lawyer use this? | Human time | Slow, few cases | Not yet | Not seen |
| Real use on a mission | Does it save time? | One mission | Hard to reproduce | Not yet measured | Not seen |

"Not seen" comes from file names, READMEs and a few files read in the [November 2026 repos](https://github.com/alexandre-darmon/ai-pm-skills/blob/main/foundations/sources.md). It does not prove a repo tests nothing in private.

## What the two extra tests found

**Template-only control** (regex graders, 3 runs per case, rules committed before the run):

| Skill | Without | Own template only | With | Gain over the template |
| --- | --- | --- | --- | --- |
| `llm-feature-prd` | 29% | 76% | 100% | +24 |
| `assistant-kpis-cost-per-outcome` | 27% | 78% | 99% | +21 |
| `conversation-analysis` | 21% | 80% | 96% | +17 |
| `build-evals` | 51% | 85% | 100% | +15 |
| `ai-act-classification` | 68% | 91% | 100% | +9, under the 10-point bar |
| `cse-consultation` (retired 2026-11-09) | 65% | 91% | 99% | +8, under the 10-point bar |

On average the format alone adds about 40 points and the method about 16 more. For the two legal skills, the gain comes mostly from the format. These templates already carry part of the method, so this is a strict test.

**Blind LLM judge** (Haiku 5.5, generic rubric, not calibrated, each answer judged twice):

| Skill | Without | Own template only | With | Judge noise | Words: template / with |
| --- | --- | --- | --- | --- | --- |
| `llm-feature-prd` | 72% | 76% | 87% | 4 pts | 2,290 / 1,783 |
| `assistant-kpis-cost-per-outcome` | 67% | 83% | 82% | 5 pts | 1,723 / 1,213 |
| `conversation-analysis` | 67% | 71% | 75% | 5 pts | 1,251 / 662 |
| `build-evals` | 76% | 81% | 79% | 8 pts | 1,466 / 838 |
| `ai-roi-quantification` | 71% | not run | 78% | 7 pts | not run / 770 |

- The judge sees a much smaller gain than the regexes: +3 to +15 points over the model alone, against +49 to +75 on the same four catalog skills. Regexes reward what the skills' author asked for, so they overstate the gain on general quality.
- Only `llm-feature-prd` clearly beats its template with the judge. The other gaps are within the judge's noise.
- The skill reaches a similar score with fewer words than the template, between 22% and 47% fewer. This was not a planned measure.
- The judge favours length on some skills (correlation 0.54 to 0.78 with word count on three of five), and Haiku is not a domain expert. Read these scores as a signal until they are calibrated on human scores.

Raw results: [`baselines/template-arm/`](../baselines/template-arm/), [`baselines/judge/`](../baselines/judge/). Sonnet 5.5 graded the same answers afterwards; both judges are in [skill-eval-gains.md](../skill-eval-gains.md) until the calibration rule picks one.

## How sure are these numbers

Since 2026-11-09, each published gain carries a 95% interval from resampling the cases within each skill ([method](evaluation.md#how-sure-are-the-numbers)). Over the catalog:

- **Regex graders**, skill over the model alone: +60 points, interval +51 to +68. Over the template: +17, interval +9 to +26. These are the five catalog skills since `cse-consultation` was retired on 2026-11-09; with it, the figures were +55 (+49 to +63) and +16 (+9 to +23). Retiring a skill with a small gain raises the mean, so read the change as a catalog change, not as progress.
- **Blind judges**, skill over the model alone: +10 (Haiku, +6 to +14) and +11 (Sonnet, +6 to +17). Over the template: +3 (+1 to +5) and +5 (+3 to +7).
- Against the template, both judges see a small gain above zero: on these cases, and by a judge not yet calibrated, the method adds something beyond the format. The gain is small, and comes mostly from `llm-feature-prd` and `conversation-analysis`.
- These intervals only reflect which cases were written. Twenty-one cases (fourteen for the judges), all written by the skills' author, remain the main limit.

## Limits today

- The skills' author also writes the cases and graders, and some graders were corrected after reading answers.
- No outside PM or lawyer has reviewed an answer yet.
- Most drafts have one run per case.
