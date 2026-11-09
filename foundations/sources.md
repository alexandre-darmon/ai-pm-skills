# Sources

Every rule in a skill names its source. Skills list ids from this table in their `sources` frontmatter; `scripts/validate_skills.py` rejects unknown ids.

Sources are ideas, never content: skills state rules in their own words and quote at most one sentence.

## Books and articles

| id | Work | What the repo takes from it | Used by |
| --- | --- | --- | --- |
| cagan-inspired | Marty Cagan, *Inspired* (2nd ed., 2017) | the four product risks (value, usability, feasibility, viability); the PM owns outcomes | `ai-opportunity-assessment`, `llm-feature-prd` |
| torres-continuous-discovery | Teresa Torres, *Continuous Discovery Habits* (2021) | outcome over output; opportunity trees as framing | `llm-feature-prd` |
| fitzpatrick-mom-test | Rob Fitzpatrick, *The Mom Test* (2013) | problem-validation questions | `ai-opportunity-assessment` |
| kohavi-experiments | Ron Kohavi, Diane Tang, Ya Xu, *Trustworthy Online Controlled Experiments* (2020) | A/B feasibility, sample size, pitfalls | `release-to-production` |
| mitchell-model-cards | Margaret Mitchell et al., *Model Cards for Model Reporting* (2019) | model card structure | `model-card-ai-registry` |
| hammer-reengineering | Michael Hammer, James Champy, *Reengineering the Corporation* (1993) | method lineage for process redesign | `process-ai-redesign` |
| dama-dmbok | DAMA International, *DAMA-DMBOK* (2nd ed., 2017) | data-quality dimensions | `ai-data-requirements` |

## Evaluation methods and statistics

The backbone of the Evaluate block. Each row is a method the skills restate in their own words.

