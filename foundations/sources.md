# Sources

Every rule in a skill names its source. Skills list ids from this table in their `sources` frontmatter; `scripts/validate_skills.py` rejects unknown ids.

Sources are ideas, never content: skills state rules in their own words and quote at most one sentence.

## Books and articles

| id | Work | What the repo takes from it | Used by |
| --- | --- | --- | --- |
| cagan-inspired | Marty Cagan, *Inspired* (2nd ed., 2017) | the four product risks (value, usability, feasibility, viability); the PM owns outcomes | S1, P1 |
| torres-continuous-discovery | Teresa Torres, *Continuous Discovery Habits* (2021) | outcome over output; opportunity trees as framing | P1 |
| fitzpatrick-mom-test | Rob Fitzpatrick, *The Mom Test* (2013) | problem-validation questions | S1 |
| helmer-7-powers | Hamilton Helmer, *7 Powers* (2016) | the moat scan | S2 |
| cialdini-influence | Robert Cialdini, *Influence* | ethical persuasion levers, each resting on a verifiable fact | S3, T2 |
| cole-online-writing | Nicolas Cole, *The Art and Business of Online Writing* (2020) | thesis first, specificity, rhythm | S3, S4 |
| hagel-power-of-pull | John Hagel, John Seely Brown, Lang Davison, *The Power of Pull* (2010) | make initiatives pulled, not pushed; be found by the people who already have the problem | S3, S4 |
| category-pirates-snow-leopard | Category Pirates (Nicolas Cole, Christopher Lochhead, Eddie Yoon), *Snow Leopard* (2022) | a category of one; obvious and non-obvious content | S4 |
| calloway-category-of-one | Joe Calloway, *Becoming a Category of One* (2009) | win on what you deliver, not on gimmicks; defy comparison | S4 |
| kohavi-experiments | Ron Kohavi, Diane Tang, Ya Xu, *Trustworthy Online Controlled Experiments* (2020) | A/B feasibility, sample size, pitfalls | M3 |
| mitchell-model-cards | Margaret Mitchell et al., *Model Cards for Model Reporting* (2019) | model card structure | G4 |
| hammer-reengineering | Michael Hammer, James Champy, *Reengineering the Corporation* (1993) | method lineage for process redesign | T1 |
| kotter-change | John Kotter, *Leading Change* (1996) | change sequencing | T2 |
| rogers-diffusion | Everett Rogers, *Diffusion of Innovations* | adopter segments, diffusion by population | T2 |
| feynman-method | Explanation technique attributed to Richard Feynman | explain simply, find the gaps, iterate | T3 |
| dama-dmbok | DAMA International, *DAMA-DMBOK* (2nd ed., 2017) | data-quality dimensions | P2 |

## Regulation and guidance

| id | Work | What the repo takes from it | Used by |
| --- | --- | --- | --- |
| eu-ai-act | Regulation (EU) 2024/1689 (AI Act) | classification, annex III, deployer duties, human oversight (art. 14), literacy (art. 4), record-keeping, serious incidents | G1, G4, G5, T3, B2 |
| ec-ai-act-guidelines | European Commission guidelines on the AI Act, as published | interpretation of definitions, prohibited practices, high-risk classification | G1, T3 |
| gdpr | Regulation (EU) 2016/679 (GDPR) | processing principles (art. 5), lawful basis (art. 6), DPIA (art. 35), breach notification (art. 33) | P2, G2, G5, M5 |
| edpb-wp248 | EDPB / WP29, *Guidelines on DPIA* (WP248 rev.01) | the nine criteria; two or more means a DPIA is likely needed | G2 |
| cnil-dpia | CNIL, list of processing operations requiring a DPIA, and the PIA tool | French DPIA list, pre-filled sections | G2 |
| cnil-ai | CNIL resources on AI systems | practical GDPR application to AI | G1 |
| cnil-employee-monitoring | CNIL guidance on monitoring employees | what counts as monitoring employees and the safeguards CNIL expects | G3 |
| code-du-travail | Code du travail, art. L2312-8, L2312-38 and related | CSE information and consultation on new technologies and monitoring means | G3 |
| fr-cse-case-law | Published French case-law summaries on CSE consultation | how courts read the duty to consult before a new technology or monitoring means | G3 |
| fr-ai-act-implementation | French implementing texts for the AI Act, as published | national authorities and procedures that apply in France | G1 |

