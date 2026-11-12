#!/usr/bin/env python3
"""Blind human labels on saved eval answers, to calibrate the LLM judge (docs/evaluation.md, "Choosing the judge").

Usage:
  python3 scripts/human_rating.py sample [--n 20] [--seed S] [--skills a,b] [--any-answer] [--include-legal] [--legal-n 6]
                                         [--sheet PATH] [--key PATH]
  python3 scripts/human_rating.py score --key PATH --sheet PATH [--sheet PATH2] [--date YYYY-MM-DD] [--judge-pass 4.0]

sample: draws answers of the recorded run of each catalog skill. "with" answers come from the
eval-out/*/answers/<skill>/runs.json whose skillHash is the one in baselines/<skill>.json; "without" answers from
that run if it has them, else from the latest earlier run of the same model holding every "without" run the
baseline counts (run_evals.py reuses the baseline's "without" score when only the skill changed). Stratified over
skills and arms (with, without, template where saved), never the same (skill, case) twice, so no request comes
back under another arm. By default only answers that every judge in baselines/judge/ scored (same id, same word
count) are drawn, and it refuses when they cannot fill --n: run judge_answers.py on the sampled skills first.
--any-answer drops that filter; the judges then score the sheet with judge_answers.py --key before score can pick one. Writes a blinded Markdown sheet, with the judge's rubric
and the request's goal (the judge sees both), and a separate key mapping each id to skill, case, arm and run. The
person grading gets the sheet only, never the key. --include-legal adds --legal-n legal answers on top of the
--n others: they never count for the judge, only for human pass rates.

score: reads the filled sheet and the key, joins the judge scores in baselines/judge/<model>/ (same answer:
same id and same word count), and applies the rule committed on 2026-11-07 on the answers that the person and
every judge scored: a judge is calibrated if its mean on the five criteria lands within 1 point of the human
score on at least 80% of at least 20 answers; if both pass, the smaller mean absolute gap wins, and under 0.2
points the cheaper one. Also reports TPR and TNR against the human pass/fail (Wilson intervals), Cohen's kappa,
the human gain with the skill (bootstrap interval), and how often the person guessed the arm.
Writes baselines/human/<date>.json. No model call, no cost.
"""
import argparse
import datetime
import hashlib
import json
import math
import random
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from eval_stats import bootstrap_ci  # noqa: E402
from judge_answers import (CRITERIA, PROMPT, blind, case_texts, git, judge_id, load_judges, recorded_answers,  # noqa: E402,F401
                           repo_names, sha256, template_answers, without_answers)
from run_evals import ROOT, case_graders, mean, skill_check  # noqa: E402
from validate_skills import read_skill  # noqa: E402

# The committed rule (docs/evaluation.md, 2026-11-07). Changing these after a human score is a new rule.
MIN_ANSWERS = 20
AGREE_WITHIN = 1.0
AGREE_SHARE = 0.80
TIE_GAP = 0.2
# Not part of the committed rule: where a judge's 1-5 mean counts as a pass, for TPR, TNR and kappa only.
JUDGE_PASS = 4.0
ARMS = ("with", "without", "template")
PASS_WORDS = {"yes": True, "y": True, "pass": True, "1": True, "no": False, "n": False, "fail": False, "0": False}
ITEM = "<!-- rating-item: {id} -->"
GUESS = "<!-- arm-guess -->"
LEGAL_N = 6


def collect(root: Path, folder: Path, answers: Path, legal: bool, label: str | None = None,
            arms_kept: tuple = ("with", "without")) -> list[dict]:
    """Every saved, error-free answer of the scored (non-negative) cases, for the arms kept."""
    skill, items = folder.name, []
    saved = json.loads((answers / "runs.json").read_text())
    for case, arms in saved["cases"].items():
        if not (folder / "evals" / case / "prompt.md").is_file():
            continue
        if any(skill_check(g) == "silent" for g in case_graders(folder, case)):
            continue  # negative case: the skill must stay silent, there is no answer to grade
        for arm, runs in arms.items():
            if arm not in arms_kept or (label and arm != "with"):
                continue
            for i, run in enumerate(runs, start=1):
                path = answers / run["file"]
                if run.get("error") or not path.is_file():
                    continue
                text = path.read_text(encoding="utf-8")
                if not text.strip():
                    continue
                name = label or arm
                items.append({"skill": skill, "case": case, "arm": name, "run": i, "legal": legal,
                              "runDir": str(answers.relative_to(root)), "file": run["file"], "judgeId": judge_id(skill, case, name, i),
                              "words": len(text.split()), "sha256": hashlib.sha256(text.encode()).hexdigest()})
    return items


