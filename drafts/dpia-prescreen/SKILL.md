---
name: dpia-prescreen
description: 'Pre-screen whether an AI use case needs a DPIA against the nine EDPB criteria and the CNIL list, and pre-fill it for the DPO. Use when personal data, profiling or a new data source is in scope.'
stage: govern
version: 0.2.0
last_verified: 2026-11-06
depends_on: [ai-data-requirements, ai-act-classification]
feeds: [model-card-ai-registry]
autonomy_relevant: true
sources: [gdpr, edpb-wp248, cnil-dpia, cnil-ai, repo-chanmeng]
eval_threshold: 0.90
status: draft
---

# dpia-prescreen

## When to use
- An AI feature processes personal data, profiles people or makes automated decisions.
- The DPO asks for a pre-screen, a new data source joins an existing system, or a step moves up the autonomy ladder (`references/autonomy-ladder.md`): re-screen.
- Do not use for the AI Act classification: use `ai-act-classification`.
- Do not use when no personal data is involved in any form: say so in one line.

## Inputs
Mandatory: purpose, populations, data categories.
Ask if missing: automated decision flags, vendors and hosting, retention, volume. Do not wait for the answers: screen on the stated facts and list what would change the result.

## Method
1. Map the AI data flows. Read the flow table from `ai-data-requirements` when it exists, otherwise fill one row per flow, with `unknown` where the brief is silent: prompts and free text; outputs; traces and logs; retrieval index and its permissions; agent memory; eval sets built from production prompts or incident traces (their own retention, anonymised first); vendor retention and training terms; fine-tuning data.
2. Score the nine EDPB criteria (WP248 rev.01), each yes, no or unknown with a reason: evaluation or scoring; automated decision with legal or similar effect; systematic monitoring; sensitive or highly personal data; large scale; matching or combining datasets; vulnerable people (employees count); innovative use of technology; preventing the use of a right or service. Only a yes backed by a stated fact counts. "Likely", "usually" or a guess is `unknown`, not counted, and becomes a question saying what it would change. Two criteria need AI-specific reading:
   - Sensitive data: free text can carry special-category data nobody planned for. Count it when the feature invites people to write about themselves or others, or the text stays linked to a person. Text neither linked nor kept stays a question.
   - Innovative use: CNIL judges it against the state of the art, not by the word AI. Generative AI and deep learning generally count; regression, clustering and random forests with known risks generally do not.
3. Check the mandatory cases: GDPR art. 35(3) (systematic automated evaluation with legal or similar effect, large-scale special-category data, large-scale monitoring of public areas) and the French CNIL list under art. 35(4), which includes constant monitoring of employees' activity and profiling for HR management, recruitment selection algorithms among its examples. Read the full list when another domain is in play (health, biometrics, large-scale location, social support).
4. Check autonomy. Give the level of each step that touches a person, from `references/autonomy-ladder.md`. A step that produces or drives a decision with legal or similarly significant effect on a person becomes a question for the DPO on GDPR art. 22, with the facts: level, who reviews, cases per reviewer per day, override rate, authority to change the outcome. Review on paper raises it too: WP251 rev.01 discounts human involvement that is only a gesture and asks for someone with the authority and competence to change the decision. A score that a later decision draws on strongly can itself be the decision (CJEU C-634/21 SCHUFA).
5. Recommend, on the counted criteria. A mandatory case gives `DPIA required`. Two or more give `DPIA recommended`: WP248 says that in most cases the controller can consider a DPIA is needed. One is a question for the DPO, because WP248 says one can be enough in some cases: give `DPIA recommended` if the facts name a concrete high risk to people or leave it unclear whether there is one, since WP248 recommends carrying one out when it is not clear; otherwise `DPIA not needed`. An LLM or an unanswered question alone, with nothing else counted, does not make it unclear: list it under what would change the result. Zero gives `DPIA not needed`. State which unknown would move the result. The DPO decides; the skill prepares. A decision not to carry out a DPIA despite the criteria is justified in writing with the DPO's view on record.
6. Pre-fill the product sections from the flow rows: purpose, data, flows, recipients, retention, risks, measures.
7. Flag transfers: any hosting, vendor or support access outside the EU is flagged for the DPO, with vendor and country. It is flagged, not assessed.
8. Write the questions for the DPO.

## Output
`templates/prescreen.md`, all headings present, also when the request is a quick yes-or-no question. The count reads `Count: <n>/9` and holds only counted yes. The recommendation line reads `Recommendation: DPIA required`, `Recommendation: DPIA recommended` or `Recommendation: DPIA not needed`, followed by "The controller decides on the DPO's advice".

## Rules and red lines
- Checklist, not verdict: the controller decides on the DPO's advice (GDPR art. 35).
- The count rule is applied and shown.
- A criterion with no stated fact is unknown, never counted.
- Art. 22 is a question with facts, never a conclusion that it applies or does not.
- Transfers are flagged, never declared lawful.

## Links
ai-data-requirements · ai-act-classification · model-card-ai-registry · cse-consultation

## Sources
- gdpr: art. 22 and art. 35, including the mandatory cases in 35(3). On art. 22: WP251 rev.01 and CJEU C-634/21.
- edpb-wp248: the nine criteria, the two-criteria rule, one criterion being enough in some cases.
- cnil-dpia: the French list and PIA sections.
- cnil-ai: AI how-to sheet on DPIAs, innovative use judged by the state of the art.
- repo-chanmeng: free-text logs and agent memory as sensitive flows; unplanned sensitive input (ideas, own words).
