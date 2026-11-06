---
name: cse-consultation
description: Check whether deploying an AI tool in a French company means informing or consulting the CSE, and prepare the file. Use for any AI tool that touches employees' work in France.
stage: govern
version: 0.2.0
last_verified: 2026-11-04
depends_on: [ai-act-classification, ai-adoption-plan]
feeds: [process-ai-redesign, ai-adoption-plan]
autonomy_relevant: true
sources: [code-du-travail, cnil-employee-monitoring, fr-cse-case-law, repo-chanmeng]
eval_threshold: 0.90
status: tested
---

# cse-consultation

## When to use
- An AI tool will be used by, or applied to, employees of a company in France: drafting assistant, copilot, agent, scoring, routing of work.
- The tool can log, measure or evaluate what individual employees do.
- The tool changes tasks, the organisation of work, workload or working conditions, or a step moves up the autonomy ladder (references/autonomy-ladder.md).
- A pilot with real employees is about to start, or a go-live date is set.
- Do not use for the AI Act classification itself: that is `ai-act-classification`.
- Do not use for the GDPR impact assessment: that is `dpia-prescreen`.
- Do not use for employees outside France: this covers French law only. In a group, apply it to the staff in France and send works-council questions elsewhere to local counsel, without applying French thresholds there.

## Inputs
Mandatory: headcount in France (and for how long it has been at that level), what the tool does and who uses it, what it records about each user, whether it changes tasks or the organisation of work, the planned pilot and go-live dates.
Ask if missing: whether a CSE exists and its committees, any company agreement on consultation timelines, the AI Act classification (`ai-act-classification`), the GDPR impact assessment status.
Exact article wording and thresholds: references/code-du-travail-fr.md (French annex).

