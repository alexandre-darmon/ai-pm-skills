I haven't indexed anything yet. The working directory is empty, so I don't have the 40-source list. Even with it, I wouldn't index all 40.

**Blockers**

1. **The 12 sources with no owner stay out of the index.** A source nobody maintains can't be re-certified, and a 2019 document can contradict current procedure without anyone noticing. Branch staff would get confident wrong answers with nothing to trace them to.
   - Each of the 12 either gets a named owner, or the sponsor escalates it.
   - Until one of those happens, it is excluded.
   - The cost of excluding them is that questions those sources would have answered now get "no basis, ask X". I can only size that once I see which topics they cover.
2. **Mixed sensitivity is unchecked.** The two SharePoint sites and the procedures may include restricted content, such as HR, pricing or customer data. Restricted and open material can't share an index unless access is enforced at retrieval, based on each user's own permissions. I need a sensitivity and audience label for every source.
3. **Expiry and refresh are unknown for all 40 sources.** Each source needs a number of days or months, set from how often it really changes. Past that date, the owner re-certifies it or it leaves the index.

**To the sponsor:** "More content means better answers" doesn't hold here. Unowned and outdated content makes answers worse, and the assistant can't tell which parts are stale. A smaller owned index with an explicit "I don't know, ask the source owner" path is safer. Owners can be found afterwards, and each source can be added once it has one. That's quicker than cleaning up a bad answer given to a branch.

**What I need from you**
- The 40-source list, with whatever exists for each: owner, last-modified date, format, sensitivity and who may access it.
- Where the content lives (SharePoint export, wiki, files), so I can sample real documents without cleaning them first.
- Which questions branch staff actually ask, from tickets or the helpdesk. These become the labelled test queries.
- Whether retrieved chunks and logs may leave your tenant, meaning the vendor and retention rules. Staff questions may contain customer personal data.
- Expected daily volume. If there's none, I'll list it as an open item, not invent a figure.

**What I'll produce once I have those**
- A `data-requirements.md` with a source register and the excluded sources listed with what is lost.
- Separate indexes by audience.
- Metadata on every chunk: owner, version, effective dates and expiry.
- Dated versions for procedures and rates that change, so the answer to "what applied then?" survives.
- A no-source fallback behaviour.
- Labelled queries for retrieval testing, and a monthly review of owners and expiry.

If you paste the list, I'll start with the register.