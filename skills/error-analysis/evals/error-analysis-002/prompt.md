---
name: error-analysis-002
description: Twenty-five free-text notes an HR policy lead wrote on thumbs-down conversations of an HR assistant, to be turned into eval categories (source - anonymised European group HR brief, 2026)
tags: [error-analysis, p1, edge-case]
expected_outcome: Groups the notes into failure modes with pass/fail definitions and counts (wrong-country policy 7, T19 counted once on its first upstream failure), sends specification failures to a fix rather than a judge, prefers code checks where they decide, flags the salary disclosure whatever its count, says the thumbs-down sample gives no rate and needs a random draw, and labels the taxonomy provisional until saturation.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our HR assistant answers employee questions on leave, pay and policies for a group with entities in France, Belgium and Germany, about 6,000 conversations a month. Our HR policy lead read the 25 conversations employees gave a thumbs-down in October and wrote a note on each:

- T01: Belgian employee asked about carrying over leave. Answer gave the French rule.
- T02: Answer correct, but no link to the policy page. Employee asked "where is this written?"
- T03: Said 12 days left; the HR system shows 9. It added the current month twice.
- T04: German employee, parental leave: answered with the French rules.
- T05: Quoted the 2025 remote-work policy (2 days a week). The 2026 policy (3 days) is not loaded.
- T06: Invented a 300 EUR "wellbeing bonus" that exists nowhere.
- T07: Employee disputes a payroll deduction; the assistant argued with him instead of pointing to his HR business partner.
- T08: 40 lines for a yes/no question on whether a training day counts as working time.
- T09: Belgian employee, deadline for a sick-leave certificate: gave the French 48-hour rule.
- T10: Pro-rata leave for a part-time employee computed on 5 days a week instead of 3.
- T11: Correct answer, no link to the policy.
- T12: Asked for a colleague's salary band and got it.
- T13: French employee got the Belgian mobility budget rules.
- T14: Old 2025 meal-voucher amount; the 2026 grid is not loaded.
- T15: Employee asked twice; the assistant repeated the same answer instead of asking which contract he has.
- T16: German employee, notice period: French rule.
- T17: No link to the policy.
- T18: Leave balance wrong: counted a public holiday as a leave day.
- T19: Retrieved the French policy for a Belgian employee, then computed the days from it, then signed off nicely. Days wrong.
- T20: Expense refusal disputed; the assistant said "the decision is final" instead of pointing to the HR business partner.
- T21: Invented a rule: "you can carry over up to 10 days". No policy says that.
- T22: Question asked in German, answered in English.
- T23: 2025 travel policy (old per diem); the 2026 one is not loaded.
- T24: Belgian employee, bridge days: French rule.
- T25: 35-line answer; the employee left without reading.

Context: the assistant is not told which country the employee works in; it searches the policies of all three countries. Its system prompt asks for "short, friendly answers in English" and says nothing about sources or disputes. The 2026 policies published since March have not been loaded yet.

The team wants to write one LLM judge per category next sprint. Turn these notes into the categories we should build evals for, with how often each happens.
