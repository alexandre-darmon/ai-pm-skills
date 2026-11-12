import contextlib
import io
import json
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

import human_rating
from judge_answers import KEY_DIR, PROMPT, blind, collect, estimate_cost, judge_id, key_items, load_judges, overall, parse_scores, redact, repo_names
from judge_answers import main as judge_main
from test_human_rating import fill, make_repo

GOOD = '{"sound": 5, "actionable": 3, "honest_about_unknowns": 3, "risk_aware": 3, "specific": 1, "meets_goal": 2, "weakest_point": "x"}'
ARM_WORDS = re.compile(r"\b(with|without|template)\b", re.I)


class FakeJudge:
    """Stands in for call_judge: records every prompt, answers 4 on every criterion, costs 0.01."""

    def __init__(self):
        self.prompts = []

    def __call__(self, prompt, model):
        self.prompts.append(prompt)
        return {**{c: 4 for c in ("sound", "actionable", "honest_about_unknowns", "risk_aware", "specific", "meets_goal")},
                "weakest_point": "w", "costUsd": 0.01}


def answer_of(prompt: str) -> str:
    return prompt.split("<answer>\n", 1)[1].rsplit("\n</answer>", 1)[0]


def request_of(prompt: str) -> str:
    return prompt.split("<request>\n", 1)[1].split("\n</request>", 1)[0]


def goal_of(prompt: str) -> str:
    return prompt.split("it achieves this goal: ", 1)[1].split("\n\n<request>", 1)[0]


def sheet_blocks(sheet: str) -> dict:
    """{sheet id: {"request", "goal" (None when the sheet shows none), "answer"}}: the quoted blocks as the person reads them."""
    out = {}
    for item_id, chunk in re.findall(r"<!-- rating-item: (\w+) -->(.*?)(?=\n---\n)", sheet, re.S):
        head, answer = chunk.split("### Answer\n\n", 1)
        request = head.split("### Request\n\n", 1)[1]
        request, goal = request.split("### Goal\n\n", 1) if "### Goal\n\n" in request else (request, None)
        out[item_id] = {"request": request.strip(), "goal": goal.strip() if goal is not None else None, "answer": answer.strip()}
    return out


def git(root: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(root), "-c", "user.email=t@example.com", "-c", "user.name=t", *args], check=True, capture_output=True)


class JudgeTest(unittest.TestCase):
    def test_redact_hides_the_arm(self):
        text = "I used the skill's template. Keep L2.\nSee `references/roi-model.md` and llm-feature-prd."
        out = redact(text, "llm-feature-prd")
        self.assertNotIn("skill", out)
        self.assertNotIn("references/", out)
        self.assertNotIn("llm-feature-prd", out)
        self.assertIn("Keep L2", out)

    def test_scores(self):
        scores = parse_scores("Here: " + GOOD)
        self.assertAlmostEqual(overall(scores), 0.5)  # generic criteria only, meets_goal stays apart
        with self.assertRaises(ValueError):
            parse_scores(GOOD.replace('"sound": 5', '"sound": 9'))
        with self.assertRaises(ValueError):
            parse_scores("no json")


