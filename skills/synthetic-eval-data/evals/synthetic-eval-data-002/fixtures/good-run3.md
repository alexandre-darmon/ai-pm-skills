Before the prompt, you should know that the plan as described can't support a go-live decision. Model X would write the questions, answer them, and grade them, so a 90% score mostly measures how much Model X agrees with itself.

## Problems with the plan

1. **Model X writes the gold answers.** If it misreads a procedure, the gold answer carries the same error, and the assistant repeats it and gets marked correct. Gold answers need to come from the procedures themselves, with a citation, and be approved by a claims expert.
2. **Same model generates, answers and judges.** Judges favour text like their own. Use a different model family for generation if you can, and check the judge against expert labels on a sample (about 100 cases).
3. **Generating questions in one shot gives tidy, easy questions.** Real policyholders write with typos, mix several requests together and leave out the policy number. Generate a table of scenarios first, have an expert review it, and only then write the questions.
4. **The set has no real questions.** Add any real ones you have (even 20 to 50, masked). Report the score on real and synthetic cases separately, and report the synthetic share.
5. **Missing case types.** You need questions the procedures can't answer (the expected behaviour is to say so or hand over to a human). You also need high-risk cases such as a claim refusal dispute, a legal threat, a vulnerable customer or suspected fraud. A 90% average can hide failures in exactly those.

## Generation prompts (two stages)

### Stage 1: scenario table (run per procedure, or per batch of related procedures)

```
You are helping build a test set for a home-insurance claims assistant.
You will receive ONE claims procedure (ID: {procedure_id}). Do not use outside knowledge.

Produce {N} test scenarios as a JSON list. Each scenario has these fields, one value each:
- procedure_id: the procedure it relates to (cite section/paragraph in source_ref)
- source_ref: the exact section(s) or sentence(s) the answer depends on
- intent: one of [declare_claim, required_documents, deadlines, claim_status,
  coverage_question, excess/deductible, expert_visit, payment/reimbursement,
  dispute_or_complaint, modify_or_cancel_claim, other]
- persona: one of [first-time claimant, elderly, stressed after a major loss (fire/flood),
  repeat claimant, third party/neighbour involved, tenant, owner-occupier]
- difficulty: one of [direct (one fact), multi-step, needs two procedures,
  ambiguous or missing information, exception or edge case]
- answerability: one of [answerable_from_procedure, not_covered_by_procedures,
  needs_human_agent]
- style: one of [clean, typos_and_abbreviations, long_and_rambling, very_short,
  emotional, mixes_two_requests, wrong_terminology]
- missing_info: what the customer fails to say, or "none"

Rules:
- Every value must appear several times across the list; do not repeat the same combination.
- At least 25% of scenarios must be answerability != answerable_from_procedure.
- At least 20% must be edge cases or exceptions that the procedure states explicitly.
- Skip combinations that make no sense and put them in a "dropped" list with the reason.
- Output scenarios only. Do NOT write the customer question or the answer yet.

PROCEDURE:
{procedure_text}
```

An expert reviews the scenario table before stage 2. They check coverage across the 40 procedures and the weighting toward risky classes. Weight those classes above their expected traffic share.

### Stage 2: question and draft gold answer (one call per scenario or small batch)

```
Write one customer message for the scenario below, and a DRAFT reference answer.

SCENARIO: {scenario_json}
PROCEDURE (the only source of truth): {procedure_text}
STYLE EXAMPLES (real customer messages; imitate register, not content): {5-10 real examples}

Customer message rules:
- Write as the policyholder would type it in the chat, following the scenario's style value
  exactly. Do not use the procedure's wording or internal terms unless a customer would.
- Do not paraphrase any style example's facts. Do not include real names, policy numbers or
  addresses; use plausible fakes only if the scenario needs them.
- Do not hint at the answer. Include the missing_info gap as specified.

Reference answer rules:
- Use only the PROCEDURE. Quote or cite the exact source_ref sentences.
- List "must_include" (facts, deadlines, documents, amounts that a correct answer needs)
  and "must_not" (statements that would be wrong or risky, e.g. promising coverage or a payout).
- If answerability is not_covered_by_procedures: the expected behaviour is to say it cannot
  confirm and direct the customer to a named human channel; state that, do not invent an answer.
- If needs_human_agent: the expected behaviour is a handover, plus what the assistant may
  safely say before it.
- If the procedure is ambiguous on this point, set "ambiguous_in_source": true instead of guessing.

Return JSON: {customer_message, must_include[], must_not[], expected_behaviour,
source_ref, ambiguous_in_source, confidence: low|medium|high}
```

## What to do around the prompts

- **Expert approval of the gold answers.** Claims experts review at least every case with `confidence` below high or `ambiguous_in_source` true. Take a random 10 to 20% of the rest, and track the rejection rate per procedure and per scenario value. Regenerate any value where more than 20% are rejected. Gold answers are only gold once approved.
- **Flag each case** with `origin` (real or synthetic), generator model and version, prompt version, scenario, date and reviewer.
- **Contamination.** Never put these questions into the assistant's prompt, few-shot examples or tuning data.
- **Judging.** Score against `must_include` and `must_not`, not free-text similarity. Calibrate the judge against expert labels on about 100 answers. Use a different model as judge if you can.
- **Reporting.** Report the score per intent, difficulty and answerability, not one global number. Set a higher bar for the high-risk classes (disputes, legal threats, vulnerable customers, coverage promises). With 1,000 cases, a small class of 30 questions can't confirm 90%, so size each class deliberately.
- **Comparing with real traffic.** Compare length, typo share and intent mix against real traffic. If the set is much tidier than real chats, regenerate it.
- **Replacing synthetic cases.** After launch, sample real masked conversations and replace synthetic cases class by class by a set date. Until then, report the results as indicative.

If you can tell me how many real customer questions you have, which classes are high-risk, and whether a second model family is available, I can turn this into a full set spec with tuple counts per class.