def pool(root: Path, include_legal: bool = False, only: set[str] | None = None) -> list[dict]:
    items = []
    for folder in sorted(p for p in (root / "skills").iterdir() if (p / "SKILL.md").is_file()):
        if only and folder.name not in only:
            continue
        legal = bool(read_skill(folder / "SKILL.md")[0].get("legal"))
        if legal and not include_legal:
            continue
        answers = recorded_answers(root, folder.name)
        if answers:
            without = without_answers(root, folder.name, answers)
            items += collect(root, folder, answers, legal, arms_kept=("with", "without") if without == answers else ("with",))
            if without and without != answers:
                items += collect(root, folder, without, legal, arms_kept=("without",))
        variant, template = root / "eval-out" / "template-arm" / "variants" / folder.name, template_answers(root, folder.name)
        if template and variant.is_dir():
            items += collect(root, variant, template, legal, "template")
    return items


def stratified_sample(items: list[dict], n: int, seed: int) -> list[dict]:
    """Rounds over the skills in random order; each round takes one answer per arm the skill has, on a case not used yet.

    A (skill, case) pair is used once: the person never sees one request under two arms, so may return fewer than n.
    With 20 answers and two arms this covers 10 skills with both arms, so the human gain is paired within each skill
    (on different cases of that skill).
    """
    rng = random.Random(seed)
    strata = {}
    for it in items:
        strata.setdefault(it["skill"], {}).setdefault(it["arm"], []).append(it)
    for arms in strata.values():
        for group in arms.values():
            rng.shuffle(group)
    skills = sorted(strata)
    rng.shuffle(skills)
    skills.sort(key=lambda s: -len(strata[s]))  # skills with both arms first: the human gain needs pairs
    picked, used = [], set()
    while len(picked) < n:
        before = len(picked)
        for skill in skills:
            for arm in ARMS:
                fresh = [it for it in strata[skill].get(arm, []) if (skill, it["case"]) not in used]
                if not fresh or len(picked) >= n:
                    continue
                used.add((skill, fresh[0]["case"]))
                picked.append(fresh[0])
        if len(picked) == before:
            break
    rng.shuffle(picked)  # the sheet order says nothing about skill or arm
    return picked


def quote(text: str) -> str:
    return "\n".join("> " + line if line.strip() else ">" for line in text.strip().splitlines())


def rubric() -> str:
    lines = dict(re.findall(r"^- (\w+): (.+)$", PROMPT, re.M))
    return "\n".join(f"- {c}: {lines[c]}" for c in CRITERIA)


def write_sheet(root: Path, picked: list[dict], sheet: Path, key: Path, seed: int, date: str) -> None:
    names = repo_names(root)
    head = [f"# Blind rating sheet, {date}", "",
            "A product manager in a regulated company asked an AI assistant each request below. Grade each answer as a",
            "demanding senior AI product lead would. Length, formatting and vocabulary earn nothing. The rubric is the judge's:", "",
            rubric(), "",
            "Each request comes with the goal the judge is given too: grade on the five criteria, the goal is context.", "",
            "For each answer fill three lines, without opening any other file:", "",
            "- overall (1-5): your overall grade on those five criteria, 1 poor, 3 mixed, 5 excellent",
            "- pass (yes/no): yes if the PM could act on this answer as it stands, no otherwise",
            "- critique: the answer's weakest point, in one line", "",
            "Leave an answer blank rather than guess: blank lines are left out, not counted as fails.", ""]
    body, entries = [], {}
    for k, it in enumerate(picked, start=1):
        item_id = f"a{k:02d}"
        request, goal_text = case_texts((root / "skills" / it["skill"] / "evals" / it["case"] / "prompt.md").read_text(encoding="utf-8"))
        text = (root / it["runDir"] / it["file"]).read_text(encoding="utf-8")
        goal = ["### Goal", "", quote(goal_text), ""] if goal_text else []
        body += ["---", "", ITEM.format(id=item_id), f"## {item_id}", "",
                 "- overall (1-5): ", "- pass (yes/no): ", "- critique: ", "",
                 "### Request", "", quote(request), "", *goal, "### Answer", "", quote(blind(text, it["skill"], names)), ""]
        entries[item_id] = {**it, "requestSha256": sha256(request), "goalSha256": sha256(goal_text)}  # judge_answers.py --key checks them
    body += ["---", "", GUESS, "## Last question", "",
             "Answer it once every answer above is graded, and do not change a grade after it. For some requests the",
             "assistant was given extra guidance before answering. Which answers do you think had it? List their ids",
             "(for example a03, a11), or write none.", "", "- guessed ids: ", ""]
    sheet.parent.mkdir(parents=True, exist_ok=True)
    key.parent.mkdir(parents=True, exist_ok=True)
    sheet.write_text("\n".join(head + body) + "\n", encoding="utf-8")
    head_commit = (git(root, "rev-parse", "HEAD") or "").strip() or None  # where judge_answers.py --key looks if a prompt changes after
    key.write_text(json.dumps({"created": date, "seed": seed, "sheet": sheet.name, "promptsCommit": head_commit, "items": entries}, indent=2) + "\n")


