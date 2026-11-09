"""The case bootstrap: reproducible, exact when cases agree, and not narrower than the data allow."""
import math
import random
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from eval_stats import bootstrap_ci, macro_mean  # noqa: E402


class BootstrapTest(unittest.TestCase):
    def test_macro_mean_weighs_each_group_the_same(self):
        self.assertAlmostEqual(macro_mean([[1.0], [0.0, 0.0, 0.0]]), 0.5)

    def test_reproducible(self):
        g = [[0.1, 0.5, 0.9], [0.2, 0.4, 0.3, 0.8]]
        self.assertEqual(bootstrap_ci(g, draws=500), bootstrap_ci(g, draws=500))

    def test_identical_cases_give_a_point(self):
        lo, hi = bootstrap_ci([[0.4, 0.4, 0.4], [0.6, 0.6]], draws=200)
        self.assertAlmostEqual(lo, 0.5)
        self.assertAlmostEqual(hi, 0.5)

    def test_single_case_group_stays_fixed(self):
        lo, hi = bootstrap_ci([[0.7]], draws=200)
        self.assertEqual((lo, hi), (0.7, 0.7))

    def test_matches_the_stratified_normal_interval(self):
        rng = random.Random(1)
        g = [[rng.random() for _ in range(n)] for n in (3, 4, 3, 5, 4, 3)]
        h = len(g)
        var = sum(sum((x - sum(s) / len(s)) ** 2 for x in s) / (len(s) - 1) / len(s) for s in g) / h ** 2
        m, half = macro_mean(g), 1.96 * math.sqrt(var)
        lo, hi = bootstrap_ci(g, draws=20_000)
        self.assertAlmostEqual(lo, m - half, delta=0.15 * half)
        self.assertAlmostEqual(hi, m + half, delta=0.15 * half)
        self.assertLess(lo, m)
        self.assertGreater(hi, m)


if __name__ == "__main__":
    unittest.main()
