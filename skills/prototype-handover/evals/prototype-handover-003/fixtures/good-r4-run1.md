I couldn't write the file because the Write tool is disabled in this session. The content is below. I can save it once Write is available, or you can paste it into `handover-file.md`. I also couldn't list the skill's folder, so I have only the template and the statistics note. I haven't read its other reference pages.

**Do not write "accuracy 95%, validated" in the inventory or the go-live pack.**
- **The interval is wide.** 38 of 40 is 95% only as a point estimate. The 95% Wilson interval is about 84% to 99%. This is a compliance control, so the lower bound is the relevant number.
- **It is a different model version.** The gateway serves a newer version than the one you tested on. A model change after a baseline invalidates that baseline for the new version, and the gateway version counts as a new release.
- **A prototype score is not release evidence.** It sets the floor that engineering's build must reach. Release evidence is the same suite run on the engineering build.
- **"Validated" is a model-risk status.** Only model risk can assign it.

**Wording the sponsor can use instead:**
"Prototype baseline: 38/40 correct (95%, 95% CI about 84–99%) on 40 officer-written questions, on <model/version>, <date>. Not validated on the production model version. Validation against the frozen suite on the engineering build is a go-live condition."

Engineering does not have to redo the testing. They run your existing 40 questions on the gateway model, and ideally extend the suite with more cases, rewording variants, and questions the library cannot answer.

**Handover file (draft)**

1. **Containment.** I don't know whether the prototype holds production personal data or production credentials, or what the kill date is. If it has either and the kill date is past or within two weeks, the file needs a stop or a dated decision by a named owner. Revoke any personal keys or access it used either way.
2. **Inventory.**
   - Known: the function (answers with citations from the policy library), the use case (compliance officers), and 38/40.
   - To confirm: how many users it has, the model and exact version, where the prompt lives, the grader, the owner, the kill date, where it runs, and the policy library snapshot date.
3. **Tier.** I propose tier 3. It informs AML and sanctions work at L1–L2, which is a regulatory control area. "Officers check it" does not lower the tier unless every answer is checked before use and a named person does the checking.
4. **Outcome.** Rebuild by engineering, as already planned. The prototype is a spec with evidence, not code to harden.
5. **Handover contract.**
   - **Baseline:** 38/40, 95%, CI about 84–99%, with model version, prompt version and date still to fill in.
   - **Bar and never-acceptable error:** The bar per class is not yet set. It must be signed before any run on the engineering build. I propose the never-acceptable error as a confidently wrong procedure, or a citation that doesn't exist or doesn't say what is claimed, in sanctions or AML escalation questions.
   - **Judge:** If an LLM graded the answers, it is "not validated: cannot gate" until its TPR and TNR are measured against expert labels.
   - **Change control:** Prompt, model id, parameters, retrieval settings and library snapshot go under change control.
   - **Trace fields:** to confirm.
6. **Intended vs implemented.** Check whether "answer only from the library" is a prompt sentence or enforced in code. Check whether citations are verified, whether it abstains on unanswerable questions, whether there is a login, and what the 2 failures were.
7. **Rebuild list.**
   - **Rebuild:** authentication and row-level access, a secrets vault, separate environments, the logging pipeline, guardrails in code (citation check, library-only answers, abstention), gateway access, and tests.
   - **Reuse as spec:** the prompt and the 40 questions (the seed suite).
8. **Register entry.** Draft fields: identifier, owner, EUC tier 3, model and provider, prompt version, autonomy L1–L2, data categories, baseline "38/40 on <date>, not validated on the gateway version", and review date.
9. **AI Act.** The bank may be the provider, since it built the system in-house for its own use. An Annex III use looks unlikely unless outputs feed decisions about individuals. This goes to the AI Act classification step and is not classified here.
10. **Questions.**
    - **IT risk:** Is the prototype an ICT asset to register now? Was its software authorised? Is any operational use accepted before January, and for how many weeks?
    - **Model risk:** Is it a model under the policy, and does the bank's model tiering place it above tier 3? Who validates it, and what bar applies per class, point estimate or lower bound?
    - **Counsel:** What is the provider role, and does Annex III apply?
    - **DPO:** Does the library or the question log contain personal data, and is a DPIA needed?

This file is a proposal and a list of questions. IT risk, model risk and counsel decide.

**To finish the file, I need these from you:**
- The kill date.
- The model version you tested on.
- Which credentials the prototype used.
- Whether any production or personal data was ever loaded.
- Who graded the 40 answers, and what the 2 failures were.
- The named business owner.