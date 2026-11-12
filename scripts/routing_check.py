#!/usr/bin/env python3
"""Free routing check: with every skill installed, does the right description stand out for each request?

Usage: python3 scripts/routing_check.py [--json PATH] [--cases routing/cases.yaml] [repo_root]

Reads routing/cases.yaml and the description of every skill in skills/ and drafts/ (with the name, the only text
the model sees when it decides which skill to load). Ranks the descriptions against each request by TF-IDF cosine
over stemmed words: stdlib only, deterministic. Reports top-1 and top-3 accuracy and the confusion pairs.
The name is left out of the score on purpose: it never changes (the validator ties it to the folder), so scoring it
would only hide a description edit (a skill whose description is wiped would still win on its name).

Known weakness: this is a lexical proxy. The model reads meaning, not shared words: it routes "which model
goes to production" to model-selection even if the request shares more words with release-to-production,
and it can decline every skill on an out-of-scope request that happens to share words with one. The paid
check (scripts/routing_eval.py) measures the real choice; this one only catches a description edit that
moves the words a collision zone depends on, in either direction (one skill loses them, another grows them).

CI rule (exit 1), a ratchet on routing/baseline.json (recorded with --update), per case:
- recorded at rank 1 with a margin over rank 2 of at least FLOOR: it must stay at rank 1; the failure names the
  skill that took it. This is the usual collision: a description that grows until it takes a neighbour's request.
- recorded in the top 3 with at least FLOOR over rank 4: it must stay in the top 3.
- cases under FLOOR are noise (an IDF shift from an unrelated edit can swap them): together they may lose at most
  TOP1_SLACK top-1 hits, and leave the top 3 freely (noted, not failed).
- a recorded case that disappears from cases.yaml fails until the record is updated.
--update refuses to record a worse state (lists every worse rank and every vanished case) unless
--accept-regressions is given, so the ratchet cannot be loosened by one quiet run.
Why a ratchet and not "top 3 for every case": the lexical proxy misses honest requests whose words differ from the
description ("chatbot told customers their policy covers flood" shares no word with an incident skill), so an
absolute rule would push us to write cases for the proxy instead of for users. Out-of-scope cases ("none") are
reported, never gated: requests outside the catalog share words with some description as often as in-scope ones do
(insurance "claims" matches a "vendor's claim"), so only the paid check can test that no skill fires.
After an edit that improves ranks, or new cases, run --update and commit routing/baseline.json.
"""
import argparse
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from validate_skills import read_frontmatter  # noqa: E402

ROOT = Path(__file__).parent.parent
CASES = ROOT / "routing" / "cases.yaml"
BASELINE = ROOT / "routing" / "baseline.json"
NONE = "none"
TOP_K = 3
FLOOR = 0.02  # cosine gap under which two skills' order is noise: the smallest gaps recorded are 0.001 to 0.003
TOP1_SLACK = 1  # among cases under FLOOR, two near-equal scores swapping places is noise; losing two is a trend
RULE = (f"a case recorded at rank 1 by at least {FLOOR} keeps rank 1, a case recorded in the top {TOP_K} by at least "
        f"{FLOOR} stays there, cases under {FLOOR} lose at most {TOP1_SLACK} top-1 hit, recorded cases may not vanish; "
        "'none' cases are not gated (lexical overlap cannot show that no skill fires)")

STOP = set("""a about above after again against all also am an and any are as at be because been before being below
between both but by can could did do does doing down during each few for from further had has have having he her here
hers him his how i if in into is it its itself just let me more most my no nor not now of off on once only or other our
ours out over own same she should so some such than that the their them then there these they this those through to too
under until up us very was we were what when where which while who whom why will with would you your yours
one two three four five six seven eight ten get got want wants need needs make way say says said use used using ask asks
asked tell told someone anyone nobody nothing anything something every really actually next week month today""".split())


