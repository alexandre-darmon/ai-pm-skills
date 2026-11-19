The table shows where the problem is, not why it happens. I'd present it with a diagnosis and a proposed fix, so the audience has something to decide on.

**1. Size it with the arithmetic shown**
- VPN setup is 40,000 × 22% = 8,800 conversations, and 8,800 × 46% = 4,048 of them are unresolved.
- Every other use case is below 15% unresolved. That is at most 31,200 × 15% = 4,680 unresolved conversations across all the others combined.
- So VPN setup is at least 4,048 / (4,048 + 4,680) ≈ 46% of all unresolved conversations, from one use case. On its own it accounts for 4,048 / 40,000 ≈ 10% of total volume.
- If VPN setup matched the 15% ceiling of the others, unresolved VPN conversations would fall from 4,048 to 1,320. That is about 2,700 fewer conversations, or roughly 7% of total volume.
- Assumptions: the labels are correct, and "unresolved" means the same thing in every use case. Say both on the slide.

**2. Find out why before proposing a fix**
- The high rate may not be the assistant's fault. VPN setup often needs something the assistant can't do, such as admin rights, device enrollment, certificates or an access request.
- Pull a masked sample of unresolved VPN conversations (100–200), drawn across the whole quarter. Read them and cluster by failure reason. Likely clusters are a missing or outdated KB article, a step that needs a human, a device or OS variant the assistant doesn't handle, a wrong answer, and the user giving up.
- Split the 46% by resolution type (escalated, abandoned or unresolved). Also split it by week, since a spike could be an outage or a bad rollout, and by channel, OS and VPN client if you have those fields.
- Check whether "VPN setup" is too broad. It may mix first-time setup with troubleshooting an existing connection, and those can have very different resolution rates.

**3. Hand the sample to the eval work**
- Give the masked unresolved sample to `build-evals` as candidate golden-set cases. Give it a named owner and a date. Scoring stays there.
- This gives you a repeatable test, so you can show the fix worked and not just that the numbers moved.

**4. Choose the action by cluster**
- For KB gaps, rewrite or add the VPN articles, by OS and client.
- For steps that need a human, build a handoff with the right information collected up front, or add a self-service path.
- For wrong answers, fix the prompt or the retrieval and test against the golden set.
- Set a target, for example VPN unresolved at or below 25% next quarter, and track it with the monthly drift check on a fresh labelled sample.

**5. For next week's presentation**
- Show the table, the arithmetic above, and a first read of the failure clusters from a small sample. Even 50 conversations is enough for a first read.
- Close with the owner, the target and the date for the re-measurement. Don't present the 46% as the finding. The finding is the cause and the plan.

If you give me the masked sample or its location, I can draft the clustering and the golden-set handoff.