## Technical references

| id | Work | What the repo takes from it | Used by |
| --- | --- | --- | --- |
| owasp-llm-top10 | OWASP, *Top 10 for LLM Applications* (2025 edition) | guardrail threat classes | B2 |
| anthropic-agents | Anthropic, *Building effective agents* (2024) | loop first, framework last | B3 |
| anthropic-evals | Anthropic documentation on building evaluations | eval design, judge use | M1 |
| anthropic-claude-code | Anthropic, Claude Code best practices | how to brief an agentic coding tool (`CLAUDE.md`, context, verification) | B1 |
| otel-genai | OpenTelemetry, GenAI semantic conventions | trace and outcome-event fields | M4 |
| apache-ossie | [Apache Ossie](https://ossie.apache.org/) (incubating), Core Metadata Specification | vendor-neutral exchange of metrics, dimensions and joins; AI context | D1 |
| dbt-semantic-layer | dbt, semantic layer documentation | metric definitions, grain, dimensions | D1 |
| ms-hax | Amershi et al., *Guidelines for Human-AI Interaction* (Microsoft, 2019) | interaction guidelines as a reference | P4 |
| google-pair | Google PAIR, *People + AI Guidebook* | trust calibration, explanation patterns | P4 |
| text-to-sql-benchmarks | Spider (Yu et al., 2018), BIRD (Li et al., 2023) | eval method for text-to-SQL, not their scores | P3 |

## Other skill repositories

Read in the November 2026 review. Ideas only, restated in our own words; no text copied.

| id | Work | What the repo takes from it | Used by |
| --- | --- | --- | --- |
| repo-chanmeng | [ChanMeng666/ai-product-manager-skill](https://github.com/ChanMeng666/ai-product-manager-skill) (MIT) | solution selection, agent and production checks, eval depth | as cited in each skill |
| repo-yoseph | [Yoseph-Zuskin/AI-Product-Manager](https://github.com/Yoseph-Zuskin/AI-Product-Manager) (MIT) | business case lines, vendor checks | as cited in each skill |
| repo-lenny | [RefoundAI/lenny-skills](https://github.com/RefoundAI/lenny-skills) (MIT) | eval practice and AI UX, as ideas; guest quotes are not reused | as cited in each skill |
| repo-vishalhabib | [vishalhabib99/ai-pm-skills](https://github.com/vishalhabib99/ai-pm-skills) (MIT) | fixing the bar before looking at cases, declined lists | as cited in each skill |
| repo-product-on-purpose | [product-on-purpose/pm-skills](https://github.com/product-on-purpose/pm-skills) (Apache-2.0) | template-only control, routing checks | as cited in each skill |
| repo-product-to-prod | [naderelewa/Product-to-Prod](https://github.com/naderelewa/Product-to-Prod) | release and production readiness checks | as cited in each skill |
| repo-pangkaifeng | [PANGKAIFENG/ai-product-manager-skills](https://github.com/PANGKAIFENG/ai-product-manager-skills) | AI PM checklists, as ideas | as cited in each skill |
| repo-phuryn | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT) | next-step links between skills | as cited in each skill |
| repo-anthropic-kwp | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) (Apache-2.0) | workflow packaging, as ideas | as cited in each skill |
| repo-deanpeters | [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills) (CC BY-NC-SA 4.0) | ideas only, never text: its license forbids commercial reuse | as cited in each skill |

## Own experience

Ids starting with `own-` point to the author's missions, anonymised (e.g. `own-prds`, `own-guardrails`, `own-nanoagent`). They need no row here, but the skill's Sources section says in one line what the rule comes from. Client data never leaves the client; only the method is published.