def stem(word: str) -> str:
    """Light suffix stripping, enough to merge plurals and verb forms (evals/eval, labelling/label, routed/route).

    A final e is dropped on every word, so route, routed and routing all become rout (release/released,
    score/scored, code/coding, price/pricing): both sides of the cosine go through the same rule.
    """
    for suffix, repl in (("ies", "y"), ("sses", "ss"), ("ing", ""), ("ed", ""), ("es", "e"), ("s", "")):
        if word.endswith(suffix) and len(word) - len(suffix) >= 3 and not (suffix == "s" and word[-2] in "su") \
                and not (suffix == "ed" and word.endswith("eed")):  # speed, proceed: not a past tense
            word = word[: len(word) - len(suffix)] + repl
            if suffix in ("ing", "ed") and word[-1] == word[-2] and word[-1] not in "s":  # labelling -> labell -> label
                word = word[:-1]
            break
    if word.endswith("e") and not word.endswith("ee") and len(word) > 3 and word[:-1] not in STOP:  # note is not "not"
        word = word[:-1]
    return word


def tokens(text: str) -> list[str]:
    words = re.findall(r"[a-z][a-z0-9]+", text.lower().replace("'s", ""))
    return [stem(w) for w in words if w not in STOP and len(w) > 1]


def load_skills(root: Path) -> dict[str, str]:
    """name -> description for skills/ and drafts/ (drafts are installed in the paid check too); no name, see above."""
    skills = {}
    for folder in sorted(p for d in ("skills", "drafts") for p in (root / d).glob("*") if (p / "SKILL.md").is_file()):
        fm, _ = read_frontmatter(folder / "SKILL.md")
        skills[fm["name"]] = str(fm.get("description") or "")
    return skills


def load_cases(path: Path) -> list[dict]:
    return yaml.safe_load(path.read_text(encoding="utf-8"))["cases"]


class Index:
    """TF-IDF vectors of the skill descriptions; a request is scored by cosine against each."""

    def __init__(self, docs: dict[str, str]):
        toks = {name: tokens(text) for name, text in docs.items()}
        df = Counter(t for ts in toks.values() for t in set(ts))
        n = len(docs)
        self.idf = {t: math.log((1 + n) / (1 + c)) + 1 for t, c in df.items()}
        self.vectors = {name: self.vector(ts) for name, ts in toks.items()}

    def vector(self, toks: list[str]) -> dict[str, float]:
        tf = Counter(t for t in toks if t in self.idf)  # words no description has cannot tell skills apart
        vec = {t: (1 + math.log(c)) * self.idf[t] for t, c in tf.items()}
        norm = math.sqrt(sum(v * v for v in vec.values()))
        return {t: v / norm for t, v in vec.items()} if norm else {}

    def rank(self, text: str) -> list[tuple[str, float]]:
        q = self.vector(tokens(text))
        scores = [(name, sum(w * d.get(t, 0.0) for t, w in q.items())) for name, d in self.vectors.items()]
        return sorted(scores, key=lambda x: (-x[1], x[0]))


def score_cases(cases: list[dict], index: Index) -> list[dict]:
    rows = []
    for c in cases:
        ranking = index.rank(c["request"])
        names = [n for n, _ in ranking]
        expected = c["expected"]
        predicted = ranking[0][0] if ranking and ranking[0][1] > 0 else NONE  # lexical: "none" only when no word is shared
        rank = names.index(expected) + 1 if expected in names else None
        score = lambda i: ranking[i][1] if i < len(ranking) else 0.0  # noqa: E731
        rows.append({"id": c["id"], "zone": c.get("zone", ""), "expected": expected, "predicted": predicted, "rank": rank,
                     # rank 1: lead over rank 2; in the top 3: lead over rank 4 (what an edit must erase to fail the gate)
                     "margin": round(score(0) - score(1), 4) if rank == 1 else None,
                     "edge": round(score(rank - 1) - score(TOP_K), 4) if rank and rank <= TOP_K else None,
                     "top": [[n, round(s, 4)] for n, s in ranking[:TOP_K]]})
    return rows


def in_top(r: dict) -> bool:
    return r["expected"] != NONE and r["rank"] is not None and r["rank"] <= TOP_K


