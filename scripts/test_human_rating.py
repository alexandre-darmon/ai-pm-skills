import contextlib
import io
import json
import re
import tempfile
import unittest
from pathlib import Path

from human_rating import (blind, cohen_kappa, decide, judge_id, judge_metrics, parse_guess, parse_sheet, pool,
                          recorded_answers, score, stratified_sample, wilson)
from human_rating import main as cli


def main(argv, root):
    with contextlib.redirect_stdout(io.StringIO()):
        return cli(argv, root=root)
from validate_skills import skill_hash

SKILL = """---
name: {name}
description: Use when testing.
license: CC-BY-4.0
metadata:
  legal: "{legal}"
---
Body of {name}.
"""
def make_repo(root: Path) -> None:
    """Four catalog skills (one legal), 8 scored cases + 1 negative each, a recorded run and an earlier stale one."""
    for name, legal in (("alpha", "false"), ("beta", "false"), ("gamma", "false"), ("lex", "true")):
        folder = root / "skills" / name
        (folder).mkdir(parents=True)
        (folder / "SKILL.md").write_text(SKILL.format(name=name, legal=legal))
        cases = {}
        for k in range(1, 10):
            case = f"{name}-00{k}"
            graders = folder / "evals" / case / "graders"
            graders.mkdir(parents=True)
            (folder / "evals" / case / "prompt.md").write_text(f"---\nname: {case}\n---\nRequest {case} for the PM.\n")
            (graders / "triggered.md").write_text("---\ntype: tool_used\ntool: Skill\ninput_match: 'x'\n" + ("max: 0\n" if k == 9 else "") + "---\n")
            cases[case] = {}
            for arm in ("with", "without"):
                cases[case][arm] = []
                for i in range(1, 4):
                    rel = f"{case}/{arm}-{i}.md"
                    for run_dir, text in (("night", f"Answer {case} {i}, see {name}. " + "word " * (k + i + (5 if arm == "with" else 0))),
                                          ("old", "stale answer")):
                        f = root / "eval-out" / run_dir / "answers" / name / rel
                        f.parent.mkdir(parents=True, exist_ok=True)
                        f.write_text(text)
                    cases[case][arm].append({"file": rel, "error": None, "graders": {}})
        h = skill_hash(folder)
        for run_dir, hsh in (("night", h), ("old", "0" * 64)):
            (root / "eval-out" / run_dir / "answers" / name / "runs.json").write_text(
                json.dumps({"startedAt": "2026-11-10T10:00:00Z", "skillHash": hsh, "cases": cases}))
        (root / "baselines").mkdir(exist_ok=True)
        record = {c: {"runsWithout": 3, "negative": c.endswith("009")} for c in cases}
        (root / "baselines" / f"{name}.json").write_text(json.dumps({"skill": name, "date": "2026-11-10", "skillHash": h,
                                                                     "model": "claude-sonnet-5-5", "cases": record}))


def write_judges(root: Path, key: dict, offsets: dict, costs: dict, skip_words: bool = False, only: dict | None = None) -> None:
    """Judge files where each judge scores human + offset (on 1-5), from the key: answers must match by id and words.

    only: {model: set of key ids} that this judge scored (default: all)."""
    for model, offset in offsets.items():
        by_skill = {}
        for item_id, it in key["items"].items():
            if only and item_id not in only[model]:
                continue
            human = HUMAN.get(item_id, 3)
            judged = min(5, max(1, human + offset))
            by_skill.setdefault(it["skill"], []).append({"id": it["judgeId"], "words": it["words"] + (1 if skip_words else 0),
                                                         "judge": (judged - 1) / 4})
        folder = root / "baselines" / "judge" / model
        folder.mkdir(parents=True, exist_ok=True)
        for skill, answers in by_skill.items():
            (folder / f"{skill}.json").write_text(json.dumps({"skill": skill, "passes": 1, "costUsd": costs[model] * len(answers), "answers": answers}))


HUMAN = {}


def fill(sheet: str, key: dict) -> str:
    """Fill the sheet: 'with' answers get 4 and pass, 'without' 2 and fail, one answer left blank."""
    def item(m):
        item_id = m.group(1)
        if item_id == "a03":
            return m.group(0)
        good = key["items"][item_id]["arm"] == "with"
        HUMAN[item_id] = 4 if good else 2
        return (f"<!-- rating-item: {item_id} -->\n## {item_id}\n\n- overall (1-5): {HUMAN[item_id]}\n"
                f"- pass (yes/no): {'yes' if good else 'no'}\n- critique: weakest point {item_id}\n")
    return re.sub(r"<!-- rating-item: (\w+) -->\n## \w+\n\n- overall \(1-5\): \n- pass \(yes/no\): \n- critique: \n", item, sheet)