def parse_guess(text: str) -> set[str] | None:
    """The ids the person thinks had extra guidance; None when the last question is blank."""
    found = re.search(r"^- guessed ids:[ \t]*(.*)$", text.split(GUESS, 1)[1] if GUESS in text else "", re.M)
    value = found[1].strip() if found else ""
    if not value:
        return None
    return set() if value.lower() in ("none", "-", "no") else set(re.findall(r"\ba\d+\b", value))


def parse_sheet(text: str) -> tuple[dict, list[str]]:
    """{id: {overall, pass, critique}} for the filled items, and the problems found. Blank items are skipped."""
    rows, problems = {}, []
    text = text.split(GUESS, 1)[0]
    chunks = re.split(r"^<!-- rating-item: (\w+) -->$", text, flags=re.M)
    for item_id, chunk in zip(chunks[1::2], chunks[2::2]):
        field = lambda name: (re.search(rf"^- {re.escape(name)}:[ \t]*(.*)$", chunk, re.M) or [None, ""])[1].strip()  # noqa: E731
        overall, verdict, critique = field("overall (1-5)"), field("pass (yes/no)").lower(), field("critique")
        if not overall and not verdict:
            continue
        try:
            score = float(overall)
        except ValueError:
            problems.append(f"{item_id}: overall '{overall}' is not a number from 1 to 5")
            continue
        if not 1 <= score <= 5:
            problems.append(f"{item_id}: overall {score} is outside 1 to 5")
            continue
        if verdict not in PASS_WORDS:
            problems.append(f"{item_id}: pass '{verdict}' must be yes or no")
            continue
        rows[item_id] = {"overall": score, "pass": PASS_WORDS[verdict], "critique": critique}
    return rows, problems


def wilson(k: int, n: int, z: float = 1.96) -> list[float] | None:
    """Wilson interval for k successes in n (references/eval-statistics.md)."""
    if not n:
        return None
    p = k / n
    centre, half = (p + z * z / (2 * n)) / (1 + z * z / n), z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return [max(0.0, centre - half), min(1.0, centre + half)]


def cohen_kappa(a: list[bool], b: list[bool]) -> float | None:
    """Agreement corrected for chance, between two labellers on the same items. None when chance agreement is 1."""
    n = len(a)
    if not n:
        return None
    observed = sum(x == y for x, y in zip(a, b)) / n
    pa, pb = sum(a) / n, sum(b) / n
    chance = pa * pb + (1 - pa) * (1 - pb)
    return None if chance == 1 else (observed - chance) / (1 - chance)


def judge_score(judge: dict, it: dict) -> float | None:
    """The judge's 1-5 mean on this answer, if it read this one: same id and same length, not an older answer saved
    under the same name."""
    entry = judge["skills"].get(it["skill"], {}).get(it["judgeId"])
    if entry and entry.get("judge") is not None and entry.get("words") == it["words"]:
        return 1 + 4 * entry["judge"]
    return None


def judged_by_all(judges: dict, it: dict) -> bool:
    return bool(judges) and all(judge_score(j, it) is not None for j in judges.values())