class KeyModeTest(unittest.TestCase):
    """--key on a synthetic repo and key (human_rating.py sample), with a fake model client."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        make_repo(self.root)
        self.sheet, self.key_path = self.root / "h" / "sheet.md", self.root / "h" / "key.json"
        with contextlib.redirect_stdout(io.StringIO()):
            human_rating.main(["sample", "--n", "24", "--seed", "1", "--any-answer", "--sheet", str(self.sheet), "--key", str(self.key_path)],
                              root=self.root)
        self.key = json.loads(self.key_path.read_text())

    def tearDown(self):
        self.tmp.cleanup()

    def judge(self, *extra, model="fake-judge"):
        fake, out = FakeJudge(), io.StringIO()
        with contextlib.redirect_stdout(out):
            code = judge_main(["--key", str(self.key_path), "--model", model, "-j", "1", *extra], root=self.root, call=fake)
        return code, fake, out.getvalue()

    def test_ids_and_word_counts_match_the_key(self):
        code, fake, _ = self.judge()
        self.assertEqual(code, 0)
        self.assertEqual(len(fake.prompts), 2 * 24)  # two passes per answer
        written = json.loads((self.root / "baselines/judge/fake-judge" / KEY_DIR / f"{self.key['created']}-{self.key['seed']}.json").read_text())
        got = {(a["skill"], a["id"], a["words"]) for a in written["answers"]}
        self.assertEqual(got, {(it["skill"], it["judgeId"], it["words"]) for it in self.key["items"].values()})
        self.assertTrue(all(a["judge"] == 0.75 for a in written["answers"]))
        self.assertAlmostEqual(written["costUsd"], 0.48)
        judges = load_judges(self.root)
        for it in self.key["items"].values():
            self.assertEqual(human_rating.judge_score(judges["fake-judge"], it), 4.0)

    def test_score_joins_both_judges(self):
        self.judge(model="claude-haiku-5-5")
        self.judge(model="claude-sonnet-5-5")
        result = human_rating.score(self.root, self.key, [fill(self.sheet.read_text(), self.key)])
        self.assertEqual(result["sharedWithJudges"], 23)  # every rated answer, scored by both judges
        self.assertEqual({m: v["answers"] for m, v in result["judges"].items()}, {"claude-haiku-5-5": 23, "claude-sonnet-5-5": 23})

    def test_judge_reads_the_sheets_text(self):
        """Request, goal and blinded answer: what the judge reads is what the person read, block for block."""
        _, fake, _ = self.judge("--passes", "1")
        shown = sheet_blocks(self.sheet.read_text())
        self.assertTrue(any(b["goal"] for b in shown.values()) and any(b["goal"] is None for b in shown.values()))
        by_sheet_order = sorted(self.key["items"])  # the judge goes through the key in sheet order with one pass
        self.assertEqual(len(fake.prompts), len(by_sheet_order))
        names = repo_names(self.root)
        for item_id, prompt in zip(by_sheet_order, fake.prompts):
            it = self.key["items"][item_id]
            text = (self.root / it["runDir"] / it["file"]).read_text()
            self.assertEqual(answer_of(prompt), blind(text, it["skill"], names))
            self.assertEqual(human_rating.quote(answer_of(prompt)), shown[item_id]["answer"])
            self.assertEqual(human_rating.quote(request_of(prompt)), shown[item_id]["request"])
            self.assertEqual(human_rating.quote(goal_of(prompt)) if goal_of(prompt) else None, shown[item_id]["goal"])

    def test_nothing_about_the_arm_reaches_the_judge(self):
        items, _ = key_items(self.root, self.key)
        self.assertTrue(all("arm" not in i and "runDir" not in i and "file" not in i for i in items))
        _, fake, printed = self.judge()
        template_words = set(ARM_WORDS.findall(PROMPT.lower()))
        for prompt, it in zip(fake.prompts, [self.key["items"][k] for k in sorted(self.key["items"])]):
            self.assertNotIn(it["runDir"], prompt)
            self.assertNotIn(it["file"], prompt)
            self.assertNotIn(it["judgeId"], prompt)
            self.assertLessEqual(set(w.lower() for w in ARM_WORDS.findall(prompt)), template_words)
        self.assertIsNone(ARM_WORDS.search(printed))
        # the same answer under the other arm gives the very same prompt
        flipped = json.loads(json.dumps(self.key))
        for it in flipped["items"].values():
            it["arm"] = "without" if it["arm"] == "with" else "with"
            it["judgeId"] = judge_id(it["skill"], it["case"], it["arm"], it["run"])
        flipped_items, _ = key_items(self.root, flipped)
        self.assertEqual([PROMPT.format(goal=i["goal"], request=i["request"], answer=i["answer"]) for i in flipped_items], fake.prompts[:len(items)])
        written = (self.root / "baselines/judge/fake-judge" / KEY_DIR).glob("*.json")
        self.assertTrue(all('"arm"' not in f.read_text() for f in written))

    def test_dry_run_calls_nothing(self):
        code, fake, printed = self.judge("--dry-run")
        self.assertEqual((code, fake.prompts), (0, []))
        self.assertIn("48 calls to fake-judge", printed)
        self.assertIn("estimated cost unknown", printed)  # no past call of this model to estimate from
        self.assertEqual(len(re.findall(r"^  a\d+: prompt [\d,]+ chars", printed, re.M)), 24)
        self.assertIsNone(ARM_WORDS.search(printed))
        self.assertFalse((self.root / "baselines/judge/fake-judge").exists())

    def test_cost_estimate_comes_from_past_calls(self):
        self.judge()  # 48 calls at 0.01
        items, _ = key_items(self.root, self.key)
        usd, basis = estimate_cost(self.root, "fake-judge", items[:10], 3)
        self.assertIn("48 past calls", basis)
        self.assertIn("rough", basis)
        self.assertAlmostEqual(usd, 0.01 * 10 * 3)  # per call, whatever the answers' length

    def test_a_changed_answer_is_not_judged(self):
        item_id, it = sorted(self.key["items"].items())[0]
        (self.root / it["runDir"] / it["file"]).write_text("rewritten since the key")
        items, skipped = key_items(self.root, self.key)
        self.assertEqual((len(items), skipped), (23, [f"{item_id}: answer file missing or changed since the key was written"]))

    def test_the_key_stores_what_the_sheet_showed(self):
        for it in self.key["items"].values():
            self.assertEqual(len(it["requestSha256"]), 64)
            self.assertEqual(len(it["goalSha256"]), 64)

    def changed_prompt(self) -> tuple[str, dict, Path, str]:
        item_id, it = sorted(self.key["items"].items())[0]
        path = self.root / "skills" / it["skill"] / "evals" / it["case"] / "prompt.md"
        before = path.read_text()
        path.write_text(before.replace("for the PM", "for the PM, rewritten after the sheet"))
        return item_id, it, path, before

    def test_a_changed_request_is_not_judged(self):
        item_id, _, _, _ = self.changed_prompt()
        items, skipped = key_items(self.root, self.key)
        self.assertEqual(len(items), 23)
        self.assertEqual(len(skipped), 1)
        self.assertTrue(skipped[0].startswith(f"{item_id}: request or goal changed since the key was written"))
        code, fake, _ = self.judge("--passes", "1")
        self.assertEqual(code, 1)  # an item went unjudged
        self.assertTrue(all("rewritten after the sheet" not in p for p in fake.prompts))

    @unittest.skipUnless(shutil.which("git"), "needs git")
    def test_a_changed_request_is_read_at_the_keys_commit(self):
        git(self.root, "init", "-q")
        git(self.root, "add", "-A")
        git(self.root, "commit", "-qm", "cases")
        with contextlib.redirect_stdout(io.StringIO()):
            human_rating.main(["sample", "--n", "24", "--seed", "1", "--any-answer", "--sheet", str(self.sheet), "--key", str(self.key_path)],
                              root=self.root)
        key = json.loads(self.key_path.read_text())
        self.assertEqual(len(key["promptsCommit"]), 40)
        item_id, _, path, before = self.changed_prompt()
        git(self.root, "commit", "-qam", "case rewritten after the sheet")
        items, skipped = key_items(self.root, key)
        self.assertEqual((len(items), skipped), (24, []))
        request = next(i["request"] for i in items if i["sheetId"] == item_id)
        self.assertEqual(request, before.split("---", 2)[2].strip())

    @unittest.skipUnless(shutil.which("git"), "needs git")
    def test_a_key_without_hashes_needs_the_commit_it_was_drawn_on(self):
        git(self.root, "init", "-q")
        git(self.root, "add", "-A")
        git(self.root, "commit", "-qm", "cases")
        old = json.loads(json.dumps(self.key))
        for it in old["items"].values():
            it.pop("requestSha256"), it.pop("goalSha256")
        old.pop("promptsCommit", None)
        item_id, _, _, before = self.changed_prompt()
        items, skipped = key_items(self.root, old)  # uncommitted change: cannot tell, skipped
        self.assertEqual(len(items), 23)
        self.assertIn(f"{item_id}: prompt.md has uncommitted changes", skipped[0])
        items, skipped = key_items(self.root, old, "HEAD")
        self.assertEqual((len(items), skipped), (24, []))
        self.assertEqual(next(i["request"] for i in items if i["sheetId"] == item_id), before.split("---", 2)[2].strip())
        self.key_path.write_text(json.dumps(old))
        code, fake, printed = self.judge("--passes", "1", "--prompts-rev", "HEAD")
        self.assertEqual((code, len(fake.prompts)), (0, 24))
        self.assertIn("stores no hash of the requests and goals, read from HEAD", printed)

    def test_key_scores_replace_older_scores_of_the_same_id(self):
        it = next(iter(self.key["items"].values()))
        folder = self.root / "baselines/judge/fake-judge"
        folder.mkdir(parents=True)
        (folder / f"{it['skill']}.json").write_text(json.dumps({"skill": it["skill"], "passes": 1, "costUsd": 0.0, "answers": [
            {"id": it["judgeId"], "words": it["words"] + 7, "judge": 0.0}]}))
        self.judge()
        self.assertEqual(human_rating.judge_score(load_judges(self.root)["fake-judge"], it), 4.0)


class RecordedModeTest(unittest.TestCase):
    def test_recorded_answers_get_the_human_rating_ids(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_repo(root)
            fake = FakeJudge()
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(judge_main(["--recorded", "--model", "fake-judge", "--passes", "1", "-j", "1", "skills/alpha"], root=root, call=fake), 0)
            written = json.loads((root / "baselines/judge/fake-judge/alpha.json").read_text())
            pooled = {(i["judgeId"], i["words"]) for i in human_rating.pool(root, only={"alpha"})}
            self.assertEqual({(a["id"], a["words"]) for a in written["answers"]}, pooled)  # the recorded run, not the stale one
            self.assertTrue(all("stale" not in p for p in fake.prompts))
            self.assertEqual(len(collect(root / "skills/alpha", root / "eval-out/old/answers/alpha")), 48)


if __name__ == "__main__":
    unittest.main()
