---
name: synthetic-eval-data
description: 'Generate synthetic eval inputs when real cases are scarce, without fooling yourself. Use pre-launch, for a rare risky class, when privacy blocks real data, or before "generate 1,000 test questions".'
stage: evaluate
version: 0.2.0
depends_on: [error-analysis, build-evals]
feeds: [build-evals, retrieval-evaluation, agent-evals, llm-judge-calibration]
autonomy_relevant: false
sources: [husain-shankar-evals, eu-ai-act, anthropic-evals, zheng-llm-judge, gdpr, tamkin-discrim-eval, sclar-format-spread, own-golden-sets]
eval_threshold: 0.80
status: draft
---

# synthetic-eval-data

## When to use
- Before launch, or for a rare but risky class (complaint with a legal threat, vulnerable customer, fraud claim), too few real cases exist to fill or size the set (fewer than 20, or some classes empty).
- A credit, insurance or HR decision must be tested for flips on a protected attribute or its proxy (name, postcode), or a score must hold under rewording.
- Privacy rules forbid copying real conversations into the eval set.
- Someone proposes "let's just generate 1,000 test questions with GPT or Claude".
- A retrieval (RAG) feature needs questions per document and questions the corpus cannot answer.
- Do not use to classify real production conversations by use case or resolution: that is `conversation-analysis`.
- Do not use to find failure modes by reading existing outputs: that is `error-analysis`.

## Inputs
Mandatory: the real examples that exist, even a dozen; the question classes and their risk; who the users are (language, channel, expertise); domain experts who can review inputs and write expected answers.
Ask if missing: failure hypotheses from `error-analysis`, real traffic statistics (length, language, class mix), the source documents (for RAG), the personal-data rules, the model under test and the model that would generate.

## Method
1. **Ground the dimensions.** Read every real example and the `error-analysis` notes. Name 3 to 6 dimensions along which answers plausibly fail: persona, intent or class, difficulty, channel, language and writing style, edge condition (missing information, two requests in one, outdated product). Each value traces to a real example or a written failure hypothesis; a value with neither is marked "assumed" and kept to a small share. Dimensions invented in a vacuum produce the questions the team imagines, not the ones users ask. Before launch, real examples still exist on today's channels (calls, emails, forms, complaints, a pilot): ask for a few dozen, masked, and say which source grounds each dimension.
2. **Generate tuples first.** A tuple is one value per dimension, e.g. (existing borrower, early repayment, partial amount, mobile, French with typos, missing loan number). List them by enumeration or sampling so every value appears several times, give risky combinations more cases than their traffic share (size per class with references/eval-statistics.md §3), and drop impossible combinations with a written rule. Experts review the tuple list before any text is written: fixing a table is cheaper than fixing 500 questions.
3. **Write inputs from tuples, in a separate step.** One generation call per tuple or small batch, with real examples as style anchors. Ask for the users' real style: typos, missing accents, French and English mixed, incomplete or run-on questions, wrong product names, pasted fragments. Asking for tuples and questions in one shot gives uniform, tidy, too-easy inputs. Prefer a generator from a different model family than the system under test.
4. **Review and measure realism.** Domain experts read every input (or a stated random share) and reject what a real user would not write. Record the rejection rate per dimension value; a value above about 20% rejected is regenerated with new anchors. Then compare the synthetic distribution with real traffic (median and 90th-percentile length, language share, class mix, share with typos, share of incomplete questions) and write the tolerance beforehand. Outside the tolerance, regenerate: a set that does not look like traffic does not measure the feature. Audit an existing set the same way before adding to it: experts rate a random sample (its rejection rate) and its distribution is compared with traffic; a failing set is regenerated value by value or demoted to a labelled regression check, and its score is read as a score on synthetic cases.
5. **Expected answers come from experts or source documents, never from the system under test.** If the model under test writes the gold answers, the eval measures its agreement with itself. Experts write or approve each expected answer, citing the document it comes from. Do not let the same model family write the questions and judge the answers unchecked: judges favour text like their own. Any judge is validated against expert labels with `llm-judge-calibration`.
6. **Flag every synthetic case and declare the share.** Each case carries `origin` (real or synthetic), generator model and version, tuple, prompt version, date and reviewer. Report the synthetic share per class next to every score, and the score on real and on synthetic cases separately: a global score can be carried by tidy synthetic inputs. For a high-risk system the set composition is part of the test-data evidence of AI Act art. 10 (references/evals-as-evidence.md); whether it is representative enough is a question for counsel, so give the composition table, not a verdict.
7. **Keep synthetic cases out of what the system sees.** Never reuse them as few-shot examples, prompt content or fine-tuning data: the system would be tested on what it was shown. Check overlap before each release. The holdout holds no unflagged synthetic case.
8. **Replace with real cases, by a date.** As traffic arrives, sample real conversations per class (masked, via `conversation-analysis`), add them, and retire synthetic cases class by class. Write the target synthetic share per class and the date; a class still mostly synthetic after it is reported as indicative.
9. **Privacy.** Synthetic data replaces copied personal data, but never paraphrase one real person's case: a rare combination of facts (illness, town, date, amount) can single someone out, and data that can single out a person is still personal data (GDPR recital 26). Build inputs from dimension values, not from stories, and scan outputs for names or identifiers the generator copied from anchors.
10. **For RAG.** Generate questions from document sections, with the section as the relevance label, in users' vocabulary rather than the document's wording (copied wording makes retrieval look easy). Generate as many questions the corpus cannot answer (a product not offered, a period not covered), expected answer "not found". Hand both to `retrieval-evaluation`.
11. **Meaning-preserving variants.** A verdict measured on one wording can flip on another. For a release or a model choice, write each case in about five variants that keep its meaning and expected answer: paraphrase, typos and missing accents, sentence or field order, the users' other language. Report the mean, the worst-variant pass rate and the share of cases whose verdict flips (references/eval-statistics.md §13); a costly class gates on its worst variant.
12. **Counterfactual pairs for decisions about people.** When the output decides on a person (credit, insurance, hiring), build pairs identical except for one protected attribute or its proxy: first name, postcode, age, a gendered word. Read the decision flip rate per attribute with its interval (references/eval-statistics.md §2) and which value the flips favour. Run unchanged inputs twice too: flips between identical runs are the noise floor, and only the excess counts. Zero flips in 100 pairs still allows up to about 3%. Generated pairs test this without copying anyone's special-category data. For a high-risk system the flip rates feed the bias examination of AI Act art. 10(2)(f)-(g) as a checklist line for counsel, never as "no bias".