## Method
1. **Find the CSE regime from the headcount.** No CSE duty until the company has had at least 11 employees for 12 consecutive months (L2311-2). From 11 to 49: a CSE with limited attributions (L2312-5): grievances, health and safety, and each member's alert right on disproportionate infringements of rights, health or individual liberties (L2312-59); no duty to inform or consult it on new technologies or monitoring. From 50 employees for 12 consecutive months: full information and consultation duties (L2312-1, L2312-8), with a transition period set by L2312-2. From 300 employees (company or establishment): a health, safety and working conditions committee (CSSCT, L2315-36) prepares the work but never gives the opinion (L2315-38). State which regime applies and why.
2. **Describe what the tool does to work**, step by step: tasks added, removed or changed; who decides; pace and workload; skills needed; jobs affected. A new technology or a significant change to working conditions or health and safety triggers consultation from 50 employees (L2312-8, II, 4°).
3. **Screen for monitoring.** Can the tool, as delivered, record or report what an identified employee does (prompts, usage per person, output volumes, quality scores, time stamps)? If yes, take the stricter path whatever the intended use. From 50 employees, the CSE is informed and consulted before the decision to use any means allowing monitoring of employees' activity (L2312-38), even when monitoring is a side capability of a tool built for something else (Cass. soc., 11 Dec. 2019, n° 18-11.792). At any headcount, employees are told before any data about them is collected (L1222-4), and the restriction must be justified and proportionate (L1121-1). From 50 employees, the CSE is also informed before recruitment tools or automated HR processing are introduced or changed (L2312-38); at any headcount, candidates are told (L1221-8, L1221-9). Point to the GDPR impact assessment (`dpia-prescreen`) and the CNIL guidance on employee monitoring.
4. **Set the obligation level**: none, information, or information and consultation, with the article for each. Under 11 employees, recommend informing employees as good practice, and apply L1222-4 if any data about them is collected.
5. **Put consultation before the decision** (L2312-14). A pilot in which the target employees use the tool in their real work is a first implementation, not an experiment (TJ Nanterre, 14 Feb. 2025): only a limited test needed to build the CSE's file may come before the opinion, and once a consultation is open nothing is implemented before it. Generative AI is a new technology under L2312-8 even when its use is optional or employees already used it on their own (TJ Créteil 2025, upheld by CA Paris, 21 May 2026). A missing mandatory consultation is a manifestly unlawful disturbance: the judge orders it and suspends the tool under penalty (Cass. soc., 27 Nov. 2024), and it is the offence of obstruction (délit d'entrave, L2317-1, fine up to EUR 7,500, EUR 37,500 for a company). Case details: references/code-du-travail-fr.md.
6. **List what the file contains** (precise, written information, L2312-15): purpose; how the tool works and its limits; data processed and retention; monitoring capabilities and safeguards; impact on jobs, tasks, workload and working conditions; health and safety; what happens when employees type sensitive content into the tool (their health, harassment, a dispute): who can read it and where it is routed; training plan; timeline; the AI Act classification and the GDPR impact assessment. The employer hands it to the CSE or puts it in the economic, social and environmental database (BDESE) and says so (R2312-5, L2312-21).
7. **Build the timeline backwards from go-live.** Without an agreement (L2312-16, L2312-19), the CSE has one month to give its opinion, two months if an expert is involved, three months if expert reports are commissioned in a consultation held at both central and establishment CSE level; the CSSCT does not extend it (R2312-6). The clock starts when the information is provided or its availability in the BDESE is notified (R2312-5); a CSE that finds it insufficient must go to court before the delay ends (L2312-15). The CSE can appoint an expert for the introduction of a new technology (L2315-94, 2°; 80% paid by the employer, L2315-80). Once the delay expires, the CSE is deemed consulted with a negative opinion (L2312-16). Add the meeting calendar and the time to prepare the file.
8. **List the questions for HR and legal**, each with the facts they need: headcount history, existing agreements, monitoring features that can be switched off, whether the pilot counts as deployment. From 50 employees, for anything planned before the opinion, ask for these facts: who uses it and how many of the target employees; real work or test data; does output reach real clients or files; is a consultation already open. They are facts for legal, not a safe harbour: the memo still holds the pilot until the opinion. Also ask counsel whether a harassment or health report typed into the tool puts the employer on notice.
9. **Outline the CSE presentation** in plain language: what the tool does and does not do, what changes for whom, what is recorded and who sees it, safeguards, training, how employees can raise concerns.
10. **State freshness.** If `last_verified` is more than 90 days old, say so at the top of the memo.

## Output
A memo following `templates/cse-memo.md`: regime and obligation level with articles, monitoring screen, file contents, timeline with legal delays, questions for HR and legal, presentation outline. Written in the user's language, with article references as in the Code (L2312-8). It ends with: "HR and legal decide; this memo prepares their decision." (in French: "Les RH et le juridique décident ; ce mémo prépare leur décision.")

## Rules and red lines
- Consultation precedes deployment, never follows. A pilot in which the target employees use the tool in their real work counts as deployment.
- Any capability to monitor individual employees triggers the stricter path, even if the company says it will not use it.
- Never state that no step is needed without the headcount regime and the article behind it.
- Every obligation cites its article of the Code du travail.
- The memo states that HR and legal decide.
- Never redefine autonomy levels: use references/autonomy-ladder.md.

## Links
references/code-du-travail-fr.md · references/autonomy-ladder.md · ai-act-classification · dpia-prescreen · ai-adoption-plan

## Sources
- code-du-travail: articles as cited, French annex in references/code-du-travail-fr.md.
- cnil-employee-monitoring: CNIL guidance on monitoring employees' activity (July 2026) and its HR referential.
- repo-chanmeng: the idea of asking what happens to sensitive employee messages, and the works-council caveat for other countries (ideas only, own words).
- fr-cse-case-law: Cass. soc. 27 Nov. 2024 and 11 Dec. 2019; interim decisions on AI tools (TJ Nanterre 2025 and 2026, TJ Créteil 2025 upheld by CA Paris 2026, TJ Paris 2025 and 2026).
