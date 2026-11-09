I haven't indexed anything yet. I can't build a source register without the actual list, and the working directory is empty. I also couldn't read the skill's `kb-plan.md` template, because access to that folder was denied. So this is the plan and the decisions I'd make, not the finished file.

**Decision on "index everything"**

I wouldn't index all 40. I'd index the 28 sources that have an owner and send the other 12 to the sponsor.

- **Staff answers:** An unowned 2019 procedure can contradict a current one, and the assistant will then quote it confidently to branch staff.
- **Re-certification:** Nobody can confirm those 12 are still correct. Without an owner, there is nobody to re-certify them or to retire them.
- **Cost of waiting:** This is cheap to reverse. Each of the 12 can go in as soon as someone names themselves as owner and confirms the content.
- **For the sponsor:** More content helps only if it is correct and has an owner. I'd frame it as phase 1 with 28 sources, then add the 12 as they get owners. The sponsor can also name an owner for the whole group, such as a branch-operations lead.

**Plan**

1. **Source register:** one row per source, with owner (a named person or team), refresh cadence, sensitivity, format and which users may see it. The 12 unowned sources go in as "excluded, escalated". Each needs an owner or a decision to drop it by a set date.
2. **Expiry as a number:**
   - Procedures: 12 months.
   - Product sheets: 3 to 6 months, or whatever matches how often they change.
   - FAQ pages: 6 months.
   - SharePoint sites: set per site, since they mix content types.
   - Past expiry, the owner re-certifies the source or it leaves the index.
3. **Inclusion and exclusion:** leave out drafts, duplicates, and personal data the use case doesn't need. Don't delete replaced versions of time-bound content such as rates, policies and terms. Keep them with effective-from and effective-to dates, so a question about an older period still gets the right answer. A replaced FAQ page is simply swapped out.
4. **Sensitivity and audience:** the two SharePoint sites are the main risk because they may hold restricted or personal data. Use separate collections with access control at retrieval. Don't put them in one open index.
5. **Chunking:** split along each document's structure. Every chunk carries owner, version, effective dates and expiry, so answers can cite a source and be checked for age.
6. **No-source behaviour:** if retrieval is empty, weak or conflicting, the assistant says it has no basis. It names what is missing and routes the person to the source owner. It doesn't answer from the closest document. Excluding the 12 sources makes this path more frequent, so wording for it is needed before launch.
7. **Retrieval tests:** write labelled queries (question plus the source that should be found) from real branch-staff questions. Hand them to `build-evals`, and run them before launch and after each source change.
8. **Monthly review and retirement:** each month, check expired sources, owner changes, and questions that found no good source. A dated version retires when no question can still reach its period, subject to legal retention.
9. **KPIs:** track the share of sampled answers citing an expired source or a version outside its period. Also track the share with a claim no cited source supports. Hand both to `assistant-kpis-cost-per-outcome`.

**What I need from you**

- The list of 40 sources, ideally with owner, last-updated date, and which of the 12 are the unowned ones.
- The sensitivity of the two SharePoint sites.
- A sample of real staff questions, for the retrieval tests.
- Confirmation that the sponsor accepts the phased approach, and who can assign owners to the 12.

Once I have the list, I'll fill in the register and write `kb-plan.md`.