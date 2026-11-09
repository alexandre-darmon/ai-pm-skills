# Process redesign: KYC new-customer file review

## Current process

Baseline is 9,000 files a month, 25 people, and about 8% of files with an issue. That is well under the 25% threshold, so exception handling doesn't need redesigning first.

| Step | Volume/month | Time per file | Hours/month | Exception rate |
| --- | --- | --- | --- | --- |
| 1. Read ID, proof of address and income documents; key data into the core system | 9,000 | 12 min | 1,800 | Not measured (unreadable, mismatched or missing documents) |
| 2. Sanctions and internal-rules check | 9,000 | 6 min | 900 | Not measured |
| 3. Open the account or request more documents | 9,000 | 3 min | 450 | Not measured |
| **Total** | | **21 min** | **3,150** | **~8% (720 files), not split by step** |

Two things need measuring before any step goes above L2:
- **Where the 8% appears.** It could be unreadable documents at step 1, hits at step 2, or incomplete files at step 3.
- **How long an issue file takes.** The 21 minutes is probably an average that includes issue files.

Capacity: 25 people at an assumed 140 productive hours a month is about 3,500 hours. Replace the 140 with the real figure. Current utilisation is therefore about 90%.

## Step table

| Step | Current level | Target level | Why not L+1 | Gate to reach target | Approach |
| --- | --- | --- | --- | --- | --- |
| 1. Extract and key data | L0 | **L3** on files that pass validation rules; L2 on the rest | L4 would load unchecked data into the core system, and errors flow into every later step | L1: golden set of labelled files, field-level accuracy at or above threshold (per field type), tested on 5 reviewers. L2: L1 in production 4 weeks, error rate stable. L3: shadow run of 2 weeks or more, with a known false-pass rate on the validation rules | **LLM/vision extraction plus rules.** Rules do the validation: ID-number checksums, document expiry, name and date matching across documents. Workflow, not agent |
| 2a. Sanctions and PEP screening | Existing tooling, human-reviewed (L1) | **L3** for no-hit files; hits stay with a human | A sanctions disposition has legal effect, so hits stay at L2 | Rules engine tested against a known-hit test set, with zero missed hits. Shadow run of 2 weeks or more against current human results | **Rule** (deterministic list matching). No model. An LLM may only summarise hits for the analyst (L1) |
| 2b. Internal rules check | L0 | **L3** for files where every rule passes | An automatic failure would refuse a customer without a human | Rules encoded and tested against 100% of historical files. Shadow run of 2 weeks or more | **Rule** |
| 3. Decide: open or request documents | L0 | **L2** (AI prepares a recommendation and a draft document request; human validates 100%) | Opening or refusing an account is a decision with legal and financial effect on a person (red line). L3 is not allowed | L1: golden set of past decisions, agreement with human decisions at or above threshold. L2: L1 in production 4 weeks, quality KPI stable, output guardrails tested | **Workflow plus LLM** for drafting only. The recommendation comes from the rule output |

L5 is excluded everywhere: this process has exceptions and decisions on people.

## Scenarios

The time-per-file figures below are **hypotheses** for a projection. Replace them with a time study on 5 reviewers before the COO sees a € figure.

| | Conservative | Target | Ambitious |
| --- | --- | --- | --- |
| Levels | S1 L2, S2 unchanged, S3 L0 | S1 L2, S2 L3 on clean files, S3 L2 | S1 L3 on about 70% of files, S2 L3, S3 L2 |
| Hypothesised minutes per file | 5 + 6 + 3 = 14 | 5 + 1.5 + 2 = 8.5 | about 1.9 + 1 + 1.5 = 4.4 |
| Reviewer hours/month | 2,100 | 1,275 | 660 |
| Hours freed vs baseline | 1,050 (33%) | 1,875 (60%) | 2,490 (79%) |

**Five ROI lines (per month, projection, no baseline yet):**

| Line | Value |
| --- | --- |
| Volume | 9,000 files (less any files bounced back to humans) |
| Quality | Share of AI outputs accepted without correction. Unknown. Measured on the golden set and a production sample. Do not use thumbs-up |
| Unit value | Minutes saved × loaded hourly cost of a KYC analyst. Cost is to be sourced from Finance. Plus error cost avoided, such as rework and regulatory findings, if quantifiable |
| Run cost | Per-file model and OCR cost × 9,000, plus infra, eval upkeep, monitoring and rules maintenance. Not yet measured. Do not take it from the demo |
| Change cost | Build, spread over 24 months (the likely life before regulations or models change). Plus golden-set labelling, training, and reviewer hours (below) |