class StatsTest(unittest.TestCase):
    def test_wilson(self):
        lo, hi = wilson(0, 20)
        self.assertEqual(lo, 0.0)
        self.assertAlmostEqual(hi, 0.161, places=3)  # zero failures in 20 still allows about 16%
        lo, hi = wilson(16, 20)
        self.assertAlmostEqual(lo, 0.584, places=3)
        self.assertAlmostEqual(hi, 0.919, places=3)
        self.assertIsNone(wilson(0, 0))

    def test_kappa(self):
        a = [True] * 10 + [False] * 10
        self.assertAlmostEqual(cohen_kappa(a, a), 1.0)
        self.assertAlmostEqual(cohen_kappa(a, [not x for x in a]), -1.0)
        b = [True] * 8 + [False] * 2 + [True] * 2 + [False] * 8  # 80% agreement, 50% by chance
        self.assertAlmostEqual(cohen_kappa(a, b), 0.6)
        self.assertIsNone(cohen_kappa([True] * 5, [True] * 5))

    def test_metrics_and_rule(self):
        rows = [{"human": 4, "humanPass": True, "judge": 4.5}] * 16 + [{"human": 2, "humanPass": False, "judge": 2.5}] * 4
        m = judge_metrics(rows, 4.0)
        self.assertEqual(m["within1"], 1.0)
        self.assertTrue(m["calibrated"])
        self.assertEqual((m["tpr"], m["tnr"]), (1.0, 1.0))
        self.assertAlmostEqual(m["meanAbsGap"], 0.5)
        off = judge_metrics(rows[:15] + [{"human": 2, "humanPass": False, "judge": 4.5}] * 5, 4.0)  # 75% within 1 point
        self.assertFalse(off["calibrated"])
        self.assertFalse(judge_metrics(rows[:19], 4.0)["calibrated"])  # 19 answers: too few
        base = {"answers": 20, "calibrated": True}
        self.assertEqual(decide({"h": {**base, "meanAbsGap": 0.5}, "s": {**base, "meanAbsGap": 0.2}}, {"h": 0.01, "s": 0.05})[0], "s")
        self.assertEqual(decide({"h": {**base, "meanAbsGap": 0.35}, "s": {**base, "meanAbsGap": 0.2}}, {"h": 0.01, "s": 0.05})[0], "h")
        none, reason = decide({"h": {**base, "calibrated": False, "meanAbsGap": 2}}, {})
        self.assertIsNone(none)
        self.assertIn("rubric", reason)
        self.assertIn("too small", decide({"h": {**base, "answers": 12, "meanAbsGap": 0.1}}, {})[1])


class SheetTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        make_repo(self.root)

    def tearDown(self):
        self.tmp.cleanup()

    def test_pool_reads_the_recorded_run_only(self):
        self.assertEqual(recorded_answers(self.root, "alpha"), self.root / "eval-out" / "night" / "answers" / "alpha")
        items = pool(self.root)
        self.assertEqual(len(items), 3 * 8 * 2 * 3)  # legal skill and negative cases left out
        self.assertNotIn("lex", {i["skill"] for i in items})
        self.assertFalse(any(i["case"].endswith("009") for i in items))
        self.assertEqual(len(pool(self.root, include_legal=True)), 4 * 8 * 2 * 3)
        self.assertEqual({i["runDir"] for i in items}, {f"eval-out/night/answers/{s}" for s in ("alpha", "beta", "gamma")})
        it = items[0]
        self.assertEqual(it["judgeId"], judge_id(it["skill"], it["case"], it["arm"], it["run"]))

    def test_sample_is_stratified_and_blind(self):
        picked = stratified_sample(pool(self.root), 12, seed=3)
        self.assertEqual(len(picked), 12)
        for skill in ("alpha", "beta", "gamma"):
            self.assertEqual(sum(p["skill"] == skill and p["arm"] == "with" for p in picked), 2)
            self.assertEqual(sum(p["skill"] == skill and p["arm"] == "without" for p in picked), 2)
        self.assertEqual(stratified_sample(pool(self.root), 12, seed=3), picked)
        sheet, key = self.root / "s" / "sheet.md", self.root / "k" / "key.json"
        self.assertEqual(main(["sample", "--n", "12", "--seed", "3", "--any-answer", "--sheet", str(sheet), "--key", str(key)], root=self.root), 0)
        text = sheet.read_text()
        self.assertEqual(text.count("<!-- rating-item:"), 12)
        for leak in ("alpha", "beta", "gamma", "with", "without"):
            self.assertNotIn(f"see {leak}", text)  # skill names replaced
        self.assertNotIn("without", text.split("Leave an answer")[1])  # no arm in the items
        self.assertIn("honest_about_unknowns", text)  # the judge's rubric
        self.assertNotIn("[ref]", text)  # a mask token would itself point at the "with" arm
        self.assertIn("- guessed ids: ", text)
        self.assertEqual(len(json.loads(key.read_text())["items"]), 12)

    def test_a_request_is_never_shown_twice(self):
        picked = stratified_sample(pool(self.root), 100, seed=5)
        pairs = [(p["skill"], p["case"]) for p in picked]
        self.assertEqual(len(pairs), len(set(pairs)))
        self.assertEqual(len(picked), 3 * 8)  # one answer per (skill, case), not 100

    def test_default_sample_draws_only_judged_answers(self):
        sheet, key_path = self.root / "sheet.md", self.root / "key.json"
        args = ["sample", "--n", "12", "--seed", "2", "--sheet", str(sheet), "--key", str(key_path)]
        self.assertEqual(main(args, root=self.root), 1)  # no judge file: refused
        everything = {"items": {f"x{k}": it for k, it in enumerate(pool(self.root))}}
        alpha_beta = {i for i, it in everything["items"].items() if it["skill"] != "gamma"}
        write_judges(self.root, everything, {"h": 0, "s": 0}, {"h": 0.01, "s": 0.05}, only={"h": alpha_beta, "s": set(everything["items"])})
        self.assertEqual(main(args, root=self.root), 0)
        self.assertNotIn("gamma", {it["skill"] for it in json.loads(key_path.read_text())["items"].values()})  # h never scored it
        self.assertEqual(main(["sample", "--n", "20", "--seed", "2", "--sheet", str(sheet), "--key", str(key_path)], root=self.root), 1)  # 16 pairs

    def test_without_answers_from_the_earlier_run(self):
        runs = self.root / "eval-out" / "night" / "answers" / "alpha" / "runs.json"
        saved = json.loads(runs.read_text())
        for arms in saved["cases"].values():
            del arms["without"]  # a with-arm run: run_evals reused the baseline's "without" score
        runs.write_text(json.dumps(saved))
        other = self.root / "eval-out" / "local" / "answers" / "alpha"  # same day, another model: not it
        other.mkdir(parents=True)
        (other / "runs.json").write_text(json.dumps({**json.loads((self.root / "eval-out/old/answers/alpha/runs.json").read_text()), "model": "qwen"}))
        items = [i for i in pool(self.root) if i["skill"] == "alpha"]
        self.assertEqual({i["runDir"] for i in items if i["arm"] == "with"}, {"eval-out/night/answers/alpha"})
        self.assertEqual({i["runDir"] for i in items if i["arm"] == "without"}, {"eval-out/old/answers/alpha"})

    def test_legal_answers_come_on_top(self):
        sheet, key_path = self.root / "sheet.md", self.root / "key.json"
        main(["sample", "--n", "12", "--seed", "4", "--any-answer", "--include-legal", "--legal-n", "4",
              "--sheet", str(sheet), "--key", str(key_path)], root=self.root)
        items = json.loads(key_path.read_text())["items"].values()
        self.assertEqual((sum(not i["legal"] for i in items), sum(i["legal"] for i in items)), (12, 4))

    def test_blind_drops_every_tell(self):
        text = ("Start here. Fill `templates/decision-record.md` now. See references/x.md for more. "
                "Use the beta method. Keep L3 for later.\nOwn alpha line.\nLast line.")
        out = blind(text, "alpha", ["alpha", "beta"])
        for tell in ("templates/", "references/", "beta", "alpha", "[ref]"):
            self.assertNotIn(tell, out)
        self.assertIn("Start here.", out)
        self.assertIn("Keep L3 for later.", out)
        self.assertIn("Last line.", out)

    def test_score_end_to_end(self):
        sheet, key_path, out = self.root / "sheet.md", self.root / "key.json", self.root / "human.json"
        main(["sample", "--n", "24", "--seed", "1", "--any-answer", "--sheet", str(sheet), "--key", str(key_path)], root=self.root)
        key = json.loads(key_path.read_text())
        filled = fill(sheet.read_text(), key)
        rows, problems = parse_sheet(filled)
        self.assertEqual((len(rows), problems), (23, []))
        write_judges(self.root, key, {"cheap": 0.5, "dear": 0.4, "loose": 2}, {"cheap": 0.01, "dear": 0.05, "loose": 0.01})
        result = score(self.root, key, [filled])
        self.assertEqual(result["rated"], 23)
        self.assertTrue(result["judges"]["cheap"]["calibrated"])
        self.assertFalse(result["judges"]["loose"]["calibrated"])
        self.assertEqual(result["decision"]["judge"], "cheap")  # gap 0.5 vs 0.4: under 0.2, the cheaper one
        self.assertAlmostEqual(result["humanGain"]["gain"], 0.5)  # 4 vs 2 on 1-5 is 0.75 vs 0.25
        self.assertEqual(result["judges"]["cheap"]["tpr"], 1.0)
        self.assertEqual(result["sharedWithJudges"], 23)
        self.assertIsNone(result["blinding"])  # last question left blank
        (self.root / "f.md").write_text(filled)
        self.assertEqual(main(["score", "--key", str(key_path), "--sheet", str(self.root / "f.md"), "--out", str(out)], root=self.root), 0)
        self.assertEqual(json.loads(out.read_text())["decision"]["judge"], "cheap")

    def test_judges_are_compared_on_the_same_answers(self):
        sheet, key_path = self.root / "sheet.md", self.root / "key.json"
        main(["sample", "--n", "24", "--seed", "1", "--any-answer", "--sheet", str(sheet), "--key", str(key_path)], root=self.root)
        key = json.loads(key_path.read_text())
        filled = fill(sheet.read_text(), key)
        ids = sorted(key["items"])
        # each judge alone covers 22 rated answers, but only 21 both: the rule counts those
        write_judges(self.root, key, {"cheap": 0.5, "dear": 0.4}, {"cheap": 0.01, "dear": 0.05},
                     only={"cheap": set(ids) - {ids[-1]}, "dear": set(ids) - {ids[0]}})
        result = score(self.root, key, [filled])
        self.assertEqual(result["sharedWithJudges"], 21)
        self.assertEqual({m["answers"] for m in result["judges"].values()}, {21})
        write_judges(self.root, key, {"cheap": 0.5, "dear": 0.4}, {"cheap": 0.01, "dear": 0.05},
                     only={"cheap": set(ids[:12]), "dear": set(ids[12:])})
        result = score(self.root, key, [filled])
        self.assertEqual(result["sharedWithJudges"], 0)
        self.assertIsNone(result["decision"]["judge"])

    def test_arm_guess_measures_the_blinding(self):
        sheet, key_path = self.root / "sheet.md", self.root / "key.json"
        main(["sample", "--n", "12", "--seed", "1", "--any-answer", "--sheet", str(sheet), "--key", str(key_path)], root=self.root)
        key = json.loads(key_path.read_text())
        guided = sorted(i for i, it in key["items"].items() if it["arm"] != "without")
        filled = fill(sheet.read_text(), key).replace("- guessed ids: ", "- guessed ids: " + ", ".join(guided))
        self.assertEqual(parse_guess(filled), set(guided))
        b = score(self.root, key, [filled])["blinding"]
        self.assertEqual((b["accuracy"], b["kappa"]), (1.0, 1.0))  # the person told every arm: the blinding failed
        self.assertEqual(parse_guess(filled.replace(", ".join(guided), "none")), set())

    def test_judge_scores_of_another_answer_are_not_joined(self):
        sheet, key_path = self.root / "sheet.md", self.root / "key.json"
        main(["sample", "--n", "24", "--seed", "1", "--any-answer", "--sheet", str(sheet), "--key", str(key_path)], root=self.root)
        key = json.loads(key_path.read_text())
        filled = fill(sheet.read_text(), key)
        write_judges(self.root, key, {"cheap": 0}, {"cheap": 0.01}, skip_words=True)
        result = score(self.root, key, [filled])
        self.assertEqual(result["judges"]["cheap"]["answers"], 0)
        self.assertIsNone(result["decision"]["judge"])
        self.assertIn("too small", result["decision"]["reason"])

    def test_bad_lines_are_reported(self):
        text = "<!-- rating-item: a01 -->\n- overall (1-5): 7\n- pass (yes/no): yes\n- critique: x\n" \
               "<!-- rating-item: a02 -->\n- overall (1-5): 3\n- pass (yes/no): maybe\n- critique: x\n" \
               "<!-- rating-item: a03 -->\n- overall (1-5): \n- pass (yes/no): \n- critique: \n"
        rows, problems = parse_sheet(text)
        self.assertEqual(rows, {})
        self.assertEqual(len(problems), 2)


if __name__ == "__main__":
    unittest.main()
