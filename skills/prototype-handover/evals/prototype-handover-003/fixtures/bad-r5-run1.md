I can't write the file in this session. The working directory is empty and I have no file-writing tool. The handover text is below, ready to paste into a file.

I wrote it without the wording "accuracy 95%, validated". The 38/40 result doesn't support that claim for the system engineering will build:

- **Different model.** The 40 questions were run on the prototype's model version. The gateway serves a newer one. Answer quality and citation behaviour can change between versions, so the result describes the prototype, not the rebuild.
- **Small sample.** 38/40 gives a 95% confidence interval of roughly 83–99%. "95%" overstates the precision.
- **Possible overlap.** The questions were written with two officers during development. If you tuned the prompt against them, the score is optimistic.
- **Citation checking is unclear.** It's not stated whether "correct" included checking that the citations were right.

Re-running 40 questions on the gateway model is cheap, so engineering doesn't need to redo much. The pack can say that the prototype result stands and that the re-run is a go-live condition.

---

# Handover: AML & Sanctions Procedures Q&A Assistant

**Owner:** Alex Darmon | **Date:** 2026-11-11 | **Target rebuild:** January 2027

## 1. Purpose
An internal assistant that answers compliance officers' questions on AML and sanctions procedures, using the policy library, with citations.

## 2. What is handed over
- System prompt (attach the final version, with a version/hash).
- The 40-question test set with reference answers and the expected source documents (attach).
- Policy library snapshot or version used in testing: *[fill in]*.
- Prototype model and version used: *[fill in]*.

## 3. Prototype test result (as observed)
| Item | Value |
|---|---|
| Questions | 40, written with two senior compliance officers |
| Correct | 38 (95%) |
| 95% confidence interval | about 83%–99% |
| Model | Prototype model *[version]*, not the gateway model |
| Citation accuracy checked separately? | *[yes/no]* |
| The 2 failures | *[describe each, and whether they were wrong, incomplete or mis-cited]* |
| Prompt tuned on these questions? | *[yes/no]* |

## 4. Status for the model risk inventory
**Proposed wording:** "Prototype achieved 38/40 correct on a 40-question expert-written set (prototype model). Not yet validated on the production model. Validation on the bank gateway model is a go-live condition."

The result must not be recorded as "accuracy 95%, validated" for the production system. It was measured on a different model version, on a small set, and may not be independent of prompt development.

## 5. Go-live conditions (for engineering)
1. Run the 40-question set unchanged through the gateway model with the handed-over prompt. Compare against the prototype result question by question.
2. Check citations: each cited document and section exists and supports the answer.
3. Add a fresh set of at least 40 questions, not used in prompt tuning, ideally with some covering edge cases, out-of-scope questions and "policy does not say" cases. Written or reviewed by officers who did not tune the prompt.
4. Agree the acceptance threshold with the model risk owner and compliance *before* running, including a zero-tolerance rule for confidently wrong sanctions answers.
5. Record the gateway model version. Re-run the set whenever the gateway model changes.
6. Decide the in-use controls: user guidance to verify against the cited policy, logging, and a feedback route for wrong answers.

## 6. Known limitations
*[Add: the failure cases, the document types not covered, and the policy library date.]*

## 7. Sign-off
Prototype owner: ____ Compliance sponsor: ____ Model risk: ____ Engineering: ____

---

Three things would sharpen it:
- Tell me what the two failures were. They are the most useful part of the handover.
- Tell me whether the prompt was tuned on those 40 questions.
- If the sponsor pushes back, the re-run is about an afternoon's work. Presenting it as a go-live condition is likely to be easier for them to accept than a delay.

If you give me a writable directory or enable file tools, I'll save this as a file.