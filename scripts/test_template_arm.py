import unittest

from template_arm import compare


def summary(score, without=0.2):
    return {"cases": {"a": {"score": score, "scoreWithout": without}, "neg": {"score": 0.0, "scoreWithout": None, "negative": True}}}


class CompareTest(unittest.TestCase):
    def test_method_must_beat_the_template_by_ten_points(self):
        self.assertTrue(compare(summary(1.0), summary(0.9))["methodBeatsFormat"])
        row = compare(summary(1.0), summary(0.95))
        self.assertFalse(row["methodBeatsFormat"])
        self.assertAlmostEqual(row["methodGain"], 0.05)  # the negative case is left out


if __name__ == "__main__":
    unittest.main()
