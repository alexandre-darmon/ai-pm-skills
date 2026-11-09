"""skill-eval-gains.md is computed from the baselines, and the README block follows it."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from eval_gains import main  # noqa: E402


def case(s, w, rl):
    return {"score": s, "scoreWithout": w, "runs": 3, "runsWithout": 3, "fired": 3, "negative": False,
            "graders": {"redline-x": rl, "a": [3, 1]}}


class EvalGainsTest(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        (self.root / "baselines").mkdir()
        (self.root / "baselines/s.json").write_text(json.dumps({"skill": "s", "model": "claude-sonnet-5-5", "date": "2026-11-01", "cases": {
            "s-001": case(1.0, 0.5, [3, 0]), "s-002": case(0.8, 0.3, [3, 3]),
            "s-003": {"runs": 3, "fired": 0, "negative": True, "graders": {}}}}))
        (self.root / "README.md").write_text("top\n<!-- gains:start -->\nold\n<!-- gains:end -->\nbottom\n")

    def test_with_and_without(self):
        out = main(self.root, draws=200)
        self.assertIn("| Regex graders: 1 skill, 2 cases × 3 runs | 40% | — | **90%** | +50 [+50, +50] | — |", out)
        self.assertIn("| 40% | — | **90%** | +50 pts (+50 to +50) | — |", out)
        self.assertIn("| Red lines held (the one thing the answer must never do) | 50% | — | **100%** | | |", out)
        readme = (self.root / "README.md").read_text()
        self.assertIn("**90%**", readme)
        self.assertTrue(readme.startswith("top\n") and readme.endswith("bottom\n") and "old" not in readme)

    def test_template_and_judge_arms(self):
        (self.root / "baselines/template-arm").mkdir()
        (self.root / "baselines/template-arm/s.json").write_text(json.dumps({"cases": {
            "s-001": case(0.7, 0.5, [3, 0]), "s-002": case(0.7, 0.3, [2, 3])}}))
        (self.root / "baselines/judge/claude-haiku-5-5").mkdir(parents=True)
        answers = [{"case": c, "arm": arm, "judge": v} for c in ("s-001", "s-002")
                   for arm, v in (("without", 0.6), ("template", 0.7), ("with", 0.8))]
        (self.root / "baselines/judge/claude-haiku-5-5/s.json").write_text(json.dumps({
            "calibrated": False, "noise": 0.05, "answers": answers,
            "arms": {a: {"words": 500} for a in ("without", "template", "with")}}))
        out = main(self.root, draws=200)
        self.assertIn("| 40% | 70% | **90%** | +50 [+50, +50] |", out)
        self.assertIn("| Blind LLM judge, Haiku 5.5: 1 of these skills, 2 cases, not calibrated | 60% | 70% | 80% | +20 [+20, +20] | +10 [+10, +10] |", out)
        self.assertIn("| 50% | 83% | **100%** |", out)
        self.assertIn("| `s` | Haiku 5.5 | 60% | 70% | 80% | +20 pts | +10 pts | 5 pts | 500 / 500 / 500 |", out)


if __name__ == "__main__":
    unittest.main()
