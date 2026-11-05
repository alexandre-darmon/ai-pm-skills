# Employee representatives and AI tools at a 9-person company in Paris

**You have no legal duty to inform or consult employee representatives.** I'm working from the skill's text and haven't opened its Code du travail annex, so check the article references with your lawyer or HR advisor.

## Why

- A social and economic committee (CSE) is only required once a company has had at least 11 employees for 12 consecutive months (L2311-2). At 9 employees you have none, so there is nobody to consult.
- The duty to inform and consult the CSE on new technologies (L2312-8) and on tools that can monitor employees (L2312-38) starts at 50 employees. Even between 11 and 49 employees, the CSE does not have that duty.

## Obligations that still apply at any headcount

1. **Tell employees before any data about them is collected** (L1222-4). Both tools are covered: the copilot can log prompts and usage, and the note-taker records and transcribes people.
2. **Keep monitoring justified and proportionate** (L1121-1). Purpose limitation matters here. A note-taker for minutes is fine. Using the recordings or usage statistics to assess individuals is not, unless you have disclosed it and it is proportionate.
3. **GDPR applies.** You need a legal basis, a privacy notice, retention periods, a data processing agreement with each vendor, and an entry in your processing register. Run the GDPR impact assessment pre-screen (`dpia-prescreen`). Recording video calls with employees is the likelier trigger. The CNIL's employee-monitoring guidance applies.
4. **Recording involves third parties.** Clients, candidates and partners on your calls are not employees. They must be told at the start of the call, and you should get their agreement. Where they object, you must be able to stop the recording.

## What to do before you start

1. **Map what each tool records per person.** Check prompts, usage per user, transcripts, timestamps and who can see them. Switch off any individual tracking you don't need.
2. **Write a short internal policy** covering:
   - purpose;
   - what is recorded and for how long;
   - who has access;
   - an explicit statement that the data won't be used for performance evaluation;
   - no recording of sensitive calls, such as one-to-ones, HR matters or health;
   - what may be pasted into the copilot (no secrets, no client personal data) and confidentiality of source code.
3. **Inform employees in writing before go-live.** Hold a team discussion, give them a way to raise concerns, and offer training. This isn't legally required as consultation, but it is good practice and it lowers the risk of disputes.
4. **Do the vendor checks.** Look at the hosting location and transfers outside the EU, whether your data is used for model training, retention, and deletion on request. For the AI Act classification, run `ai-act-classification`. These tools are probably low-risk, but check that they aren't used for HR decisions.
5. **Add a disclosure line for external participants.** For example: "This call is recorded and transcribed by an AI note-taker."

## Plan for growth

- **At 11 employees for 12 months:** you must set up a CSE with limited attributions (L2312-5). Its members can raise an alert on disproportionate infringements of rights or liberties (L2312-59).
- **At 50 employees for 12 months:** the CSE must be informed and consulted before you deploy new technology (L2312-8) or any means of monitoring activity (L2312-38). Generative AI counts as new technology even if its use is optional.
- **Document your current setup now,** so that later consultation is a matter of updating a file, not starting over.

HR and legal decide; this memo prepares their decision.