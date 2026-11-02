"""The pass rules of run_evals.py, on hand-written `claude plugin eval` results."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from run_evals import summarise, verdict  # noqa: E402

GRADERS = [
    {"name": "triggered", "type": "tool_used", "weight": 1, "config": {"tool": "Skill", "input_match": "s"}},
    {"name": "has-x", "type": "regex", "weight": 1, "config": {}},
    {"name": "red-line", "type": "regex", "weight": 3, "config": {}},
]


def run(fired, has_x, red_line):
    return {"error": None, "graders": [
        {"name": "triggered", "passed": fired, "weight": 1},
        {"name": "has-x", "passed": has_x, "weight": 1},
        {"name": "red-line", "passed": red_line, "weight": 3},
    ]}


def result(arms):
    return {"claudeVersion": "x", "startedAt": "2026-11-02T00:00:00Z", "partial": False,
            "cases": [{"name": "s-001", "graders": GRADERS, "arms": arms}]}


class RunEvalsTest(unittest.TestCase):
    def test_two_arms_pass(self):
        s = summarise(result({"with": [run(True, True, True)], "without": [run(False, True, False)]}), "s", "h")
        self.assertEqual(verdict(s, 0.8, None), [])
        case = s["cases"]["s-001"]
        self.assertEqual((case["score"], case["scoreWithout"], case["fired"]), (1.0, 0.25, 1))  # indicator not scored

    def test_red_line_and_no_gain_fail(self):
        s = summarise(result({"with": [run(True, True, False)], "without": [run(False, True, False)]}), "s", "h")
        self.assertEqual(verdict(s, 0.8, None), [
            "s-001: score 0.25 < threshold 0.80",
            "mean delta +0.00: the skill adds nothing over the model alone",
        ])

    def test_without_arm_reused_from_baseline(self):
        s = summarise(result({"with": [run(True, True, True)]}), "s", "h")
        self.assertIn("no score without the skill", verdict(s, 0.8, None)[0])
        s = summarise(result({"with": [run(True, True, True)]}), "s", "h")
        self.assertEqual(verdict(s, 0.8, {"cases": {"s-001": {"scoreWithout": 0.5}}}), [])
        self.assertEqual(s["meanDelta"], 0.5)


if __name__ == "__main__":
    unittest.main()
