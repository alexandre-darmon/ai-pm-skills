# Handover register map

What each text says about a PM-built AI tool, in our own words. Last verified: 2026-11-11, against the texts below. An article number not listed here is not stated in a handover file; the point is phrased without it.

## EUC tiers (`aws-euc-tiers`)

| Tier | Scope | Controls the source asks for |
| --- | --- | --- |
| 1 Personal | One user, every output reviewed by that user, no effect beyond their own work | Existing access controls |
| 2 Team | Several users, no regulated outcome, failures recoverable | Named owner, inventory entry, human checkpoints, change control on prompts |
| 3 Business-critical | Touches customer outcomes, regulatory returns or financial controls | Rebuilt as a governed system, or a platform that enforces audit lineage, human review, output sampling and drift detection |
| 4 Mission-critical | Executes against ledgers, payments, trading or capital | No employee-built component in the execution path, independent validation, a named senior manager, full audit lineage |

The repo adds the autonomy axis (references/autonomy-ladder.md) and takes the higher of the two. Levels are the ladder's: a tool that drafts and a person who validates every output is L2, which tier 1 already assumes for a single user.

| Wanted level | On a personal task | On a team task | On a customer, pricing, regulatory or financial output |
| --- | --- | --- | --- |
| L0–L2 | 1 | 2 | 3 |
| L3 and above | 3 | 3 | 4 |

## DORA, for financial entities

- **Regulation (EU) 2022/2554, art. 3(7)**: defines an ICT asset as a software or hardware asset in the financial entity's network and information systems.
- **ESMA Q&A 2103** (11 February 2024, "EUC, EULA and Shadow IT"): end-user computing tools fall under that broad definition, so the DORA provisions on managing, securing and assessing the risk of ICT assets apply to them. It cites RTS art. 11(2)(c) and 16(9). Art. 4(2) and 16(5)–(6) below are this repo's additions, read from the RTS itself.
- **Delegated Regulation (EU) 2024/1774 (RTS on the ICT risk management framework)**:
  - art. 4(2)(b): the asset management policy keeps, per ICT asset, a unique identifier, its physical or logical location, its classification, its owner, the business functions it supports, whether it is exposed to external networks and its links and dependencies.
  - art. 11(2)(c): only authorised software is installed on ICT systems and endpoint devices.
  - art. 16(5)(a): non-production environments store only anonymised, pseudonymised or randomised production data.
  - art. 16(6): by derogation, production data may be stored there only for specific testing occasions, for limited periods, after approval by the relevant function and with those occasions reported to the ICT risk management function. It is a testing derogation: it does not cover running a business process on production data, and the skill never presents an operational exception as covered by it. Whether IT risk accepts operational use at all is a question for IT risk.
  - art. 16(9): those rules also apply, on a risk basis, to ICT systems developed or managed by users outside the ICT function.
- Outside financial entities, DORA does not apply: use the company's own end-user computing or shadow IT policy, and ask IT risk which one.

## Register entry: draft fields

| Field | Why |
| --- | --- |
| Identifier, name | RTS art. 4(2)(b) |
| Location (where it runs, where its data sits) | RTS art. 4(2)(b) |
| Owner (a named person, not a team) | RTS art. 4(2)(b); tier 2 control |
| Classification (proposed tier, data categories) | RTS art. 4(2)(b) |
| Business functions supported, dependencies (model provider, APIs, data sources) | RTS art. 4(2)(b) |
| Model, version, provider; prompt version | AI-specific: the behaviour changes with them |
| Autonomy level per step, wanted level | references/autonomy-ladder.md |
| Eval suite id and frozen baseline date | the handover contract |
| Kill or review date | references/build-to-learn.md |

## AI Act (Regulation (EU) 2024/1689)

- art. 3(3): a provider develops an AI system, or has it developed, and places it on the market or puts it into service under its own name or trademark.
- art. 3(11): putting into service includes supplying the system for its own use in the Union. A bank that builds an AI tool and uses it itself can therefore be its provider, not only a deployer.
- art. 25(1): a deployer or other party becomes provider of a high-risk system if it puts its name on it, substantially modifies it, or changes the purpose of a system not classified high-risk so that it becomes high-risk.
- The classification itself (Annex III point, exceptions, dates) belongs to `ai-act-classification`. This skill only raises the flag with the facts.

## GDPR

Personal data in a prototype, or special category data such as health, is a question for the DPO on a data protection impact assessment (art. 35). Not decided here.
