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
        (self.root / "skills/s").mkdir(parents=True)  # only catalog skills are shown
        (self.root / "baselines/d.json").write_text(json.dumps({"skill": "d", "model": "claude-sonnet-5-5", "date": "2026-11-01",
                                                               "cases": {"d-001": case(0.0, 0.0, [0, 0])}}))  # a draft: left out
        (self.root / "baselines/s.json").write_text(json.dumps({"skill": "s", "model": "claude-sonnet-5-5", "date": "2026-11-01", "casesHash": "h", "cases": {
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
        (self.root / "baselines/template-arm/s.json").write_text(json.dumps({"casesHash": "h", "cases": {
            "s-001": case(0.7, 0.5, [3, 0]), "s-002": case(0.7, 0.3, [2, 3])}}))
        (self.root / "baselines/judge/claude-haiku-5-5").mkdir(parents=True)
        answers = [{"case": c, "arm": arm, "judge": v} for c in ("s-001", "s-002")
                   for arm, v in (("without", 0.6), ("template", 0.7), ("with", 0.8))]
        (self.root / "baselines/judge/claude-haiku-5-5/s.json").write_text(json.dumps({
            "calibrated": False, "noise": 0.05, "answers": answers,
            "arms": {a: {"words": 500} for a in ("without", "template", "with")}}))
        (self.root / "README.md").write_text("top\n<!-- gains:start -->\nold\n<!-- gains:end -->\nbottom\n")
        out = main(self.root, draws=200)
        readme = (self.root / "README.md").read_text()
        self.assertIn("| 40% | 70% | **90%** | +50 pts | +20 pts |", readme)
        self.assertIn("| Blind LLM judge, Haiku 5.5: 1 of these skills, 2 cases, earlier runs | 60% | 70% | 80% | +20 pts | +10 pts |", readme)
        self.assertNotIn("[+", readme)
        self.assertNotIn("calibrated", readme)
        self.assertTrue(readme.startswith("top\n") and readme.endswith("bottom\n"))
        self.assertIn("| 40% | 70% | **90%** | +50 [+50, +50] |", out)
        self.assertIn("| Blind LLM judge, Haiku 5.5: 1 of these skills, 2 cases, earlier runs | 60% | 70% | 80% | +20 [+20, +20] | +10 [+10, +10] |", out)
        self.assertIn("| Red lines held (the one thing the answer must never do) | 50% | — | **100%** |", out)
        self.assertIn("| `s` | Haiku 5.5 | 60% | 70% | 80% | +20 pts | +10 pts | 5 pts | 500 / 500 / 500 |", out)

    def test_readme_gains_are_the_shown_scores_subtracted_on_one_base(self):
        # a second skill without a template run: the template is then shown only on a row of the skills that have one
        (self.root / "skills/t").mkdir(parents=True)
        (self.root / "baselines/t.json").write_text(json.dumps({"skill": "t", "model": "claude-sonnet-5-5", "date": "2026-11-01", "casesHash": "x", "cases": {
            "t-001": case(0.905, 0.4, [3, 0])}}))
        (self.root / "baselines/template-arm").mkdir()
        (self.root / "baselines/template-arm/s.json").write_text(json.dumps({"casesHash": "h", "cases": {
            "s-001": case(0.7, 0.5, [3, 0]), "s-002": case(0.7, 0.3, [2, 3])}}))
        main(self.root, draws=200)
        readme = (self.root / "README.md").read_text()
        rows = [r for r in readme.splitlines() if r.startswith("| Regex graders")]
        self.assertEqual(len(rows), 2)
        self.assertIn("| — |", rows[0])  # 2 skills, only one with a template run: no template column on this row
        self.assertIn("Regex graders, the 1 skills also run with their template only: 2 cases | 40% | 70% | 90% | +50 pts | +20 pts |", rows[1])
        for r in readme.splitlines():
            cells = [c.strip().strip("*") for c in r.split("|")[1:-1]]
            if len(cells) == 6 and cells[1].endswith("%") and cells[3].endswith("%") and cells[4].endswith("pts"):
                self.assertEqual(int(cells[4].split()[0]), int(cells[3][:-1]) - int(cells[1][:-1]), r)

    def judge_file(self, folder, **extra):
        (self.root / "baselines/judge" / folder).mkdir(parents=True)
        answers = [{"case": c, "arm": arm, "judge": v} for c in ("s-001", "s-002") for arm, v in (("without", 0.6), ("with", 0.8))]
        (self.root / "baselines/judge" / folder / "s.json").write_text(json.dumps({
            "calibrated": False, "noise": 0.05, "answers": answers, "arms": {a: {"words": 500} for a in ("without", "with")}, **extra}))

    def test_other_vendor_judges_are_labelled_by_kind_and_answer_set(self):
        self.judge_file("typesafe--jev-1.14", judgeModel="typesafe/jev-1.14", judgeKind="decision", answerSet="recorded")
        self.judge_file("openai--gpt-6.1-sol", judgeModel="openai/gpt-6.1-sol", judgeKind="llm", answerSet="latest")
        out = main(self.root, draws=200)
        self.assertIn("| Blind decision model, typesafe/jev-1.14: 1 of these skills, 2 cases, recorded runs |", out)
        self.assertIn("| Blind LLM judge, openai/gpt-6.1-sol: 1 of these skills, 2 cases, earlier runs |", out)

    def test_a_limit_trial_stays_out_of_the_tables(self):
        self.judge_file("typesafe--jev-1.14", judgeModel="typesafe/jev-1.14", judgeKind="decision", answerSet="recorded", limit=1)
        out = main(self.root, draws=200)
        self.assertNotIn("jev", out)
        self.assertNotIn("jev", (self.root / "README.md").read_text())

    def test_template_arm_on_other_cases_is_left_out(self):
        (self.root / "baselines/template-arm").mkdir()
        (self.root / "baselines/template-arm/s.json").write_text(json.dumps({"casesHash": "old", "cases": {
            "s-001": case(0.7, 0.5, [3, 0]), "s-002": case(0.7, 0.3, [2, 3])}}))
        self.assertIn("| 40% | — | **90%** |", main(self.root, draws=200))


if __name__ == "__main__":
    unittest.main()
