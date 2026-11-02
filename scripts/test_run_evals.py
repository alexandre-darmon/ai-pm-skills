"""The pass rules of run_evals.py, on hand-written `claude plugin eval` results."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from run_evals import summarise, verdict, warnings  # noqa: E402

GRADERS = [
    {"name": "triggered", "type": "tool_used", "weight": 1, "config": {"tool": "Skill", "input_match": "s"}},
    {"name": "has-x", "type": "regex", "weight": 1, "config": {}},
    {"name": "redline-x", "type": "regex", "weight": 3, "config": {}},
]
NEGATIVE = [{"name": "not-triggered", "type": "tool_used", "weight": 1, "config": {"tool": "Skill", "min": 0, "max": 0}}]


def run(fired, has_x, red_line):
    return {"error": None, "graders": [
        {"name": "triggered", "passed": fired, "weight": 1},
        {"name": "has-x", "passed": has_x, "weight": 1},
        {"name": "redline-x", "passed": red_line, "weight": 3},
    ]}


def silent_run(stayed_silent):
    return {"error": None, "graders": [{"name": "not-triggered", "passed": stayed_silent, "weight": 1}]}


def result(arms, *extra):
    return {"claudeVersion": "x", "startedAt": "2026-11-02T00:00:00Z", "partial": False,
            "cases": [{"name": "s-001", "graders": GRADERS, "arms": arms}, *extra]}


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
            "s-001: red line redline-x missed in 1/1 runs",
            "mean delta +0.00: the skill adds nothing over the model alone",
        ])

    def test_without_arm_reused_from_baseline(self):
        s = summarise(result({"with": [run(True, True, True)]}), "s", "h")
        self.assertIn("no score without the skill", verdict(s, 0.8, None)[0])
        s = summarise(result({"with": [run(True, True, True)]}), "s", "h")
        self.assertEqual(verdict(s, 0.8, {"cases": {"s-001": {"scoreWithout": 0.5}}}), [])
        self.assertEqual(s["meanDelta"], 0.5)

    def test_red_line_must_pass_every_run(self):
        runs = [run(True, True, True), run(True, True, True), run(True, True, False)]
        s = summarise(result({"with": runs, "without": [run(False, False, False)]}), "s", "h")
        self.assertEqual(verdict(s, 0.7, None), ["s-001: red line redline-x missed in 1/3 runs"])  # mean 0.75 >= 0.7

    def test_negative_case(self):
        neg = lambda ok: {"name": "s-004", "graders": NEGATIVE, "arms": {"with": [silent_run(ok)], "without": [silent_run(True)]}}  # noqa: E731
        arms = {"with": [run(True, True, True)], "without": [run(False, True, False)]}
        s = summarise(result(arms, neg(True)), "s", "h")
        self.assertEqual(verdict(s, 0.8, None), [])
        self.assertEqual(s["meanDelta"], 0.75)  # the negative case is left out of the delta
        s = summarise(result(arms, neg(False)), "s", "h")
        self.assertEqual(verdict(s, 0.8, None), ["s-004: the skill fired, or the run errored, on a request it should leave alone (1/1 runs)"])
        errored = {"name": "s-004", "graders": NEGATIVE, "arms": {"with": [{"error": "api", "graders": []}]}}
        self.assertEqual(len(verdict(summarise(result(arms, errored), "s", "h"), 0.8, None)), 1)  # silence not shown

    def test_discrimination_warnings(self):
        s = summarise(result({"with": [run(True, True, True)], "without": [run(False, True, False)]}), "s", "h")
        self.assertEqual(warnings(s), ["s-001/has-x: passes without the skill too: it measures the model, not the skill"])
        s = summarise(result({"with": [run(True, True, True)]}), "s", "h")
        verdict(s, 0.8, {"cases": {"s-001": {"scoreWithout": 0.25, "runsWithout": 1,
                                             "graders": {"has-x": [1, 1], "redline-x": [1, 0]}}}})
        self.assertEqual(len(warnings(s)), 1)  # per-grader "without" counts come from the baseline


if __name__ == "__main__":
    unittest.main()
