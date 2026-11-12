"""Refresh the README catalog between <!-- catalog:start --> and <!-- catalog:end -->.

A skill is listed as available if its folder is in skills/, as a draft if it is in drafts/. The one-line
summaries below are written for readers; the SKILL.md description is written for triggering.
    python3 scripts/readme_catalog.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BLOCKS = {"specify": "Specify", "build": "Build", "evaluate": "Evaluate", "prove": "Prove"}
SUMMARY = {
    "ai-opportunity-assessment": "AI or not, in which form, and the dated ask with its stop conditions.",
    "llm-feature-prd": "PRD for an LLM feature: autonomy level per step, failure paths, eval stub, guardrails, stop conditions.",
    "process-ai-redesign": "Level per step for a whole process, gates, scenarios with ROI lines, migration path.",
    "ai-data-requirements": "Fields and documents a feature reads and writes: owners, expiry, flows, lawful basis.",
    "agent-design-and-tooling": "An agent's loop, tools, permission matrix, stop conditions and traces.",
    "ai-feasibility-spike": "A throwaway prototype on the real model: one question, appetite and bar set first, n of N with intervals, cost per correct answer.",
    "system-prompt-and-guardrails": "System prompt plus input, output and action guardrails, with a red-team set.",
    "trace-review-tool": "A thin review app a coding agent builds over masked traces: pass/fail with critique, reviewer and time on every label.",
    "prototype-handover": "What a PM-built AI tool becomes in a bank: rebuilt, registered at its EUC tier or retired; suite and baseline as the contract.",
    "ai-interaction-patterns": "What users see: sources, confidence only when calibrated, correction, refusal, escalation.",
    "build-evals": "Eval set, graders, per-class thresholds signed before the run, intervals, baseline; per-component checks.",
    "error-analysis": "Read real traces, find and price failure modes before choosing any metric or judge.",
    "llm-judge-calibration": "Validate an LLM judge with TPR and TNR on held-out labels; correct the rate it reports.",
    "synthetic-eval-data": "Synthetic inputs from dimensions grounded in real traffic, with the share declared; counterfactual variants.",
    "agent-evals": "End state, forbidden events, pass^k with bounds, prompt injection measured as utility under attack.",
    "retrieval-evaluation": "RAG evaluated in two stages: retrieval at the k sent, then generation on fixed contexts.",
    "model-selection": "Choose a model on your own suite: cost per success, noise test, decision record.",
    "ai-vendor-evaluation": "Buy on your own bake-off: cost per correct outcome, benchmark audit, clauses that keep quality testable.",
    "red-team-evals": "Plan and read an attack campaign on an assistant or RAG: classes, sizing, rates with intervals, residual-risk record. Never \"robust\".",
    "multi-turn-evals": "Evaluate whole conversations: scripted and simulated cases, a validated simulator, conversation-level graders, pass^k.",
    "release-to-production": "Ship a change: offline gate, shadow, canary, A/B only if the sample allows.",
    "production-evals-monitoring": "Quality after release: sampled judges, control limits, owners, and the AI Act art. 72 plan.",
    "conversation-analysis": "What people really ask the assistant, and how it goes, with personal data masked first.",
    "assistant-kpis-cost-per-outcome": "KPIs for an assistant or agent: quality by domain, adoption, cost per correct outcome.",
    "ai-roi-quantification": "ROI of a live AI product: volume × quality × unit value − costs, baseline, sensitivity.",
    "ai-act-classification": "EU AI Act role, risk category, obligations and the eval evidence each article asks for. Never a verdict.",
    "model-card-ai-registry": "The eval record of each version: results per class with intervals, judge, signed thresholds, limits.",
    "ai-incident-playbook": "Contain, roll back, report on time, and turn every incident into regression cases before the fix ships.",
    "ai-adoption-plan": "Adoption proven on correct outcomes, over-trust measured, training by role, AI Act art. 4 evidence.",
}


def stage(folder):
    m = re.search(r'^\s+stage: "?(\w+)', (folder / "SKILL.md").read_text(), re.M)
    return m.group(1) if m else "specify"


# Reads under root: keep check_generated.INPUTS in step with any new folder read here.
def main(root=ROOT):
    order = list(SUMMARY)
    found = {p.name: p for d in ("skills", "drafts") for p in (root / d).glob("*") if (p / "SKILL.md").is_file()}
    missing = sorted(set(found) - set(SUMMARY))
    if missing:
        sys.exit(f"add a summary for {missing}")
    rank = {b: i for i, b in enumerate(BLOCKS)}
    order = sorted((n for n in order if n in found), key=lambda n: rank.get(stage(found[n]), 0))  # by block, then as listed
    tested = [n for n in order if found[n].parent.name == "skills"]
    drafts = [n for n in order if found[n].parent.name == "drafts"]
    rows = [f"| [`{n}`](skills/{n}/SKILL.md) | {BLOCKS[stage(found[n])]} | {SUMMARY[n]} |" for n in tested]
    out = [f"{len(found)} skills in {['zero', 'one', 'two', 'three', 'four', 'five'][len(BLOCKS)]} blocks, hard cap 30. Each one owns its triggers: no two skills compete for the same request, "
           "and the validator flags descriptions that overlap. **Available** skills are in `skills/`: their last recorded run "
           "(three runs per case, on today's text and cases) passes, the validator checks it on every push, and they install from the marketplace. **Drafts** are written and pass the free checks, not yet the paid runs.",
           "", f"### Available ({len(tested)})", "", "| Skill | Block | What it does |", "| --- | --- | --- |", *rows]
    if drafts:
        out += ["", f"### Drafts ({len(drafts)})", "", "| Skill | Block | What it does |", "| --- | --- | --- |",
                *[f"| `{n}` | {BLOCKS[stage(found[n])]} | {SUMMARY[n]} |" for n in drafts]]
    readme = root / "README.md"
    text = readme.read_text()
    head, rest = text.split("<!-- catalog:start -->", 1)
    readme.write_text(f"{head}<!-- catalog:start -->\n" + "\n".join(out) + f"\n<!-- catalog:end -->{rest.split('<!-- catalog:end -->', 1)[1]}")
    return len(tested), len(drafts)


if __name__ == "__main__":
    print(main())