def judge_metrics(rows: list[dict], judge_pass: float) -> dict:
    """rows: {human (1-5), humanPass, judge (1-5)} on the shared answers: rated, not legal, scored by every judge."""
    n = len(rows)
    within = sum(abs(r["judge"] - r["human"]) <= AGREE_WITHIN for r in rows)
    pos, neg = [r for r in rows if r["humanPass"]], [r for r in rows if not r["humanPass"]]
    tp, tn = sum(r["judge"] >= judge_pass for r in pos), sum(r["judge"] < judge_pass for r in neg)
    return {"answers": n, "within1": within / n if n else None, "within1Interval": wilson(within, n),
            "meanAbsGap": mean([abs(r["judge"] - r["human"]) for r in rows]),
            "meanGap": mean([r["judge"] - r["human"] for r in rows]),  # above 0: the judge is more lenient than the person
            "tpr": tp / len(pos) if pos else None, "tprInterval": wilson(tp, len(pos)), "humanPasses": len(pos),
            "tnr": tn / len(neg) if neg else None, "tnrInterval": wilson(tn, len(neg)), "humanFails": len(neg),
            "kappa": cohen_kappa([r["humanPass"] for r in rows], [r["judge"] >= judge_pass for r in rows]),
            "calibrated": n >= MIN_ANSWERS and within / n >= AGREE_SHARE}


def decide(metrics: dict, costs: dict) -> tuple[str | None, str]:
    """Apply the committed rule. Returns (the judge kept or None, the reason in one sentence)."""
    if not metrics:
        return None, "no judge scores found in baselines/judge/"
    if not any(v["answers"] for v in metrics.values()):
        return None, ("sample too small to pick: no judge scored these answers (same id and word count); "
                      "run scripts/judge_answers.py --key <key.json> with every judge, then score again")
    shared = min(v["answers"] for v in metrics.values())
    if shared < MIN_ANSWERS:
        return None, (f"sample too small to pick: {shared} human-scored answers that every judge also scored, "
                      f"the rule needs {MIN_ANSWERS}")
    passed = sorted((v["meanAbsGap"], m) for m, v in metrics.items() if v["calibrated"])
    if not passed:
        return None, "no judge is calibrated: the judge stays out of any reported score and the rubric is revised before a new test"
    best = passed[0][0]
    close = [m for gap, m in passed if gap - best < TIE_GAP]
    if len(close) == 1:
        return close[0], f"{close[0]} is calibrated and closest to the human score (mean gap {best:.2f})"
    cheapest = min(close, key=lambda m: (costs.get(m) is None, costs.get(m) or 0, m))
    return cheapest, f"{', '.join(close)} are calibrated within {TIE_GAP} points of each other: {cheapest} is the cheaper"


def human_gain(rated: list[dict], arm: str, base: str) -> dict:
    """Mean over skills of (arm − base) human score on 0-1, paired within skill; 95% bootstrap interval over skills."""
    diffs = []
    for skill in sorted({r["skill"] for r in rated}):
        a = [r["score"] for r in rated if r["skill"] == skill and r["arm"] == arm]
        b = [r["score"] for r in rated if r["skill"] == skill and r["arm"] == base]
        if a and b:
            diffs.append(mean(a) - mean(b))
    out = {"skills": len(diffs), "gain": mean(diffs), "interval": None}
    if len(diffs) >= 2:
        out["interval"] = list(bootstrap_ci([diffs]))
    return out