Prompt skeletons, dimension examples, the realism checks, variants and counterfactual pairs: references/synthetic-generation.md.

## Output
A synthetic set spec following `templates/synthetic-set-spec.md`: real examples read, dimensions and their grounding, tuple plan with weights, generation prompts and models, review results and rejection rates, distribution comparison with real traffic, source of expected answers, flag schema, synthetic share per class, variant and counterfactual results when run, contamination check, replacement plan with dates. A section that cannot be filled says what is missing and who provides it.

## Rules and red lines
- Never present a set as representative without its synthetic share per class.
- Never let the system under test write the expected answers or labels.
- Never generate without dimensions grounded in real traffic or error analysis.
- Never mix unflagged synthetic cases into the holdout or any reported set.
- Synthetic cases never enter prompts, few-shot examples or training data.
- No synthetic input paraphrases a real person's case.
- A bias check is a flip rate with its interval and a question for counsel, never "fair", "no bias" or "compliant".

## Links
references/eval-statistics.md · references/evals-as-evidence.md · references/synthetic-generation.md · error-analysis · build-evals · llm-judge-calibration · conversation-analysis · retrieval-evaluation · agent-evals

## Sources
- husain-shankar-evals: dimensions, tuples, then natural-language inputs in a separate step; synthetic inputs grounded in observed failures.
- eu-ai-act: art. 10 on relevant and representative test data, behind the declared synthetic share; art. 10(2)(f)-(g) on examining and mitigating bias, behind counterfactual pairs as a checklist line.
- anthropic-evals: eval sets that mirror real task distribution, graders written from expected behaviour.
- zheng-llm-judge: self-enhancement bias, behind keeping question writer and judge apart.
- gdpr: recital 26, data that can single out a person stays personal data.
- tamkin-discrim-eval: counterfactual inputs that change only a protected attribute, read as a decision flip rate.
- sclar-format-spread: scores move with meaning-preserving format changes; report the spread and the worst variant.
- own-golden-sets: rejection rate, distribution check and dated replacement of synthetic cases, from client eval work (method only).
