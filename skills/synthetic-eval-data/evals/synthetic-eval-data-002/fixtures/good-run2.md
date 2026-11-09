Before the prompt, there are three changes to your plan, because the plan as written can't support a go-live decision.

1. **Model X must not be the only author of the gold answers.** If it writes the gold and also answers the questions, a procedure it misreads gets the same wrong answer on both sides. The 90% then measures agreement with itself, not correctness. Experts must approve the gold. The prompt below only produces drafts with verbatim quotes, so review is fast. Review every case in risky classes and a stated random share of the rest.
2. **Model X should not write the questions and also judge the answers.** Judges favour text like their own. Use a different model family for generation if you can. At minimum, check the judge against expert labels on about 100 cases.
3. **Generate in two steps: tuples first, then questions.** One-shot generation gives 1,000 tidy, easy, near-duplicate questions. A 90% score on those says little about real policyholders. Include "cannot be answered from the procedures" cases, and flag every case as synthetic. Report scores per class, not just a global figure.

Here are the prompts.

## Step 1: scenario tuples (experts review this table before step 2)

```
You are helping build a test set for a home-insurance claims assistant.
You are given 40 claims procedures (below). Do NOT write questions yet.

Produce 1,000 scenario tuples as JSONL. Each tuple has these fields:
- procedure_ids: the procedure(s) needed to answer (1–2 ids), or [] if the
  question is deliberately NOT covered by any procedure
- intent: declare_claim | document_list | deadline | status_follow_up |
  coverage_question | reimbursement_amount_or_delay | complaint | other
- persona: first-time claimant | experienced policyholder | tenant |
  landlord | elderly or non-technical | stressed after major loss
- peril: water damage | fire | theft | storm | glass | other
- difficulty: single-fact | multi-step | two requests in one |
  missing information the customer should be asked for |
  exception or edge condition in the procedure
- answerability: answerable | partially answerable | not in procedures |
  needs human agent (dispute, legal threat, fraud suspicion, distress)
- style: clean | typos and no punctuation | very short | long and rambling |
  wrong terminology | pasted fragment of a message or email

Rules:
- Every procedure appears in at least 15 tuples.
- Allocation: about 65% answerable, 15% partially answerable, 10% not in
  procedures, 10% needs human agent. Give risky intents (complaint, deadline,
  coverage exclusions, anything with legal or financial consequence) more
  tuples than their natural frequency.
- Every value of every field appears many times; no two tuples identical.
- Drop impossible combinations and list the rules you applied.
- Do not invent facts about real people. No names, addresses, or policy
  numbers.
Output only the JSONL, then the list of dropped-combination rules.

PROCEDURES:
<<<paste the 40 procedures with their ids>>>
```

(Run in batches of about 100 tuples so the allocation stays under control.)

## Step 2: write the customer question from one tuple (separate call per tuple or small batch)

```
Write ONE message a policyholder would send to a home-insurance claims chat,
for the scenario below. Write it the way real customers write, following the
"style" field. Do not mention procedure ids or internal vocabulary. Use the
customer's words, not the procedure's wording. Do not make the message
more polite, complete, or well organised than the style requires. If
"missing information" is the difficulty, leave that information out. Invent no
real names; use no identifiers.

Style examples from real traffic (imitate register and length only; never copy
their content):
<<<paste 10–20 real customer messages, anonymised>>>

SCENARIO: <<<one tuple>>>

Output only the customer message.
```

## Step 3: draft gold answer for expert review (Model X may do this, but it is a draft)

```
You are preparing the reference answer for a test set. You are given the
customer message, its scenario, and the relevant procedures.

Output JSON:
- "key_points": the facts the correct answer MUST contain (amounts, deadlines,
  documents, steps), each with "quote": the verbatim sentence from the
  procedure that supports it and "procedure_id".
- "must_not": statements that would be wrong or dangerous (e.g. promising
  coverage, inventing a deadline, giving a legal opinion).
- "expected_behaviour": answer | ask_clarifying_question |
  say_not_covered_and_redirect | hand_over_to_human.
- "gold_answer": a short answer using only the key points.
- "confidence": high | medium | low, plus "ambiguities": any place where the
  procedure is unclear, contradictory, or silent.

Rules: use ONLY the procedures provided. If the procedures do not answer the
question, expected_behaviour is say_not_covered_and_redirect and
key_points is empty; never fill the gap from general insurance knowledge.
Every key point needs a verbatim quote, or it is removed.
```

## What to record and do next

- Each case carries: `origin: synthetic`, generator model and version, tuple, prompt version, date, reviewer, and the expert verdict (approved / edited / rejected).
- Experts read the questions as well as the golds. Reject anything a real customer wouldn't write. If one tuple value is rejected more than about 20% of the time, regenerate it.
- Compare the set with real traffic (length, typos, class mix) before using it.
- Judge on `key_points`, `must_not`, and `expected_behaviour`, not on similarity to the gold text. This makes the judge easier to validate.
- Never reuse these cases as few-shot examples or prompt content for the assistant.
- At go-live, report the 90% per intent and per answerability class, with the synthetic share. Set a separate, stricter bar for "needs human agent" and "not in procedures", where a confident wrong answer is the worst failure. Add real conversations as they arrive and retire synthetic cases class by class.

If you tell me the 40 procedures' format and give me a dozen real customer messages, I can tune the allocation and the style anchors.