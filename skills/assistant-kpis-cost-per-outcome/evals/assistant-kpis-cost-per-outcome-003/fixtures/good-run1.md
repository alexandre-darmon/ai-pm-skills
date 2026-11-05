# KPI spec and monthly review: employee assistant

## 1. What the 84% can and can't tell you

- **It is a blended number.** With 200 answers, the margin is about ±5 points (79–89%), and I don't know how the sample split across the three KBs. Two of the KBs have a known reason to be weak, so 84% could hide a failing KB behind a strong HR one. I'm treating it as a baseline, not a KPI.
- **Cost per correct answer is about 0.25 EUR.** That is 1,900 ÷ (9,000 × 0.84) = 1,900 ÷ 7,560. It is a run-cost figure only, and it moves with quality: at 70% it would be 0.30 EUR.
- **Hypotheses to test, not findings.** HR (240 docs, reviewed within 3 months) should be fine. IT (14 months since the last full review, ticketing tool changed in the spring) probably gives stale answers about the old tool. Travel and expenses (September policy change, half the documents updated) probably gives wrong answers where old and new versions coexist.

## 2. Source inventory

Please confirm which of these fields your traces contain.

| Field | Needed for | Status |
|---|---|---|
| trace_id, timestamp, tokens, cost | Volume, cost | Assumed present, to confirm |
| Use case / KB per conversation | Volume and quality by KB | **Unknown.** If missing, run `conversation-analysis` classification. |
| User ID (pseudonymised) and country | Adoption by country | **Unknown.** Needed for the 3 populations. |
| Retrieved document IDs per answer | Stale-answer rate | **Unknown.** Without them, stale rate can only be judged by the reviewer. |
| Per-document last-review date and version, per KB owner | Stale-answer rate | Exists for HR; needs an extract for IT and T&E. |
| Outcome event | Outcome rate | **Not computable yet.** See below. |
| Thumbs-up | – | Not a quality source. |

**Outcome event.** Add this to each trace: `outcome_id`, `trace_id`, `use_case`, `result` (success / failure / escalated / abandoned), `value_eur` (empty until someone sources a unit value), `source` (user / system / reviewer), `timestamp`. Use `gen_ai.*` attribute names for the model and token fields. Until outcomes are logged, quality comes from the sampled review below and is labelled **interim**.

## 3. KPI table

| Family | KPI and formula | Grain | Refresh | Owner | Status |
|---|---|---|---|---|---|
| Volume | Conversations by use case and KB, from traces | KB × country × month | Weekly | Assistant product owner | Computable if KB/use case is classified |
| Quality (interim) | Sampled answers judged correct ÷ sampled answers, shown with n and ± margin | **One line per KB**, plus country as a secondary cut | Monthly | KB owner (HR, IT, T&E) with a reviewer | Computable now. The existing 200-answer review shows 84% blended, with no per-KB split. |
| Adoption | Active users ÷ eligible users, weekly curve, plus the share returning within 4 weeks | Country (3), against 3,500 eligible | Weekly | Product owner | Needs user ID and country |
| Cost per correct outcome | Run cost ÷ (volume × quality). Numerator is run cost only (tokens, infra, licences). Review time is reported separately as change cost. | Total and per KB (if cost can be allocated) | Monthly | Product owner with Finance | Baseline 0.25 EUR, blended and interim |
| Stale-answer rate | Sampled answers relying on a document past its review date or superseded ÷ sampled answers, next to the age of each KB's oldest active document | Per KB | Monthly | KB owner | Needs retrieved doc IDs and review dates |

Every usage KPI (volume, adoption) is shown next to the quality KPI at the same grain. Neither appears alone.

## 4. Monthly review sample

The review sample is stratified by KB, not proportional. Proportional sampling would leave T&E with too few answers to read.

| KB | Answers/month | Why |
|---|---|---|
| IT | 70 | Suspected weakest, oldest content |
| Travel and expenses | 70 | Policy changed, so mixed versions are likely |
| HR | 50 | Recently reviewed, stable |
| **Total** | **190**, rounded to 200 | Same effort as last quarter's review |

- **Precision is limited.** At n = 50–70, the margin is about ±10–12 points. Treat any KB line under 30 as indicative. For decisions, pool two months, or raise a KB's sample when its line is close to its threshold.
- **Add a floor per country.** Take at least 10 answers per country within each KB, so a country-specific policy error can't hide.
- **Reviewers grade against a written rubric.** The rubric is correct / incorrect / correct but stale. Reviewers are domain staff, not the KB authors. Double-grade 10% to check agreement.
- **Each answer also gets a stale flag.** The reviewer records the cited document and its review date, which feeds the stale-answer rate.

## 5. Dashboard (one page)

1. Volume by use case and KB, month over month.
2. Quality by KB: three lines, each with n, margin and threshold. No blended headline.
3. Adoption curve by country, with the 4-week return share.
4. Cost per correct outcome, with the cost lines stated.
5. Stale-answer rate by KB, with the oldest-document age.

## 6. Monthly review template

Hold it for 45 minutes with the product owner, the three KB owners and the sponsor.

1. **KPIs against last month and target.** One row per KB: quality (n, margin), stale rate, volume, oldest-document age.
2. **Decisions.** One line each, such as "IT: re-review the 40 ticketing-tool documents by 15 Dec."
3. **KB actions.** Each has a named owner and a date.
4. **Sample review.** Note disagreements between reviewers and rubric changes.
5. **Gate evidence.** State which assistant steps the quality KPI supports for the L2 gate, and for how many consecutive months it has held, with n. Nothing qualifies yet because there is no per-KB history.
6. **Economics.** Hand volume × quality per use case to `ai-roi-quantification`. No gain or ROI figure is stated until a unit value is sourced. A figure needs volume × quality × unit value − run cost − change cost.

## 7. Targets

I haven't invented targets. After the first per-KB review month, set thresholds per KB with the sponsor. Because of the suspected IT and T&E issues, expect the first months to show a gap. In the meantime, the useful control is a stale-answer threshold: no KB should have active documents past their review date.

## 8. Next steps

1. Confirm which trace fields exist, especially KB, country, user ID and retrieved doc IDs.
2. Re-cut last quarter's 200 answers by KB if they were tagged. That gives a per-KB baseline right away.
3. Get the IT and T&E document lists with review dates and versions, and flag documents that coexist in old and new versions.
4. Run the first stratified review within the next month.
5. Decide who logs the outcome event, and what counts as success for each use case.

I didn't have access to the skill's template files (`templates/kpi-spec.md`, `references/roi-model.md`). The structure above follows the skill's method. If you'd like it as a file in that template, I can write it out.