**Capacity is not cash.** The freed hours are capacity until someone removes a cost or names the work they are redeployed to. For example, redeploy them to the backlog of issue files, to quality control or to onboarding speed. Show the two separately.

**Human fallback** (items per period × time per item = reviewer hours, against hours left):

| | Conservative | Target | Ambitious |
| --- | --- | --- | --- |
| Reviewer hours/month | 2,100 | 1,275 | 660 |
| Against ~3,500 hours today | Leaves 1,400 | Leaves 2,225 | Leaves 2,840 |

- **Queue owner:** KYC team lead.
- **SLA:** to set from the current turnaround. Proposed starting point is one business day for clean files and two for issue files.
- **Timeout:** the file stays pending and escalates to the team lead. An account is never opened by default.
- **Staffing:** at 140 hours a person, the target scenario needs about 9 people for review. If a scenario can't be staffed, lower the level.
- **Exception time:** the 720 issue files a month aren't sized separately. Measure their time per item.

## Trade-offs

| | Conservative | Target | Ambitious |
| --- | --- | --- | --- |
| Cost per correct outcome | Highest, but least build | Mid | Lowest if quality holds. Extra eval and monitoring cost |
| Risk | Low. Humans check every extraction | Medium. A false pass on a rule goes unseen except in samples | Highest. Extraction errors on the 70% with sampling only |
| Reversibility | Trivial | Easy: demote S2 to L2 | Easy, but staff skills and headcount may have moved on |
| Obligations | Logging, DPIA pre-screen, AI literacy | Same, plus incident playbook and CSE consultation | Same as target, with a closer AML-regulator conversation |

**Recommendation:** start with the conservative scenario, then move to the target one step at a time behind the gates. Don't commit to the ambitious scenario until the measured error rate supports it.

## Migration path and gates

Each move is one level at a time, behind its gate from `build-evals` and `release-to-production`.

1. S1: L0 → L1 → L2 → L3.
2. S2a and S2b: shadow run first, then L3.
3. S3: L0 → L1 → L2 and stay there.

| Step | Demotion trigger (observed value) | Who acts |
| --- | --- | --- |
| 1. Extraction | Field error rate above the gate threshold on the weekly sample, or any rise after a model change | KYC team lead demotes to L2 immediately |
| 2a. Sanctions | Any missed hit found in a sample or audit | Compliance officer; demote to L2 and open an incident |
| 2b. Rules | Disagreement with human review above threshold, or a rules change not yet re-tested | KYC team lead |
| 3. Decision | Agreement with human decisions falls below threshold, or a customer or regulator complaint | Head of KYC |

Moving down needs no approval. The rollback mechanism comes from `release-to-production`.

## Dependencies

- **`ai-act-classification`:** no step is at L4 or above, so it isn't mandatory. Run it anyway, because step 3 supports decisions on persons. If anyone proposes face matching against the ID photo, it becomes a biometric use that is likely high-risk.
- **`cse-consultation`:** required. The reviewers' work changes from keying to validating, and capacity gains may become a headcount question. Don't measure individual reviewers on AI-acceptance rates without consultation.
- **`dpia-prescreen`:** required, because ID documents are personal data. Check where the model is hosted and where files travel.
- **AML/KYC regulation:** confirm with Compliance that the regulator accepts machine-extracted data and automated rule clearance, and what audit evidence it needs.

## Plan and milestones

| When | Milestone | Owner |
| --- | --- | --- |
| Weeks 1–4 | Baseline time study. Split the 8% by step. Pull and label the golden set. Start the CSE consultation and DPIA pre-screen | KYC head, Data/AI lead |
| Weeks 5–8 | S1 L1: extraction suggestions shown to 5 reviewers. Encode S2 rules | AI lead, Compliance |
| Weeks 9–12 | S1 L2 in production. Start the 4-week stability clock. Shadow run S2 | KYC team lead |
| Weeks 13–16 | S3 L1 → L2. First ROI report with a real baseline | KYC head, Finance |
| Month 5+ | Decide on S1 and S2 at L3 from the measured gates, then the ambitious scenario only if the data supports it | COO sponsor |

## Next step

Is a time study feasible in the next month? It would give the baseline, and every € figure above depends on it.