def failures(rows: list[dict], baseline: dict | None) -> list[str]:
    """The CI rule: a ratchet on the recorded winners and ranks (module docstring). No baseline: no failure."""
    if not baseline:
        return []
    out, rec, soft_lost = [], baseline.get("cases", {}), []
    by_id = {r["id"]: r for r in rows}
    for cid in sorted(set(rec) - set(by_id)):
        out.append(f"{cid}: recorded in routing/baseline.json but gone from cases.yaml "
                   "(run --update --accept-regressions if the removal is meant)")
    for r in rows:
        before = rec.get(r["id"])
        if not before or r["expected"] == NONE or before.get("rank") is None:
            continue
        top = ", ".join(n for n, _ in r["top"])
        if before["rank"] == 1 and r["rank"] != 1:
            if before["margin"] >= FLOOR:
                out.append(f"{r['id']}: {r['predicted']} took it from {r['expected']} (recorded at rank 1 by "
                           f"{before['margin']:.3f}, now rank {r['rank']}; top {TOP_K}: {top})")
                continue
            soft_lost.append(r["id"])
        if before["rank"] <= TOP_K and not in_top(r) and (before.get("edge") or 0) >= FLOOR:
            out.append(f"{r['id']}: {r['expected']} fell from rank {before['rank']} to {r['rank']} "
                       f"(recorded {before['edge']:.3f} above rank {TOP_K + 1}; top {TOP_K}: {top})")
    if len(soft_lost) > TOP1_SLACK:
        out.append(f"{len(soft_lost)} near-tie cases lost top-1 ({', '.join(soft_lost)}; slack {TOP1_SLACK})")
    return out


def notes(rows: list[dict], baseline: dict | None) -> list[str]:
    """Not failures: new cases, near-tie moves, improvements (lock them in with --update), cases too close to gate."""
    if not baseline:
        return []
    rec, out = baseline.get("cases", {}), []
    for r in rows:
        if r["expected"] == NONE:
            continue
        before = rec.get(r["id"])
        if before is None:
            out.append(f"{r['id']}: new case, not gated until --update")
            continue
        if before["rank"] is None or (r["rank"] is not None and r["rank"] < before["rank"]):
            out.append(f"{r['id']}: {r['expected']} improved from rank {before['rank']} to {r['rank']}")
        elif r["rank"] != before["rank"]:
            out.append(f"{r['id']}: {r['expected']} moved from rank {before['rank']} to {r['rank']} (under the {FLOOR} floor, not gated)"
                       if (before["rank"] == 1 and before["margin"] < FLOOR) or (before["rank"] <= TOP_K and (before.get("edge") or 0) < FLOOR)
                       else f"{r['id']}: {r['expected']} moved from rank {before['rank']} to {r['rank']} (outside the top {TOP_K}, not gated)")
    return out


def worse(rows: list[dict], baseline: dict | None) -> list[str]:
    """What --update would lose: every case whose rank got worse, every recorded case that vanished (gated or not)."""
    if not baseline:
        return []
    rec, by_id = baseline.get("cases", {}), {r["id"]: r for r in rows}
    out = [f"{cid}: gone from cases.yaml" for cid in sorted(set(rec) - set(by_id))]
    for r in rows:
        before = rec.get(r["id"])
        if before and (r["rank"] is None or r["rank"] > before["rank"]):
            out.append(f"{r['id']}: {r['expected']} rank {before['rank']} -> {r['rank']} (top-1 now {r['predicted']})")
    return out


def record(rows: list[dict]) -> dict:
    return {"rule": RULE, "floor": FLOOR,
            "top1Hits": sum(r["expected"] == r["predicted"] for r in rows if r["expected"] != NONE),
            "cases": {r["id"]: {"rank": r["rank"], "winner": r["predicted"], "margin": r["margin"], "edge": r["edge"]}
                      for r in rows if r["expected"] != NONE}}