def score(root: Path, key: dict, sheets: list[str], judge_pass: float = JUDGE_PASS) -> dict:
    labels, problems = parse_sheet(sheets[0])
    second = parse_sheet(sheets[1])[0] if len(sheets) > 1 else None
    unknown = sorted(set(labels) - set(key["items"]))
    if unknown:
        problems.append(f"ids not in the key: {', '.join(unknown)}")
    judges = load_judges(root)
    rated = []
    for item_id, h in sorted(labels.items()):
        it = key["items"].get(item_id)
        if not it:
            continue
        row = {"id": item_id, **{k: it[k] for k in ("skill", "case", "arm", "run", "legal", "runDir")},
               "human": h["overall"], "score": (h["overall"] - 1) / 4, "humanPass": h["pass"], "critique": h["critique"], "judges": {}}
        for model, j in judges.items():
            value = judge_score(j, it)
            if value is not None:
                row["judges"][model] = value
        rated.append(row)
    # one list for every judge: gaps and the tie rule compare judges on the same answers
    shared = [r for r in rated if not r["legal"] and judges and all(m in r["judges"] for m in judges)]
    metrics = {model: judge_metrics([{"human": r["human"], "humanPass": r["humanPass"], "judge": r["judges"][model]} for r in shared], judge_pass)
               for model in judges}
    picked, reason = decide(metrics, {m: j["costPerAnswer"] for m, j in judges.items()})
    arms = {}
    for arm in ARMS:
        rows = [r for r in rated if r["arm"] == arm]
        if rows:
            k = sum(r["humanPass"] for r in rows)
            arms[arm] = {"answers": len(rows), "score": mean([r["score"] for r in rows]), "passRate": k / len(rows), "passInterval": wilson(k, len(rows))}
    out = {"date": None, "sheetItems": len(key["items"]), "rated": len(rated), "unrated": len(key["items"]) - len(rated),
           "legalRated": sum(r["legal"] for r in rated), "sharedWithJudges": len(shared),
           "sharedArms": {a: sum(r["arm"] == a for r in shared) for a in ARMS if any(r["arm"] == a for r in shared)},
           "problems": problems,
           "rule": {"minAnswers": MIN_ANSWERS, "agreeWithin": AGREE_WITHIN, "agreeShare": AGREE_SHARE, "tieGap": TIE_GAP,
                    "judgePassForTprTnr": judge_pass, "committed": "docs/evaluation.md, 2026-11-07"},
           "judges": metrics, "decision": {"judge": picked, "reason": reason}, "arms": arms,
           "humanGain": human_gain(rated, "with", "without"), "methodGain": human_gain(rated, "with", "template"),
           "blinding": blinding(rated, parse_guess(sheets[0])), "answers": rated}
    if second is not None:
        shared = sorted(set(labels) & set(second))
        out["humanAgreement"] = {"answers": len(shared), "kappa": cohen_kappa([labels[i]["pass"] for i in shared], [second[i]["pass"] for i in shared]),
                                 "within1": mean([float(abs(labels[i]["overall"] - second[i]["overall"]) <= AGREE_WITHIN) for i in shared])}
    return out


def blinding(rated: list[dict], guessed: set[str] | None) -> dict | None:
    """How often the person told the arm: kappa near 0 means the blinding held. Truth: any arm other than "without"."""
    if guessed is None or not rated:
        return None
    truth, guess = [r["arm"] != "without" for r in rated], [r["id"] in guessed for r in rated]
    right = sum(t == g for t, g in zip(truth, guess))
    return {"answers": len(rated), "guessedGuided": sum(guess), "actualGuided": sum(truth), "accuracy": right / len(rated),
            "accuracyInterval": wilson(right, len(rated)), "kappa": cohen_kappa(truth, guess)}


def fmt(x, digits=2) -> str:
    return "n/a" if x is None else f"{x:.{digits}f}"


def interval(iv) -> str:
    return "n/a" if not iv else f"[{iv[0]:.2f}, {iv[1]:.2f}]"


