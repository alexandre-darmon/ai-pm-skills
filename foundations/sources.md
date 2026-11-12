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
| yao-tau-bench | Shunyu Yao et al., *τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains* (2024) | pass^k (all k trials succeed) as the reliability measure for agents; grading on the database end state, once per conversation; an LLM-simulated user that drives the conversation | `agent-evals` |
| es-ragas | Shahul Es et al., *RAGAS: Automated Evaluation of Retrieval Augmented Generation* (2023) | faithfulness, answer relevance and context precision and recall measured apart | `retrieval-evaluation` |
| manning-ir | Christopher Manning, Prabhakar Raghavan, Hinrich Schütze, *Introduction to Information Retrieval* (2008) | recall at k, precision, mean reciprocal rank, nDCG, pooled relevance judgements | `retrieval-evaluation` |
| agentdojo | Edoardo Debenedetti et al., *AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents* (NeurIPS 2024) | the same agent tasks run clean and with injected tool outputs: utility, utility under attack, attack success rate | — |
| kalai-hallucinate | Adam Tauman Kalai et al., *Why Language Models Hallucinate* (OpenAI, 2025) | accuracy-only scoring rewards guessing; grade abstention apart and price a confident error above a hand-off | — |
| tamkin-discrim-eval | Alex Tamkin et al., *Evaluating and Mitigating Discrimination in Language Model Decisions* (Anthropic, 2023) | counterfactual variants that change only a protected attribute, read as a decision flip rate | — |
| sclar-format-spread | Melanie Sclar et al., *Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design* (ICLR 2024) | scores move with meaning-preserving format changes: report the spread and the worst variant | — |
| laban-multi-turn | Philippe Laban et al., *LLMs Get Lost in Multi-Turn Conversation* (2025) | the same task revealed over several turns scores lower, mostly from unreliability across runs rather than lost aptitude; a model that assumes too early and answers too soon rarely recovers | — |
| kwan-mt-eval | Wai-Chung Kwan et al., [*MT-Eval: A Multi-Turn Capabilities Evaluation Benchmark for Large Language Models*](https://arxiv.org/abs/2401.16745) (EMNLP 2024) | the same queries scored single-turn and multi-turn to measure the drop; four interaction patterns (recollection, expansion, refinement, follow-up); distance to the relevant turn and error propagation as causes | — |
| bai-mt-bench-101 | Ge Bai et al., [*MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues*](https://arxiv.org/abs/2402.14762) (ACL 2024) | a taxonomy of multi-turn abilities drawn from real dialogues, scored per task and per turn | — |
| dou-simulatorarena | Yao Dou et al., [*SimulatorArena: Are User Simulators Reliable Proxies for Multi-Turn Evaluation of AI Assistants?*](https://arxiv.org/abs/2510.05444) (EMNLP 2025) | validate a user simulator against annotated real conversations, on both message behaviour and agreement with human ratings; profile-conditioned simulators agree best | — |
| zhou-sim2real-users | Xuhui Zhou et al., [*Mind the Sim2Real Gap in User Simulation for Agentic Tasks*](https://arxiv.org/abs/2603.11245) (2026) | τ-bench rerun with real participants: LLM-simulated users are too cooperative and uniform, so agents score higher than with people; a stronger model is not a more faithful simulator | — |
| mazeika-harmbench | Mantas Mazeika et al., [*HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal*](https://arxiv.org/abs/2402.04249) (2024) | attack success rate as the share of test cases that elicit the target behaviour, judged by a fixed classifier under fixed generation settings; generation length alone moved it by up to 30% in the paper | — |
| openai-external-red-teaming | Lama Ahmad et al., [*OpenAI's Approach to External Red Teaming for AI Models and Systems*](https://arxiv.org/abs/2503.16431) (OpenAI, 2024) | campaign design: red team composition, access level, guidance to testers; findings feed risk assessment and become automated evaluations; a red team is a snapshot in time | — |
| anthropic-red-teaming | Anthropic, [*Challenges in red teaming AI systems*](https://www.anthropic.com/news/challenges-in-red-teaming-ai-systems) (2024) | domain-expert, automated, multimodal and open-ended red teaming compared; qualitative probing standardised, then scaled into quantitative evaluations in a test-mitigate-retest loop | — |
| ai2-signal-noise | Ai2, *Signal and Noise: A Framework for Reducing Uncertainty in Language Model Evaluation* (2025) | keep cases whose spread between systems exceeds their run-to-run noise | — |
| zhu-agentic-benchmarks | Yuxuan Zhu et al., *Establishing Best Practices for Building Rigorous Agentic Benchmarks* (NeurIPS 2025) | validity checks before trusting a benchmark score: a do-nothing agent, a known-wrong answer | — |
| zhang-gsm1k | Hugh Zhang et al., *A Careful Examination of Large Language Model Performance on Grade School Arithmetic* (NeurIPS 2024) | contamination read as the gap between a public set and a fresh matched set | — |
| kapoor-agents-matter | Sayash Kapoor et al., *AI Agents That Matter* (2024) | compare agents on a cost-accuracy frontier against simple baselines | — |
| verga-poll | Pat Verga et al., *Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models* (2024) | a panel of smaller judges from different families, validated as one unit | — |
| rogan-gladen | Walter Rogan and Beth Gladen, *Estimating prevalence from the results of a screening test* (American Journal of Epidemiology, 1978) | correcting an observed pass rate with the judge's sensitivity and specificity | `llm-judge-calibration`, `production-evals-monitoring` |
| cohen-kappa | Jacob Cohen, *A coefficient of agreement for nominal scales* (1960) | agreement corrected for chance, between two labellers | `llm-judge-calibration` |
| wilson-interval | Edwin Wilson, *Probable inference, the law of succession, and statistical inference* (JASA, 1927); James Hanley and Abby Lippman-Hand, *If nothing goes wrong, is everything all right?* (JAMA, 1983) | an interval for a pass rate that holds with few cases or a rate near 0 or 1; zero failures in n cases still allows a true rate up to about 3/n | `agent-evals`, `ai-adoption-plan`, `ai-vendor-evaluation`, `build-evals`, `error-analysis`, `llm-judge-calibration`, `model-card-ai-registry` |
| efron-bootstrap | Bradley Efron and Robert Tibshirani, *An Introduction to the Bootstrap* (1993); J.N.K. Rao and C.F.J. Wu, *Resampling inference with complex survey data* (JASA, 1988) | resampling cases to get an interval; rescaling for small strata | `llm-judge-calibration` |
| montgomery-spc | Douglas Montgomery, *Introduction to Statistical Quality Control* (8th ed., 2019) | control charts for a rate: alert on a shift beyond its expected noise, not on every dip | `ai-incident-playbook`, `production-evals-monitoring` |
| google-sre | Betsy Beyer et al., *Site Reliability Engineering* (2016) | service-level objectives, error budgets, alerting on symptoms users feel | `ai-incident-playbook`, `production-evals-monitoring` |
| repo-evals-skills | [ai-evals-course/evals-skills](https://github.com/ai-evals-course/evals-skills) (Apache-2.0) | the engineering counterpart this repo complements; its build-review-interface skill as the generic model of a trace review app; credited, ideas only | README credits |
| openai-evals-guide | OpenAI, *Evaluation best practices* (platform documentation, 2025) | eval-driven development, logging everything that runs in production | README credits |
| inspect-ai | UK AI Security Institute, [Inspect](https://inspect.aisi.org.uk/) evaluation framework | a harness-neutral case format: dataset, solver, scorer | `build-evals` (harness note) |
| promptfoo | [Promptfoo](https://www.promptfoo.dev/) | assertions per test case, as a second harness format | `build-evals` (harness note) |

## Regulation and guidance

| id | Work | What the repo takes from it | Used by |
| --- | --- | --- | --- |
| eu-ai-act | Regulation (EU) 2024/1689 (AI Act) | classification, annex III, deployer duties, human oversight (art. 14), literacy (art. 4), record-keeping and automatic logs (art. 12), log retention by providers (art. 19) and by deployers (art. 26(6)); the articles that ask for eval evidence: testing against prior defined metrics and probabilistic thresholds before release, and residual risk judged acceptable (art. 9(5), 9(8)), test data (art. 10), accuracy and robustness (art. 15), resilience to errors and to attacks such as data poisoning, model poisoning, adversarial examples and confidentiality attacks (art. 15(4)–(5)), quality management (art. 17), deployer monitoring (art. 26(5)), post-market monitoring (art. 72), serious incidents (art. 73); testing to identify risk-management measures and show consistent performance (art. 9(6)); the accuracy, robustness and cybersecurity levels a provider declares in the instructions for use (art. 13(3)(b)(ii)) | `ai-act-classification`, `ai-adoption-plan`, `ai-incident-playbook`, `ai-vendor-evaluation`, `model-card-ai-registry`, `production-evals-monitoring`, `synthetic-eval-data`, `system-prompt-and-guardrails` |
| eu-digital-omnibus-ai | Regulation (EU) 2026/1744 (Digital Omnibus on AI), in force 27 July 2026 | the amended application dates (annex III high-risk from 2 December 2027, annex I from 2 August 2028) and the rewritten art. 4 | `ai-act-classification`, `ai-adoption-plan`, `ai-vendor-evaluation`, `production-evals-monitoring` |
| eu-gpai-code | European Commission, [*General-Purpose AI Code of Practice*](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) (10 July 2025), safety and security chapter | context only: providers of GPAI models with systemic risk run state-of-the-art evaluations including red-teaming and open-ended testing; deployers do not inherit this duty but can ask for the provider's results | — |
| en-18286 | EN 18286, quality management system for EU AI Act regulatory purposes (CEN-CENELEC JTC 21), cited in the Official Journal on 14 October 2026 | test procedures before, during and after development as part of the quality system | `production-evals-monitoring` |
| dora | Regulation (EU) 2022/2554 (Digital Operational Resilience Act), arts. 3(7), 24–25, 28–30 | ICT asset definition (art. 3(7)); digital operational resilience testing programme and testing of ICT tools and systems: vulnerability scans, scenario-based and penetration tests (arts. 24–25); ICT third-party risk for banks and insurers: register of providers, mandatory contract clauses, exit plans | `ai-vendor-evaluation` |
| dora-rts-ict-risk | Commission Delegated Regulation (EU) 2024/1774 (RTS on the ICT risk management framework under DORA) | records of ICT assets (art. 4(2)(b)); only authorised software on ICT systems (art. 11(2)(c)); production data kept out of non-production environments, with a narrow derogation for testing (art. 16(5)(a), 16(6)); development, testing and production-data rules for ICT systems, extended to systems built or managed by users outside the ICT function (art. 16(9)) | — |
| dora-incident-reporting | Regulation (EU) 2022/2554 (DORA) arts. 17–19, and Commission Delegated Regulation (EU) 2025/301 art. 5 | classification of major ICT-related incidents and their reporting clocks: initial notification within 4 hours of classification and no later than 24 hours from awareness, intermediate report within 72 hours, final report within one month | — |
| esma-qa-2103 | ESMA, [Q&A 2103](https://www.esma.europa.eu/publications-data/questions-answers/2103) on end-user computing, EULAs and shadow IT under DORA (11 February 2024) | end-user tools and systems built outside the ICT function are ICT assets (DORA art. 3(7)): identified, documented and risk-managed like any other | — |
| ec-ai-act-guidelines | European Commission guidelines on the AI Act, as published | interpretation of definitions, prohibited practices, high-risk classification | `ai-act-classification` |
| gdpr | Regulation (EU) 2016/679 (GDPR) | processing principles (art. 5), lawful basis (art. 6), processor terms (art. 28), DPIA (art. 35), breach notification (art. 33) | `ai-act-classification`, `ai-data-requirements`, `ai-incident-playbook`, `ai-vendor-evaluation`, `conversation-analysis`, `error-analysis`, `production-evals-monitoring`, `synthetic-eval-data` |
| cnil-ai | CNIL resources on AI systems | practical GDPR application to AI | `ai-act-classification` |
| fr-ai-act-implementation | French implementing texts for the AI Act, as published | national authorities and procedures that apply in France | `ai-act-classification` |

## Technical references

| id | Work | What the repo takes from it | Used by |
| --- | --- | --- | --- |
| owasp-llm-top10 | OWASP, *Top 10 for LLM Applications* (2025 edition) | guardrail threat classes; an attack taxonomy for LLM applications (prompt injection, sensitive information disclosure, data and model poisoning, excessive agency, system prompt leakage and others) to read red-team coverage against | `system-prompt-and-guardrails` |
| nist-ai-100-2 | NIST, [*Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations*](https://csrc.nist.gov/pubs/ai/100/2/e2025/final) (NIST AI 100-2 E2025, March 2025) | attacks classed by attacker goal (availability, integrity, privacy, and misuse for generative AI), capability, knowledge and lifecycle stage; direct and indirect prompt injection; a shared vocabulary for attack classes | — |
| mitre-atlas | MITRE, [ATLAS](https://atlas.mitre.org/) knowledge base of adversary tactics and techniques against AI systems | tactics, techniques and case studies modelled on ATT&CK, to map a campaign's attacks to known techniques; counts change by release, cite the version used | — |
| pyrit | Microsoft AI Red Team, [PyRIT](https://github.com/microsoft/PyRIT) (MIT) | an example of an open-source red-team toolkit (automated scans, adaptive multi-turn attacks, human-led testing); named as an example, never as a procedure | — |
| garak | NVIDIA, [garak](https://github.com/NVIDIA/garak) (Apache-2.0) | an example of an open-source LLM vulnerability scanner: probes send attacks, detectors mark failures, a failure rate per probe; named as an example, never as a procedure | — |
| anthropic-agents | Anthropic, *Building effective agents* (2024) | loop first, framework last | `agent-design-and-tooling`, `agent-evals` |
| anthropic-agent-tools | Anthropic, *Writing effective tools for agents, with agents* (engineering blog, 2025) | prototype a few purposeful tools, test them on realistic tasks, read the transcripts, then refine names, descriptions and response size | — |
| mcp-spec | [Model Context Protocol specification](https://modelcontextprotocol.io/specification/latest) | tools, resources and prompts exposed by a server to a model; consent and tool-safety principles | — |
| spec-kit | GitHub, [Spec Kit](https://github.com/github/spec-kit) (MIT) | a project constitution and specs that a coding agent builds against; eval criteria and gates written so a constitution can import them | — |
| anthropic-evals | Anthropic documentation on building evaluations | eval design, judge use | `build-evals`, `llm-judge-calibration`, `production-evals-monitoring`, `retrieval-evaluation`, `synthetic-eval-data` |
| otel-genai | OpenTelemetry, GenAI semantic conventions | trace, outcome-event and evaluation-result fields | `assistant-kpis-cost-per-outcome`, `production-evals-monitoring` |
| ms-hax | Amershi et al., *Guidelines for Human-AI Interaction* (Microsoft, 2019) | interaction guidelines as a reference | `ai-interaction-patterns` |
| google-pair | Google PAIR, *People + AI Guidebook* | trust calibration, explanation patterns | `ai-adoption-plan`, `ai-interaction-patterns` |
| text-to-sql-benchmarks | Spider (Yu et al., 2018), BIRD (Li et al., 2023) | eval method for text-to-SQL, not their scores | `build-evals` |

## Building to learn

The backbone of the Build block (references/build-to-learn.md): what a PM builds, how it is bounded, and what goes wrong when it is not.

| id | Work | What the repo takes from it | Used by |
| --- | --- | --- | --- |
| cagan-prototypes-products | Marty Cagan, [*Prototypes vs Products*](https://www.svpg.com/prototypes-vs-products/) (SVPG, 2025) | build to learn versus build to earn; a convincing prototype hides most of the work a product needs | — |
| singer-shape-up | Ryan Singer, [*Shape Up*](https://basecamp.com/shapeup) (Basecamp, 2019) | the appetite (what the work is worth, set before, not an estimate); the circuit breaker (stop by default at the end of the cycle) | — |
| kromer-learn-measure-build | Tristan Kromer, [*Build Measure Learn vs Learn Measure Build*](https://kromatic.com/blog/build-measure-learn-vs-learn-measure-build) (Kromatic, 2012, updated 2023) | plan the loop in reverse: the question, then the data that answers it, then the smallest build | — |
| willison-lethal-trifecta | Simon Willison, [*The lethal trifecta for AI agents*](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) (2025) | private data, untrusted content and a way to send data out in one agent let an attacker steal the data; remove one of the three | — |
| metr-ai-dev-productivity | METR, [*Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) (2025) | perceived speed-up and measured time diverge: measure time and cost per correct output | — |
| replit-db-incident | eWeek, [*AI Agent Wipes Production Database, Then Lies About It*](https://www.eweek.com/news/replit-ai-coding-assistant-failure/) (July 2025) | a coding agent told to change nothing without approval deleted a live database: controls belong in code and permissions, not in the prompt | — |
| bloomberg-ing-vibe-coding | Bloomberg, [*ING's 'Vibe Coding' AI Is Building Its New Trading Systems*](https://news.bloomberglaw.com/artificial-intelligence/ings-vibe-coding-ai-is-building-its-new-trading-systems) (May 2026) | a bank prototyping trading tools in hours, with senior developers validating before anything runs on live systems | — |
| aws-euc-tiers | AWS for Industries, [*EUC 2.0: Why uncontrolled copilot platforms are financial services' next governance challenge*](https://aws.amazon.com/blogs/industries/euc-2-0-why-uncontrolled-copilot-platforms-are-financial-services-next-governance-challenge/) (2026) | four tiers for employee-built AI (personal, team, business-critical, mission-critical) and the controls each one requires | — |
| husain-field-guide | Hamel Husain, [*A Field Guide to Rapidly Improving AI Products*](https://hamel.dev/blog/posts/field-guide/) (2025) | a custom data viewer is the first investment: a thin app over real traces, built in hours, that domain experts use to label | — |
| feng-autonomy-levels | K. J. Kevin Feng, David McDonald, Amy Zhang, [*Levels of Autonomy for AI Agents*](https://arxiv.org/abs/2506.12469) (2025) | autonomy described by the user's role (operator, collaborator, consultant, approver, observer); cross-check for the L0–L5 ladder, which stays the repo's only definition | — |
| sierra-adlc | Sierra, [*The Agent Development Life Cycle*](https://sierra.ai/blog/agent-development-life-cycle) (2024) | declarative goals with deterministic guardrails, versioned agent snapshots, expert conversation reviews turned into regression tests | — |
| reganti-badam-ccd | Aishwarya Naresh Reganti and Kiriti Badam, [*Why your AI product needs a different development lifecycle*](https://www.lennysnewsletter.com/p/why-your-ai-product-needs-a-different) (Lenny's Newsletter, 2025) | continuous development and continuous calibration; agency earned version by version, starting with high human control | — |

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