def summary(rows: list[dict]) -> dict:
    n = len(rows)
    in_scope = [r for r in rows if r["expected"] != NONE]
    confusion = Counter((r["expected"], r["predicted"]) for r in rows if r["expected"] != r["predicted"])
    return {"cases": n,
            "top1": sum(r["expected"] == r["predicted"] for r in rows) / n if n else 0.0,
            "top3": sum(r["rank"] is not None and r["rank"] <= TOP_K for r in in_scope) / len(in_scope) if in_scope else 0.0,
            "confusion": [{"expected": e, "predicted": p, "count": k} for (e, p), k in sorted(confusion.items(), key=lambda x: (-x[1], x[0]))]}


def unknown_names(cases: list[dict], skills: set[str]) -> list[str]:
    return [f"{c.get('id')}: expected '{c.get('expected')}' is not a skill or draft" for c in cases
            if c.get("expected") != NONE and c.get("expected") not in skills]


def report(rows: list[dict], s: dict, fails: list[str], extra: list[str] = ()) -> str:
    lines = ["| Case | Zone | Expected | Lexical top 3 | Rank |", "| --- | --- | --- | --- | --- |"]
    for r in rows:
        mark = "" if r["expected"] == r["predicted"] else " ✗"
        top = ", ".join(f"{n} {sc:.2f}" for n, sc in r["top"])
        lines.append(f"| {r['id']} | {r['zone']} | {r['expected']}{mark} | {top} | {r['rank'] or '—'} |")
    lines.append(f"\nTop-1 {s['top1']:.0%} of {s['cases']} cases, top-3 {s['top3']:.0%} of in-scope cases (lexical proxy, not the model's choice).")
    if s["confusion"]:
        lines.append("\nConfusions (expected → lexical top-1):")
        lines += [f"- {c['expected']} → {c['predicted']} ({c['count']})" for c in s["confusion"]]
    lines.append("\n'none' cases: the lexical proxy always finds some shared word, so only the paid check "
                 "(scripts/routing_eval.py) tests them.")
    if extra:
        lines.append("\nNotes:")
        lines += [f"- {n}" for n in extra]
    lines.append(f"\nRule: {RULE}. " + ("FAIL" if fails else "pass"))
    lines += [f"- {f}" for f in fails]
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?", type=Path, default=ROOT)
    ap.add_argument("--cases", type=Path)
    ap.add_argument("--json", type=Path, help="also write rows and summary as JSON")
    ap.add_argument("--update", action="store_true", help="record the current ranks in routing/baseline.json")
    ap.add_argument("--accept-regressions", action="store_true",
                    help="with --update: record even if some rank got worse or a recorded case vanished")
    args = ap.parse_args(argv)
    skills = load_skills(args.root)
    cases = load_cases(args.cases or args.root / "routing" / "cases.yaml")
    bad = unknown_names(cases, set(skills))
    if bad:
        print("\n".join(bad))
        return 1
    rows = score_cases(cases, Index(skills))
    path = args.root / "routing" / "baseline.json"
    baseline = json.loads(path.read_text()) if path.is_file() else None
    if args.update:
        lost = worse(rows, baseline)
        if lost and not args.accept_regressions:
            print("not recorded: these get worse against routing/baseline.json (rerun with --accept-regressions "
                  "to record them on purpose):\n" + "\n".join(f"- {x}" for x in lost))
            return 1
        if lost:
            print("recording worse ranks on purpose:\n" + "\n".join(f"- {x}" for x in lost))
        path.write_text(json.dumps(record(rows), indent=2) + "\n")
        print(f"recorded {path.relative_to(args.root) if path.is_relative_to(args.root) else path}")
        baseline = json.loads(path.read_text())
    s, fails = summary(rows), failures(rows, baseline)
    if baseline is None:  # a deleted record must not switch the gate off silently
        fails.append("routing/baseline.json is missing: run python3 scripts/routing_check.py --update and commit it")
    print(report(rows, s, fails, notes(rows, baseline)), end="")
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps({"summary": s, "failures": fails, "rows": rows}, indent=2) + "\n")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