def main(argv: list[str] | None = None, root: Path = ROOT) -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("sample")
    s.add_argument("--n", type=int, default=MIN_ANSWERS)
    s.add_argument("--seed", type=int, help="default: drawn at random and written to the key")
    s.add_argument("--include-legal", action="store_true", help="add --legal-n legal answers on top of --n, for human pass rates only")
    s.add_argument("--legal-n", type=int, default=LEGAL_N)
    s.add_argument("--any-answer", action="store_true", help="also draw answers no judge scored; run judge_answers.py --key on the key before score")
    s.add_argument("--skills", help="comma-separated catalog skills to draw from (default: all)")
    s.add_argument("--date", default=str(datetime.date.today()))
    s.add_argument("--sheet", type=Path)
    s.add_argument("--key", type=Path)
    c = sub.add_parser("score")
    c.add_argument("--key", type=Path, required=True)
    c.add_argument("--sheet", type=Path, action="append", required=True, help="the filled sheet; a second one adds a human-human kappa")
    c.add_argument("--date", default=str(datetime.date.today()))
    c.add_argument("--judge-pass", type=float, default=JUDGE_PASS, help="judge 1-5 mean counted as a pass, for TPR, TNR and kappa only")
    c.add_argument("--out", type=Path)
    args = ap.parse_args(argv)

    if args.cmd == "sample":
        seed = args.seed if args.seed is not None else random.SystemRandom().randrange(10**6)
        only = {x.strip() for x in args.skills.split(",")} if args.skills else None
        items = pool(root, args.include_legal, only)
        if not items:
            print("no saved answers of a recorded run found under eval-out/: nothing to sample")
            return 1
        for skill in sorted({i["skill"] for i in items}):
            dirs = {a: {i["runDir"] for i in items if i["skill"] == skill and i["arm"] == a} for a in ("with", "without")}
            if not dirs["without"]:
                print(f"note: {skill} has no saved 'without' answers of its recorded scores")
            elif dirs["without"] != dirs["with"]:
                print(f"note: {skill} 'without' answers from the earlier run {', '.join(sorted(dirs['without']))}")
        scored, legal = [i for i in items if not i["legal"]], [i for i in items if i["legal"]]
        if not args.any_answer:
            judges = load_judges(root)
            kept = [i for i in scored if judged_by_all(judges, i)]
            print(f"{len(kept)} of {len(scored)} non-legal answers scored by every judge ({', '.join(judges) or 'none found'})")
            scored = kept
        picked = stratified_sample(scored, args.n, seed)
        if len(picked) < args.n:
            print(f"only {len(picked)} answers can be drawn (one per skill and case), {args.n} asked")
            if not args.any_answer:
                print("refused: run scripts/judge_answers.py --recorded with every judge on the recorded answers of the skills to "
                      "sample, or lower --n (under 20 it cannot pick a judge), or --any-answer, then judge_answers.py --key on the key")
                return 1
        if args.include_legal:
            picked += stratified_sample(legal, args.legal_n, seed)
            random.Random(seed).shuffle(picked)
        base = root / "eval-out" / "human" / args.date
        sheet, key = args.sheet or base / "sheet.md", args.key or base / "key.json"
        write_sheet(root, picked, sheet, key, seed, args.date)
        per_arm = {a: sum(p["arm"] == a for p in picked) for a in ARMS if any(p["arm"] == a for p in picked)}
        print(f"{len(picked)} answers from {len({p['skill'] for p in picked})} skills {per_arm}, "
              f"{sum(p['legal'] for p in picked)} legal, seed {seed}")
        print(f"sheet (give this one): {sheet}\nkey (keep it away from the grader): {key}")
        return 0

    key = json.loads(args.key.read_text())
    result = score(root, key, [p.read_text(encoding="utf-8") for p in args.sheet], args.judge_pass)
    result["date"] = args.date
    for p in result["problems"]:
        print("problem:", p)
    out = args.out or root / "baselines" / "human" / f"{args.date}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(f"{result['rated']} rated, {result['unrated']} blank, {result['legalRated']} legal (not used for the judge), "
          f"{result['sharedWithJudges']} scored by every judge {result['sharedArms']}")
    for model, m in result["judges"].items():
        print(f"{model}: n {m['answers']}, within 1 point {fmt(m['within1'])} {interval(m['within1Interval'])}, mean gap {fmt(m['meanAbsGap'])} "
              f"(signed {fmt(m['meanGap'])}), TPR {fmt(m['tpr'])} {interval(m['tprInterval'])}, TNR {fmt(m['tnr'])} {interval(m['tnrInterval'])}, "
              f"kappa {fmt(m['kappa'])}, calibrated {m['calibrated']}")
    for name in ("humanGain", "methodGain"):
        g = result[name]
        if g["skills"]:
            print(f"{name}: {fmt(g['gain'])} {interval(g['interval'])} over {g['skills']} skills")
    if result["blinding"]:
        b = result["blinding"]
        print(f"arm guess: {b['guessedGuided']} guessed guided, {b['actualGuided']} were, accuracy {fmt(b['accuracy'])} "
              f"{interval(b['accuracyInterval'])}, kappa {fmt(b['kappa'])} (near 0: the blinding held)")
    else:
        print("arm guess: last question left blank, blinding not measured")
    if "humanAgreement" in result:
        h = result["humanAgreement"]
        print(f"two raters: {h['answers']} shared, kappa {fmt(h['kappa'])}, within 1 point {fmt(h['within1'])}")
    print("decision:", result["decision"]["judge"] or "none", "-", result["decision"]["reason"])
    print("written:", out)
    return 1 if result["problems"] else 0


if __name__ == "__main__":
    sys.exit(main())
