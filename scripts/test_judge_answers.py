import unittest

from judge_answers import overall, parse_scores, redact

GOOD = '{"sound": 5, "actionable": 3, "honest_about_unknowns": 3, "risk_aware": 3, "specific": 1, "meets_goal": 2, "weakest_point": "x"}'


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


if __name__ == "__main__":
    unittest.main()
