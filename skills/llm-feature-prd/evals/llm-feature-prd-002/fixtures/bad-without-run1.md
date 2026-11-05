I couldn't save the PRD to a file because the Write tool is disabled in this session, so it's below. I can save it once Write is available.

# PRD: Refund Agent (Customer Service)

**Status:** Draft v1 · 2026-11-05 · **Target:** live in 2 sprints

## 1. Problem
About 40,000 refund requests a month are handled by 6 people, with a 3-day average resolution time. Most of that work is routine: read the request, check the order, click refund in the back office.

## 2. Goals and metrics
| Metric | Today | Target |
|---|---|---|
| Resolution time (request received → refund issued in back office) | 3 days | Same day (p90 < 4 h on auto-resolved cases) |
| Refund error rate | not baselined | < 1% of refunds issued |
| Variable cost per request | n/a | < 0.10 EUR (about 4,000 EUR/month at full volume) |
| Auto-resolution rate | 0% | ≥ 60% by end of ramp (assumption, to validate in shadow mode) |

- **Resolution time** stops when the refund is issued. Card settlement time is excluded because we don't control it.
- **Refund error** means a wrong amount, wrong order or line, duplicate, or refund the policy doesn't allow. We measure it with a weekly audited random sample plus all disputes and finance reversals.
- **Baseline:** we must measure the current human error rate the same way. Without it, "< 1%" has no reference point.

## 3. Scope
**In scope**
- Read French refund requests from the existing channel.
- Identify the customer and order, check eligibility, and issue the refund through the back office API, capped at the order amount (or the remaining refundable amount).
- Reply to the customer in French.
- Escalate to a human with a structured summary when the agent isn't confident or the case isn't eligible.

**Out of scope for v1**
- Other languages, which go to humans.
- Goodwill gestures, compensation, chargebacks and B2B credit notes.
- Policy changes.
- Any back office action other than refunds.

## 4. Key design decisions
1. **The agent approves or escalates. It never denies.** Rejections go to a human, which limits the harm from wrong refusals and avoids fully automated adverse decisions under GDPR Art. 22.
2. **Hard limits live in code, not in the prompt.** The refund tool wrapper rejects a call when any of these is true:
   - the amount exceeds what's still refundable;
   - the order doesn't belong to the verified customer;
   - a refund is already in flight (idempotency key per order line);
   - the order is outside the refund window.
3. **Risk gates force escalation:**
   - fraud or risk flag;
   - high refund velocity;
   - new account with a high-value order;
   - claimed data doesn't match the order record;
   - complaint or legal wording;
   - low model confidence.
4. **Recommended amount ceiling at launch.** You asked for refunds up to the order amount. I'd still start with auto-approval up to a threshold X EUR and raise it as audited error data comes in. This is the main business decision to confirm (see open questions).
5. **Full audit trail** for every decision: request, data read, rule applied, tool call, reply.
6. **Kill switch and feature flags** by reason, amount band and product.

## 5. Functional requirements
- **FR1 Intake:** receive requests from the current channel.
- **FR2 Classify:** non-refund and non-French requests go to the human queue untouched.
- **FR3 Extract:** order reference, reason, requested amount and items.
- **FR4 Verify:** the requester must match the order owner, otherwise escalate.
- **FR5 Decide:** policy rules (window, status, refunded so far) are deterministic code. The LLM only interprets free text.
- **FR6 Act:** call the refund API with an idempotency key, then read back the record to confirm amount and status.
- **FR7 Reply:** send a French message with amount, expected funds timing and a way to reach a human. Disclose that it's an automated assistant (AI Act Art. 50).
- **FR8 Escalate:** create a human ticket with summary, data pulled, reason and suggested action.
- **FR9 Monitor:** dashboard for volume, auto-resolution, resolution time, cost per request, escalation reasons and error samples.

## 6. Non-functional requirements
- **EU hosting:** inference, storage, logs, queues and observability tools all in EU regions. For example, Claude through AWS Bedrock or Google Vertex AI in an EU region. Security and legal must verify region and terms before build.
- **GDPR:** DPAs with processors, a DPIA, minimal PII in prompts, a log retention policy, and no training on customer data.
- **French only:** the eval set must include informal, misspelled and abbreviated French.
- **Cost:**
  - Use a small model for classify and extract, deterministic code for policy and API calls, and a larger model only for ambiguous cases.
  - I expect a few cents per request, well under the cap, but this must be measured from day one. Long threads and attachments can inflate tokens.
- **Latency:** under 2 minutes from intake to refund on auto-resolved cases.
- **Reliability:** if the model or back office API fails, the request falls back to the human queue with no silent drops. Retries are idempotent.

## 7. Rollout (two sprints)
**Before sprint 1 (week 0)**
- Confirm back office API access and a sandbox.
- Get the written refund policy.
- Pull 2–3k historical resolved requests.
- Get legal and security sign-off on EU hosting.

**Sprint 1: build and shadow**
- Build intake, extraction, verification, policy checks, the guarded refund tool, escalation and logging.
- Build a French eval set of at least 500 labelled cases.
- Run in **shadow mode** on live traffic: the agent decides and drafts but takes no action.
- **Exit gate:**
  - at least 98% agreement with humans on cases it would auto-approve;
  - zero guardrail violations;
  - cost under 0.10 EUR per request.

**Sprint 2: controlled live and ramp**
- Go live on the lowest-risk segment (low amounts, delivered orders, clear reasons).
- Ramp from 10% to 25%, 50% and 100% of the eligible segment. Each step needs a week with error rate under 1% on audited samples.
- Audit 100% of agent refunds in week 1, then a statistical sample.
- Keep the team's capacity unchanged until the metrics are stable.

"Live in two sprints" is realistic as production on a controlled share with the ramp underway. Full volume and the full amount range depend on passing the gates, and I'd advise against skipping them.

## 8. Risks
| Risk | Mitigation |
|---|---|
| Fraud and prompt injection in customer messages | Code-level guardrails, ownership checks, risk gates, velocity limits, customer text treated as untrusted |
| Every wrong refund is a direct loss | Launch ceiling, audit sampling, read-back verification, kill switch |
| Policy is ambiguous or undocumented | Codify it with the support lead in week 0 and escalate anything uncovered |
| Back office API has no idempotency or sandbox | Wrapper-level dedup, and flag it as a week-0 blocker |
| The 1% target may be stricter than humans achieve today | Measure the human baseline in shadow mode |
| Team change management (6 people) | Move them to escalations, QA and policy tuning, and involve them in the eval set |
| GDPR Art. 22 and AI Act transparency | Agent never denies, AI disclosure in replies, human recourse in every message |

## 9. Open questions (needed before sprint 1)
1. Which channels do requests come in on, and is there an authenticated customer context?
2. Does the back office have a refund API, a sandbox, idempotency and a refund history endpoint? If not, how do we act "directly"? I don't recommend UI automation.
3. Is the refund policy written down, and who owns it?
4. Will the business accept an auto-approval ceiling at launch? What is the distribution of order amounts?
5. What are the current human error rate and the share of requests that aren't simple refunds?
6. Which EU-hosted model provider and region do security and legal accept?
7. Who signs off on the risk budget for refund losses caused by the agent?

## 10. Later
Proactive status updates, additional languages, partial-refund handling, and feeding escalation data back into policy improvements.