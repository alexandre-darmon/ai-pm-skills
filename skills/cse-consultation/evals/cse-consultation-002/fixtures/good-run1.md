# Memo: AI copilot and AI note-taker for a 9-person Paris team

**Short answer:** you have no obligation to inform or consult employee representatives. You still have duties to the employees themselves and to the people who join your calls.

I didn't check the skill's `last_verified` date or the French annex, so confirm the articles below with legal counsel.

## 1. Regime and obligation level

- **Headcount:** 9 employees in France. A CSE (comité social et économique) is only mandatory once a company has had at least 11 employees for 12 consecutive months (L2311-2).
- **Obligation level:** none towards representatives. The information and consultation duties on new technology (L2312-8, II, 4°) and on monitoring means (L2312-38) apply from 50 employees. The 11–49 CSE has limited powers (L2312-5) and no duty to be consulted on these topics.
- **Good practice:** inform and consult your team anyway, since the tools change how people work.
- **Growth:** if you stay at 11 or more for 12 consecutive months, a CSE becomes mandatory. From 50, the full consultation duties apply, and the tools already in place would then be part of the file.

## 2. Monitoring screen

Both tools can record what an identified person does:

- **Copilot:** prompts, usage per person, acceptance rates and time stamps.
- **Note-taker:** who spoke, for how long, what they said, and a full recording and transcript.

The consultation duty is not triggered at your size. These obligations still apply at any headcount:

- **Prior notice to employees (L1222-4):** tell them before any data about them is collected. Say what is recorded, why, who sees it, and for how long.
- **Proportionality (L1121-1):** the restriction on privacy must be justified and proportionate. Switch off per-person analytics, speaker-time metrics and any scoring of individuals. Don't use the transcripts to evaluate people.
- **Recruitment (L1221-8, L1221-9):** if the note-taker joins candidate interviews, candidates must be told beforehand.
- **GDPR and CNIL:** you need a legal basis, a retention period, a processor agreement with the vendors, and a record of processing. Run the `dpia-prescreen` skill. Call recordings and transcripts, with voice data, are likely to need a DPIA.
- **External participants:** clients, partners and candidates on your calls must be told that the call is recorded and transcribed, ideally before the call and again at its start. Don't rely on the bot's name appearing in the participant list.

## 3. What to do before you start

1. **Classify the tools under the AI Act** with `ai-act-classification`. Check in particular that the note-taker has no emotion-detection feature, and plan AI-literacy training for your staff.
2. **Run the `dpia-prescreen` skill** on the note-taker first.
3. **Configure the tools:**
   - Turn off individual usage dashboards and speaker analytics.
   - Set a short retention period for recordings and keep the transcript or minutes only.
   - Check where the vendor stores the data and whether it trains on your data. Opt out of training.
   - Don't let the bot join sensitive calls such as HR, one-to-ones and legal matters.
4. **Write a short internal charter** covering permitted uses, no use for performance evaluation, retention, and how to ask a call to go unrecorded.
5. **Inform employees in writing before go-live** (L1222-4) and hold a team discussion. A pilot with real work counts as deployment, so inform first.
6. **Add a recording notice** to your call invitations and to the bot's join message.
7. **Check client contracts** for confidentiality clauses that restrict recording or sending data to third-party AI vendors. This matters for a software startup.
8. **Keep a record of these steps.** If a CSE is created later, you'll need the file anyway.

## 4. Questions for HR and legal

- Does any employee-count history put you near 11 for a CSE? Do you have any agreement or contract clause on monitoring?
- Which vendor features can be switched off, and does the vendor use your data for training?
- Do the calls include candidates, clients under NDA, or special-category data?
- Is there an employment-contract or house-rules update needed to reflect the new tools?

HR and legal decide; this memo prepares their decision.