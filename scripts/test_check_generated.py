"""check_generated.py regenerates the README blocks and skill-eval-gains.md in a scratch copy and compares."""
import contextlib
import io
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import check_generated  # noqa: E402
import eval_gains  # noqa: E402
import readme_catalog  # noqa: E402


def case(s, w):
    return {"score": s, "scoreWithout": w, "runs": 3, "runsWithout": 3, "fired": 3, "negative": False,
            "graders": {"redline-x": [3, 1], "a": [3, 1]}}


class CheckGeneratedTest(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.root, ignore_errors=True)
        (self.root / "baselines").mkdir()
        (self.root / "drafts").mkdir()
        skill = self.root / "skills/build-evals"  # a name readme_catalog has a summary for
        skill.mkdir(parents=True)
        (skill / "SKILL.md").write_text('---\nname: build-evals\nmetadata:\n  stage: "evaluate"\n---\nbody\n')
        (self.root / "baselines/build-evals.json").write_text(json.dumps({
            "skill": "build-evals", "model": "claude-sonnet-5-5", "date": "2026-11-01", "casesHash": "h",
            "cases": {"build-evals-001": case(1.0, 0.5), "build-evals-002": case(0.8, 0.3)}}))
        (self.root / "README.md").write_text("top\n<!-- gains:start -->\nold\n<!-- gains:end -->\n"
                                             "mid\n<!-- catalog:start -->\nold\n<!-- catalog:end -->\nbottom\n")
        (self.root / "skill-eval-gains.md").write_text("old\n")

    def fresh(self):
        with contextlib.redirect_stdout(io.StringIO()):
            eval_gains.main(self.root)
            readme_catalog.main(self.root)

    def run_main(self):
        with contextlib.redirect_stdout(io.StringIO()):
            return check_generated.main(self.root)

    def test_stale_files_are_reported_and_left_alone(self):
        before = (self.root / "README.md").read_text()
        self.assertEqual(sorted(f for f, _ in check_generated.stale(self.root)), ["README.md", "skill-eval-gains.md"])
        self.assertEqual((self.root / "README.md").read_text(), before)  # nothing written
        self.assertEqual(self.run_main(), 1)

    def test_fresh_files_pass(self):
        self.fresh()
        self.assertEqual(check_generated.stale(self.root), [])
        self.assertEqual(self.run_main(), 0)

    def test_hand_edit_of_a_block_is_caught(self):
        self.fresh()
        readme = self.root / "README.md"
        readme.write_text(readme.read_text().replace("### Available (1)", "### Available (2)"))
        problems = check_generated.stale(self.root)
        self.assertEqual([f for f, _ in problems], ["README.md"])
        self.assertIn("+### Available (1)", problems[0][1])

    def test_text_outside_the_blocks_is_free(self):
        self.fresh()
        readme = self.root / "README.md"
        readme.write_text(readme.read_text().replace("mid\n", "anything a human wrote\n"))
        self.assertEqual(check_generated.stale(self.root), [])

    def test_new_baseline_makes_it_stale(self):
        self.fresh()
        b = json.loads((self.root / "baselines/build-evals.json").read_text())
        b["cases"]["build-evals-002"]["score"] = 0.2
        (self.root / "baselines/build-evals.json").write_text(json.dumps(b))
        self.assertEqual(sorted(f for f, _ in check_generated.stale(self.root)), ["README.md", "skill-eval-gains.md"])


if __name__ == "__main__":
    unittest.main()
