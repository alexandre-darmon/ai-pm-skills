# KPI spec and monthly review: employee assistant

## 1. What you can and can't compute today

| Item | Status |
|---|---|
| Volume: about 9,000 conversations a month | Known in total. **Not split by KB or use case**, which needs classification. |
| Quality: 84% of 200 answers correct | **Interim, blended only.** There is no per-KB figure, and I don't know how the 200 were split across KBs. |
| Adoption: 3,500 eligible employees in 3 countries | The denominator is known. **Active users per country are not provided.** |
| Run cost: 1,900 EUR a month | Known. I don't know which lines it includes (tokens, infra, licences). Review time is not in it. |
| Stale-answer rate | **Not computable.** It needs the review date and version of each document that an answer cites. |
| Unit value per outcome | **Missing.** No gain or ROI figure is stated. |

Cost per correct outcome right now, as a rough number: 1,900 ÷ (9,000 × 0.84) = **about 0.25 EUR**. It divides by successes, not by conversations. It rests on a blended 84% and on "correct answer" standing in for "outcome", so don't use it in a decision yet. Per KB it will differ.

The 84% likely hides a spread. HR was reviewed recently and should score high. IT hasn't had a full review in 14 months and the ticketing tool changed in the spring. Travel and expenses had half its documents updated after the September policy change, so old and new versions may contradict each other. A high HR score can pull the blended figure up and mask a failing IT or travel KB. That's why every KPI below is reported per KB.

## 2. Instrumentation to add

Each trace needs:
- `trace_id`, `timestamp`, `user_id` (pseudonymised), `country`
- `use_case` and the KBs consulted
- the document IDs and versions cited in the answer
- tokens and cost, using the OpenTelemetry `gen_ai.*` attributes

Each outcome is logged as an event attached to the trace:
- `outcome_id`, `trace_id`, `use_case`
- `result`: success, failure, escalated or abandoned
- `value_eur`: left empty until a unit value is sourced
- `source`: user, system or reviewer
- `timestamp`

Each KB also needs an inventory table with owner, last review date and the age of its oldest active document. For travel and expenses, add a flag for documents superseded in September.

Until outcomes are logged, quality comes from the sampled review below. It is **interim**. Thumbs-up is not used as a quality source.

## 3. KPI table

| Family | Definition and formula | Source | Grain | Refresh | Owner | Status |
|---|---|---|---|---|---|---|
| Volume | Conversations by use case and KB | Traces plus classification | Use case × KB × country | Weekly | Assistant product owner | Total only. Split needs classification. |
| Quality | Correct sampled answers ÷ sampled answers, with n | Reviewed sample | One line per KB (HR, IT, T&E), plus country within the sample | Monthly, with a weekly sample | One domain reviewer per KB | Interim. Blended 84%, n=200. |
| Adoption | Active users ÷ eligible users, as a weekly curve, plus the share returning within 4 weeks | Traces and HR headcount | Country (3 populations) | Weekly | Product owner | Eligible known. Active users missing. |
| Cost per correct outcome | Run cost ÷ (volume × quality), per KB. State whether review time is included. | Finance, traces, review | KB | Monthly | Product owner with finance | About 0.25 EUR blended, not reliable yet |
| Stale-answer rate | Sampled answers citing a document past its review date or superseded ÷ sampled answers. Show the age of each KB's oldest active document beside it. | Reviewed sample plus document inventory | KB | Monthly | KB owners | Not computable. Needs document IDs and versions in traces. |

Every usage KPI (volume, adoption) sits next to the quality line at the same grain. There is no blended quality score on the dashboard.

## 4. Monthly sample

The sample is about 210 conversations a month, and it is stratified, not random across the whole pool:

| KB | Sample | Why |
|---|---|---|
| HR | 50 | Recently reviewed, lower risk. |
| IT | 80 | 14 months without a full review, and the tool changed. |
| Travel and expenses | 80 | Policy changed in September and half the documents were updated. |

- **Margin of error:** at n=80 it is about ±8 points. Any line with n<30 is flagged **indicative**.
- **Country coverage:** make sure each country appears in the sample. The September travel policy or the IT tooling may differ by country, which I can't tell from what you gave me.
- **Rubric:** reviewers grade against a written rubric: correct, incorrect, outdated or incomplete. They also record whether the cited document was stale. Double-grade 10% of the sample to check that reviewers agree.
- **First month:** weight toward the two risky KBs. The baseline of the first stratified review replaces the 84% as the reference.

Review time is change cost. Track the hours, since the review is part of what the assistant costs to run well.

## 5. One-page dashboard

1. Volume by use case and KB
2. Quality by KB, with threshold and n
3. Adoption curve for each of the 3 countries
4. Cost per correct outcome by KB
5. Stale-answer rate by KB, with the oldest active document's age

Each line shows its threshold and its sample size. Targets are for you to set. I won't invent thresholds, but I'd propose setting them after the first stratified month, not before.

## 6. Monthly review template

Attendees: the product owner, the three KB owners, and finance for cost.

For each KPI, record this month, last month, target and the decision taken:

| KPI | This month | Last month | Target | Decision | Owner and date |
|---|---|---|---|---|---|
| Quality: HR (n=) | | | | | |
| Quality: IT (n=) | | | | | |
| Quality: T&E (n=) | | | | | |
| Stale-answer rate per KB | | | | | |
| Adoption per country | | | | | |
| Cost per correct outcome per KB | | | | | |
| Volume by use case | | | | | |

Agenda:
1. **Failures.** Review the incorrect answers by cause: stale document, missing document, retrieval, model.
2. **KB actions.** Each action has a named KB owner and a date. Likely first actions:
   - IT: full review, with the ticketing procedures first.
   - T&E: remove or retire the pre-September documents still in the index.
3. **Review cadence.** Move any KB past its review date onto a schedule, for example every 6 months for IT.
4. **Autonomy decisions.** Quality holding steady is the evidence for a step's L2 gate. Say which step it gates and since when the KPI has held, with sample sizes. It can't count until you have at least 2 to 3 months of per-KB data.
5. **Economics.** Volume × quality per use case goes to the ROI work. Don't state a gain until a unit value is sourced, then show all of volume × quality × unit value − run cost − change cost.

## 7. What I need from you

- The split of the 200 reviewed answers by KB, or the review file itself.
- Active users per country.
- What the 1,900 EUR covers.
- Whether the traces carry document IDs and versions today.
- Who owns each KB.

I haven't created any files. I can write this out as a document if you want it in the repo.