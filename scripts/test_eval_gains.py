"""skill-eval-gains.md is computed from the baselines, and the README block follows it."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from eval_gains import main  # noqa: E402


class EvalGainsTest(unittest.TestCase):
    def test_gains(self):
        root = Path(tempfile.mkdtemp())
        (root / "baselines").mkdir()
        case = lambda s, w, rl: {"score": s, "scoreWithout": w, "runs": 3, "runsWithout": 3, "fired": 3, "negative": False,
                                 "graders": {"redline-x": rl, "a": [3, 1]}}
        (root / "baselines/s.json").write_text(json.dumps({"skill": "s", "date": "2026-11-01", "cases": {
            "s-001": case(1.0, 0.5, [3, 0]), "s-002": case(0.8, 0.3, [3, 3]),
            "s-003": {"runs": 3, "fired": 0, "negative": True, "graders": {}}}}))
        (root / "README.md").write_text("top\n<!-- gains:start -->\nold\n<!-- gains:end -->\nbottom\n")
        out = main(root)
        self.assertIn("| Mean score on the scored cases | 40% | **90%** |", out)
        self.assertIn("| 40% | **90%** | +50 pts | 100% vs 50% | 2 × 3 |", out)
        readme = (root / "README.md").read_text()
        self.assertIn("**90%**", readme)
        self.assertTrue(readme.startswith("top\n") and readme.endswith("bottom\n") and "old" not in readme)


if __name__ == "__main__":
    unittest.main()