| id | Work | What the repo takes from it | Used by |
| --- | --- | --- | --- |
| husain-shankar-evals | Hamel Husain and Shreya Shankar, *AI Evals for Engineers and PMs* (course, 2025) and their FAQ on AI evals (hamel.dev, 2025) | error analysis before metrics (open coding, then grouping into failure modes, until no new mode appears); binary pass/fail criteria over Likert scales; judges validated against expert labels with TPR and TNR; synthetic inputs built from dimensions | `agent-evals`, `ai-incident-playbook`, `build-evals`, `error-analysis`, `llm-judge-calibration`, `model-card-ai-registry`, `production-evals-monitoring`, `retrieval-evaluation`, `synthetic-eval-data` |
| shankar-validators | Shreya Shankar et al., *Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences* (UIST 2024) | criteria drift: people refine their criteria while grading outputs, so criteria are written after reading outputs and revised | `error-analysis`, `llm-judge-calibration` |
| glaser-strauss-grounded-theory | Barney Glaser and Anselm Strauss, *The Discovery of Grounded Theory* (1967); Anselm Strauss and Juliet Corbin, *Basics of Qualitative Research* (1990) | open coding, axial coding, theoretical saturation: the lineage of error analysis | `error-analysis` |
| zheng-llm-judge | Lianmin Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena* (NeurIPS 2023) | position, verbosity and self-enhancement biases of LLM judges; swap the order in pairwise judging | `llm-judge-calibration`, `synthetic-eval-data` |
| yan-llm-evaluators | Eugene Yan, *Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)* (eugeneyan.com, 2024) | direct scoring versus pairwise comparison; judge quality read as classification metrics, not correlation | `llm-judge-calibration` |
| miller-error-bars | Evan Miller, *Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations* (Anthropic, 2024) | standard errors on eval scores, clustering when cases share a source, paired differences between two systems, power analysis before the run | `ai-opportunity-assessment`, `ai-vendor-evaluation`, `build-evals`, `model-card-ai-registry`, `retrieval-evaluation` |
| anthropic-agent-evals | Anthropic, *Demystifying evals for AI agents* (engineering blog, 2026) | tasks, trials and graders on transcript and outcome; pass@k against pass^k; capability evals versus regression evals | `agent-evals` |
| yao-tau-bench | Shunyu Yao et al., *τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains* (2024) | pass^k (all k trials succeed) as the reliability measure for agents; grading on the database end state; a simulated user | `agent-evals` |
| es-ragas | Shahul Es et al., *RAGAS: Automated Evaluation of Retrieval Augmented Generation* (2023) | faithfulness, answer relevance and context precision and recall measured apart | `retrieval-evaluation` |
| manning-ir | Christopher Manning, Prabhakar Raghavan, Hinrich Schütze, *Introduction to Information Retrieval* (2008) | recall at k, precision, mean reciprocal rank, nDCG, pooled relevance judgements | `retrieval-evaluation` |
| rogan-gladen | Walter Rogan and Beth Gladen, *Estimating prevalence from the results of a screening test* (American Journal of Epidemiology, 1978) | correcting an observed pass rate with the judge's sensitivity and specificity | `llm-judge-calibration`, `production-evals-monitoring` |
| cohen-kappa | Jacob Cohen, *A coefficient of agreement for nominal scales* (1960) | agreement corrected for chance, between two labellers | `llm-judge-calibration` |
| wilson-interval | Edwin Wilson, *Probable inference, the law of succession, and statistical inference* (JASA, 1927); James Hanley and Abby Lippman-Hand, *If nothing goes wrong, is everything all right?* (JAMA, 1983) | an interval for a pass rate that holds with few cases or a rate near 0 or 1; zero failures in n cases still allows a true rate up to about 3/n | `agent-evals`, `ai-adoption-plan`, `ai-vendor-evaluation`, `build-evals`, `error-analysis`, `llm-judge-calibration`, `model-card-ai-registry` |
| efron-bootstrap | Bradley Efron and Robert Tibshirani, *An Introduction to the Bootstrap* (1993); J.N.K. Rao and C.F.J. Wu, *Resampling inference with complex survey data* (JASA, 1988) | resampling cases to get an interval; rescaling for small strata | `llm-judge-calibration` |
| montgomery-spc | Douglas Montgomery, *Introduction to Statistical Quality Control* (8th ed., 2019) | control charts for a rate: alert on a shift beyond its expected noise, not on every dip | `ai-incident-playbook`, `production-evals-monitoring` |
| google-sre | Betsy Beyer et al., *Site Reliability Engineering* (2016) | service-level objectives, error budgets, alerting on symptoms users feel | `ai-incident-playbook`, `production-evals-monitoring` |
| repo-evals-skills | [ai-evals-course/evals-skills](https://github.com/ai-evals-course/evals-skills) | the engineering counterpart this repo complements; credited, ideas only | README credits |
| openai-evals-guide | OpenAI, *Evaluation best practices* (platform documentation, 2025) | eval-driven development, logging everything that runs in production | README credits |
| inspect-ai | UK AI Security Institute, [Inspect](https://inspect.aisi.org.uk/) evaluation framework | a harness-neutral case format: dataset, solver, scorer | `build-evals` (harness note) |
| promptfoo | [Promptfoo](https://www.promptfoo.dev/) | assertions per test case, as a second harness format | `build-evals` (harness note) |

## Regulation and guidance

| id | Work | What the repo takes from it | Used by |
| --- | --- | --- | --- |
| eu-ai-act | Regulation (EU) 2024/1689 (AI Act) | classification, annex III, deployer duties, human oversight (art. 14), literacy (art. 4), record-keeping; the articles that ask for eval evidence: testing against prior metrics (art. 9), test data (art. 10), accuracy and robustness (art. 15), quality management (art. 17), deployer monitoring (art. 26(5)), post-market monitoring (art. 72), serious incidents (art. 73) | `ai-act-classification`, `ai-adoption-plan`, `ai-incident-playbook`, `ai-vendor-evaluation`, `model-card-ai-registry`, `production-evals-monitoring`, `synthetic-eval-data`, `system-prompt-and-guardrails` |
| eu-digital-omnibus-ai | Regulation (EU) 2026/1744 (Digital Omnibus on AI), in force 27 July 2026 | the amended application dates (annex III high-risk from 2 December 2027, annex I from 2 August 2028) and the rewritten art. 4 | `ai-act-classification`, `ai-adoption-plan`, `ai-vendor-evaluation`, `production-evals-monitoring` |
| en-18286 | EN 18286, quality management system for EU AI Act regulatory purposes (CEN-CENELEC JTC 21), cited in the Official Journal on 14 October 2026 | test procedures before, during and after development as part of the quality system | `production-evals-monitoring` |
| dora | Regulation (EU) 2022/2554 (Digital Operational Resilience Act), arts. 28–30 | ICT third-party risk for banks and insurers: register of providers, mandatory contract clauses, exit plans | `ai-vendor-evaluation` |
| ec-ai-act-guidelines | European Commission guidelines on the AI Act, as published | interpretation of definitions, prohibited practices, high-risk classification | `ai-act-classification` |
| gdpr | Regulation (EU) 2016/679 (GDPR) | processing principles (art. 5), lawful basis (art. 6), DPIA (art. 35), breach notification (art. 33) | `ai-act-classification`, `ai-data-requirements`, `ai-incident-playbook`, `ai-vendor-evaluation`, `conversation-analysis`, `error-analysis`, `production-evals-monitoring`, `synthetic-eval-data` |
| cnil-ai | CNIL resources on AI systems | practical GDPR application to AI | `ai-act-classification` |
| fr-ai-act-implementation | French implementing texts for the AI Act, as published | national authorities and procedures that apply in France | `ai-act-classification` |

## Technical references

| id | Work | What the repo takes from it | Used by |
| --- | --- | --- | --- |
| owasp-llm-top10 | OWASP, *Top 10 for LLM Applications* (2025 edition) | guardrail threat classes | `system-prompt-and-guardrails` |
| anthropic-agents | Anthropic, *Building effective agents* (2024) | loop first, framework last | `agent-design-and-tooling`, `agent-evals` |
| anthropic-evals | Anthropic documentation on building evaluations | eval design, judge use | `build-evals`, `llm-judge-calibration`, `production-evals-monitoring`, `retrieval-evaluation`, `synthetic-eval-data` |
| otel-genai | OpenTelemetry, GenAI semantic conventions | trace, outcome-event and evaluation-result fields | `assistant-kpis-cost-per-outcome`, `production-evals-monitoring` |
| ms-hax | Amershi et al., *Guidelines for Human-AI Interaction* (Microsoft, 2019) | interaction guidelines as a reference | `ai-interaction-patterns` |
| google-pair | Google PAIR, *People + AI Guidebook* | trust calibration, explanation patterns | `ai-adoption-plan`, `ai-interaction-patterns` |
| text-to-sql-benchmarks | Spider (Yu et al., 2018), BIRD (Li et al., 2023) | eval method for text-to-SQL, not their scores | `build-evals` |

## Other skill repositories

Read in the November 2026 review. Ideas only, restated in our own words; no text copied. Repos no skill draws on any more were removed in v2.0.

| id | Work | What the repo takes from it | Used by |
| --- | --- | --- | --- |
| repo-chanmeng | [ChanMeng666/ai-product-manager-skill](https://github.com/ChanMeng666/ai-product-manager-skill) (MIT) | solution selection, agent and production checks, eval depth | `agent-design-and-tooling`, `agent-evals`, `ai-adoption-plan`, `ai-data-requirements`, `ai-incident-playbook`, `ai-interaction-patterns`, `ai-opportunity-assessment`, `ai-roi-quantification`, `assistant-kpis-cost-per-outcome`, `build-evals`, `conversation-analysis`, `error-analysis`, `llm-feature-prd`, `model-card-ai-registry`, `model-selection`, `process-ai-redesign`, `release-to-production`, `system-prompt-and-guardrails` |
| repo-yoseph | [Yoseph-Zuskin/AI-Product-Manager](https://github.com/Yoseph-Zuskin/AI-Product-Manager) (MIT) | business case lines, vendor checks | `ai-opportunity-assessment`, `ai-roi-quantification`, `ai-vendor-evaluation`, `model-card-ai-registry` |
| repo-lenny | [RefoundAI/lenny-skills](https://github.com/RefoundAI/lenny-skills) (MIT) | eval practice and AI UX, as ideas; guest quotes are not reused | `agent-evals`, `ai-adoption-plan`, `build-evals`, `model-selection` |
| repo-vishalhabib | [vishalhabib99/ai-pm-skills](https://github.com/vishalhabib99/ai-pm-skills) (MIT) | fixing the bar before looking at cases, declined lists | `ai-act-classification`, `ai-data-requirements`, `ai-opportunity-assessment`, `build-evals` |
| repo-product-on-purpose | [product-on-purpose/pm-skills](https://github.com/product-on-purpose/pm-skills) (Apache-2.0) | template-only control, routing checks | `ai-data-requirements` |

## Own experience

Ids starting with `own-` point to the author's missions, anonymised (e.g. `own-prds`, `own-guardrails`, `own-nanoagent`). They need no row here, but the skill's Sources section says in one line what the rule comes from. Client data never leaves the client; only the method is published.
