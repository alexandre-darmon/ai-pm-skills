I couldn't save the file: Write is disabled in this session. The full draft is below, so you can paste it into `handover-file.md`.

The main point is that the handover can't say "accuracy 95%, validated". The reasons are in §4.2 of the draft:
- **Different model version.** The 95% was measured on the model version you prototyped with. The gateway serves a newer one, and any model change is a new release, so the baseline doesn't carry over.
- **Small sample.** 38/40 has a 95% Wilson interval of about 83.5% to 98.6%.
- **No per-class scores or bar.** The 40 questions weren't split by class, and no pass bar was signed before the run.
- **A floor, not release evidence.** The prototype score is the floor engineering's build must reach. Release evidence is the same frozen suite run on the engineering build through the gateway.
- **"Validated" isn't yours to claim.** Model risk validates it.

Engineering still saves effort. They can reuse the 40 expert-written questions as the suite's seed, the prompt as configuration, and the failure cases. They have to rerun the suite, but they don't have to rebuild it.

I proposed tier 3 and rebuild by engineering, because this is a regulatory-control area. I couldn't lower the tier on "a human reads the answers" without knowing every output is checked before use.

I also didn't have these facts, so they are marked "to confirm" in the draft:
- model and version used in the test
- prompt location
- credentials the prototype ran on
- number of users
- named owner
- kill date
- what the two failed questions were
- whether a grader or judge was used, and if so its TPR and TNR

I also couldn't read the skill's template or reference files, so I followed the structure from its instructions. I couldn't check the DORA, RTS and AI Act article numbers against its register map, so the draft refers to those rules without numbers.

---

# Handover file: AML and sanctions procedures Q&A assistant
Status: DRAFT, 2026-11-11.

## 0. Containment
Not triggered on what I know (reads the policy library, not production personal data). To confirm: credentials used, whether any case or customer data is in the library or the questions, and the kill date. If production credentials or personal data are involved and the kill date is past or within two weeks, a named owner must record a dated stop-or-exception decision, and the credentials must be rotated.

## 1. Inventory (known / to confirm)
- Function: answers officers' questions on AML and sanctions procedures from the policy library, with citations (known).
- Users: compliance officers; number to confirm.
- Data and credentials: policy library; credentials to confirm.
- Actions: reads and answers; no writes known (confirm).
- Model and version: to confirm. The version used in the test must be written down.
- Prompt location, owner, sponsor, kill date, where it runs: to confirm.
- Eval: 40 questions written with two senior officers; 38 correct (known).

## 2. Tier
- Process axis: proposed tier 3 (regulatory-control area).
- Autonomy axis: answer plus human reading, proposed L1–L2 today and after the change (confirm against the ladder).
- Proposed tier: 3. It stays there unless every output is validated before use. Who checks?

## 3. Outcome
Rebuild by engineering in January. IT risk and model risk decide, not the sponsor.

## 4. Handover contract
**Baseline (a floor, not release evidence):**
- 38/40 = 95.0%, Wilson 95% interval about 83.5%–98.6%.
- Still to supply: suite version or hash, grader, model and prompt versions, run date, per-class scores, description of the two failures, whether criteria moved while grading.
- Bar per class: none signed before the run. Define one with the officers.
- Never-acceptable error, as a candidate: a confidently wrong answer on a sanctions or escalation step, or a citation that doesn't support the answer.

**Suggested wording for the inventory and go-live pack:**
> Prototype baseline: 38/40 correct (95%, 95% Wilson interval about 84%–99%) on a 40-question expert-written suite, measured on [model/version] on [date]. Not validated. Release evidence to be produced by running the frozen suite on the engineering build via the bank's gateway before go-live.

**Engineering reuses:** the questions and expert answers as the suite seed, the prompt as configuration, the failure cases.
**Engineering must:**
- fix the grader and the pass bar before running
- rerun on the gateway's model version
- extend the suite, including questions whose correct answer is "not in the library"
- put prompt, model ID and parameters under change control, so any model or gateway update triggers a rerun

**Autonomy and gate to the next level:** to confirm. Proposed: answer with citation, a human decides.
**Trace fields logged by the prototype:** to confirm.

## 5. Intended vs implemented
Meant to answer with citations. Actual behaviour to confirm:
- refusal when the library has no answer
- whether citations are checked against the answer
- handling of superseded policies
- shortcuts such as keys in a file, no login, prompt-only guardrails, whole-library access

Failure modes seen: the two wrong answers.

## 6. Engineering rebuild list
- **Rebuild:**
  - authentication and per-user document access
  - secrets in a vault
  - gateway model access
  - logging and retention
  - guardrails in code (a citation must exist in the retrieved text)
  - retrieval with policy version and effective-date handling
- **Reuse as spec:** prompt; eval suite as seed.
- **Drop:** prototype code.
- **Never carried over:** prototype credentials.

## 7. Draft register entry
- Identifier, location, owner: to confirm.
- Classification: proposed EUC tier 3.
- Business function: AML and sanctions procedure support.
- Dependencies: policy library, bank model gateway.
- Model, version and provider: to confirm.
- Prompt version and autonomy level: to confirm.
- Data categories: internal documents (confirm no personal data).
- Eval suite and baseline date: 40 questions, date to confirm.
- Kill or review date: to confirm.

## 8. AI Act flag (for `ai-act-classification`)
The bank built this for its own use on a vendor model, so it may be the provider. Annex III relevance depends on whether outputs feed decisions about people. To confirm.

## 9. Questions
- **IT risk:**
  - Is the prototype in the asset inventory?
  - What credentials does it use, and where does it run?
  - Is operational use before January accepted? If so, until what date, in weeks and not "until the rebuild"?
- **Model risk:**
  - Is this a model under the policy, and does the bank's tiering put it above tier 3?
  - Who validates it, and when?
  - What bar and sample size do you require?
  - Will a rerun of the frozen suite on the gateway build count as release evidence?
- **Counsel:** provider role; Annex III.
- **DPO:** personal data in the library or the questions? Is a DPIA needed?
- **Sponsor:** will you accept the wording above instead of "accuracy 95%, validated"?

This file is a proposal and a list of questions. IT risk, model risk and counsel decide.

---

If you tell me the missing facts, or turn Write back on, I can fill in the "to confirm" fields and save the file.