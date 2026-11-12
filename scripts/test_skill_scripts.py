"""Known values for the statistical scripts shipped inside catalog skills (skills/*/scripts/*.py).

The scripts are imported by path and never edited from here: editing one would make its skill's recorded run stale.
A wrong value is reported as an expectedFailure with a comment, so the suite stays green and the defect stays visible.

References are computed independently: the Wilson interval as the two roots of (p_hat - p)^2 = z^2 p (1 - p) / n,
found by bisection, plus a few literal values (to 4 decimals) checked by hand.
"""
import contextlib
import csv
import importlib.util
import io
import math
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
Z = 1.96

KNOWN = {
    "agent-evals/scripts/agent_reliability.py",
    "ai-interaction-patterns/scripts/reliability_table.py",
    "ai-feasibility-spike/scripts/spike_readout.py",
    "ai-vendor-evaluation/scripts/bakeoff.py",
    "red-team-evals/scripts/redteam_rates.py",
    "error-analysis/scripts/failure_modes.py",
    "llm-judge-calibration/scripts/judge_metrics.py",
    "production-evals-monitoring/scripts/control_limits.py",
}


def load(rel):
    """Import skills/<rel> as a module without writing bytecode into the skill folder."""
    path = ROOT / "skills" / rel
    name = "skill_" + rel.replace("/", "_").replace("-", "_").removesuffix(".py")
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    old, sys.dont_write_bytecode = sys.dont_write_bytecode, True
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.dont_write_bytecode = old
    return mod


def run_main(mod, argv):
    """Run a script's main() with argv, return its stdout."""
    out, old = io.StringIO(), sys.argv
    sys.argv = ["script"] + list(argv)
    try:
        with contextlib.redirect_stdout(out):
            if "argv" in mod.main.__code__.co_varnames[:mod.main.__code__.co_argcount]:
                mod.main(list(argv))
            else:
                mod.main()
    finally:
        sys.argv = old
    return out.getvalue()


def wilson_ref(k, n, z=Z):
    """Wilson bounds as the roots of the score equation, by bisection (independent of the closed form)."""
    ph = k / n
    f = lambda p: (ph - p) ** 2 - z * z * p * (1 - p) / n  # noqa: E731  >= 0 outside the interval

    def root(a, b, inside_at_b):
        for _ in range(200):
            m = (a + b) / 2
            if (f(m) <= 0) == inside_at_b:
                b = m
            else:
                a = m
        return (a + b) / 2

    lo = 0.0 if k == 0 else root(0.0, ph, True)
    hi = 1.0 if k == n else root(1.0, ph, True)
    return lo, hi


WILSON_COPIES = [
    ("red-team-evals/scripts/redteam_rates.py", lambda m, k, n: m.wilson(k, n)),
    ("ai-interaction-patterns/scripts/reliability_table.py", lambda m, k, n: m.wilson(k, n)),
    ("agent-evals/scripts/agent_reliability.py", lambda m, k, n: m.wilson(k, n)),
    ("ai-feasibility-spike/scripts/spike_readout.py", lambda m, k, n: m.wilson(k, n)),
    ("ai-vendor-evaluation/scripts/bakeoff.py", lambda m, k, n: m.wilson(k, n)),
    ("error-analysis/scripts/failure_modes.py", lambda m, k, n: m.wilson(k, n)),
    ("llm-judge-calibration/scripts/judge_metrics.py", lambda m, k, n: m.wilson(k, n)),
]


class Inventory(unittest.TestCase):
    def test_every_skill_script_is_covered(self):
        found = {str(p.relative_to(ROOT / "skills")) for p in (ROOT / "skills").glob("*/scripts/*.py")}
        self.assertEqual(found - KNOWN, set(), "a skill ships a new script: add its known values here")


class ReliabilityTable(unittest.TestCase):
    """ai-interaction-patterns: a confidence figure is shown only from the lower bound, and only once the tolerated rate is set."""

    def setUp(self):
        self.m = load("ai-interaction-patterns/scripts/reliability_table.py")

    def test_top_bucket(self):
        v = self.m.verdict(286, 310, claim=0.95, tolerate=None, min_cases=30)
        self.assertAlmostEqual(v["lo"], 0.887, places=3)
        self.assertAlmostEqual(v["hi"], 0.947, places=3)
        self.assertEqual(v["claim"], "contradicted")  # "95% sure" is above the upper bound
        self.assertIn("set --tolerate", v["show"])
        v = self.m.verdict(286, 310, claim=None, tolerate=0.85, min_cases=30)
        self.assertIn("at least 85 in 100", v["show"])  # 0.887 rounded down to 5 points

    def test_low_bucket_shows_no_figure(self):
        self.assertIn("no figure", self.m.verdict(48, 100, claim=None, tolerate=0.85, min_cases=30)["show"])
        self.assertIn("fewer than 30", self.m.verdict(9, 10, claim=None, tolerate=0.85, min_cases=30)["show"])


class RedTeamRates(unittest.TestCase):
    """red-team-evals: a class reads "under" a tolerance only when the Wilson upper bound falls below it."""

    def setUp(self):
        self.m = load("red-team-evals/scripts/redteam_rates.py")

    def test_sizing_with_zero_successes(self):
        self.assertEqual(self.m.seeds_needed(0.01, 0), 381)  # 0/381: upper bound just under 1%
        self.assertLess(self.m.wilson(0, 381)[1], 0.01)
        self.assertGreater(self.m.wilson(0, 380)[1], 0.01)  # one seed fewer reads undecided
        self.assertGreater(self.m.seeds_needed(0.01, 1), 381)  # a success needs more seeds

    def test_share_parses_percent_and_fraction(self):
        self.assertAlmostEqual(self.m.share("1%"), 0.01)
        self.assertAlmostEqual(self.m.share("0.01"), 0.01)


class WilsonReference(unittest.TestCase):
    def test_reference_matches_literal_values(self):
        for (k, n), (lo, hi) in {(0, 10): (0.0, 0.2775), (10, 10): (0.7225, 1.0), (5, 10): (0.2366, 0.7634),
                                 (1, 20): (0.0089, 0.2361), (28, 30): (0.7868, 0.9815)}.items():
            rlo, rhi = wilson_ref(k, n)
            self.assertAlmostEqual(rlo, lo, places=4, msg=f"{k}/{n}")
            self.assertAlmostEqual(rhi, hi, places=4, msg=f"{k}/{n}")


class WilsonCopies(unittest.TestCase):
    def test_every_copy_agrees_with_the_reference(self):
        for rel, call in WILSON_COPIES:
            mod = load(rel)
            for n in (1, 2, 3, 5, 10, 20, 30, 47, 100, 150, 400):
                for k in sorted({0, 1, n // 3, n // 2, n - 1, n} & set(range(n + 1))):
                    lo, hi = call(mod, k, n)
                    rlo, rhi = wilson_ref(k, n)
                    with self.subTest(script=rel, k=k, n=n):
                        self.assertLess(abs(lo - rlo), 1e-3)
                        self.assertLess(abs(hi - rhi), 1e-3)
                        self.assertTrue(-1e-12 <= lo <= k / n + 1e-12 and k / n - 1e-12 <= hi <= 1.0 + 1e-12)  # float noise at k = 0 or n

    def test_edges_are_exact(self):
        for rel, call in WILSON_COPIES:
            mod = load(rel)
            with self.subTest(script=rel):
                self.assertAlmostEqual(call(mod, 0, 30)[0], 0.0, places=12)
                self.assertAlmostEqual(call(mod, 30, 30)[1], 1.0, places=12)
                self.assertAlmostEqual(call(mod, 30, 30)[0], 30 / (30 + Z * Z), places=4)  # k = n: n / (n + z^2)

    def test_empty_class_is_nan_where_guarded(self):
        for rel in ("ai-vendor-evaluation/scripts/bakeoff.py", "error-analysis/scripts/failure_modes.py",
                    "llm-judge-calibration/scripts/judge_metrics.py"):
            self.assertTrue(math.isnan(load(rel).wilson(0, 0)[0]), rel)


class AgentReliability(unittest.TestCase):
    m = load("agent-evals/scripts/agent_reliability.py")

    def test_pass_hat_k(self):
        self.assertAlmostEqual(self.m.pass_hat_k(4, 5, 3), 0.4)        # C(4,3)/C(5,3)
        self.assertAlmostEqual(self.m.pass_hat_k(5, 5, 3), 1.0)
        self.assertAlmostEqual(self.m.pass_hat_k(2, 5, 3), 0.0)
        self.assertAlmostEqual(self.m.pass_hat_k(9, 10, 1), 0.9)       # k = 1 is pass@1

    def test_pass_at_k(self):
        self.assertAlmostEqual(self.m.pass_at_k(2, 5, 3), 0.9)         # 1 - C(3,3)/C(5,3)
        self.assertAlmostEqual(self.m.pass_at_k(0, 5, 3), 0.0)
        self.assertAlmostEqual(self.m.pass_at_k(1, 5, 1), 0.2)

    def test_zero_bound(self):
        r3, exact = self.m.zero_bound(300)
        self.assertAlmostEqual(r3, 0.01)
        self.assertAlmostEqual(exact, 1 - 0.05 ** (1 / 300))
        self.assertAlmostEqual(exact, 0.009936, places=5)

    def test_cli_per_task_rates(self):
        out = run_main(self.m, ["--k", "3", "5/5", "4/5", "5/5", "2/5", "5/5"])
        self.assertIn("pass@1 (mean per-trial success): 84.0%", out)    # (1 + .8 + 1 + .4 + 1) / 5
        self.assertIn("pass^3 (all 3 trials succeed): 68.0%", out)      # (1 + .4 + 1 + 0 + 1) / 5
        self.assertIn("pass@1 ^ 3 = 59.3%", out)
        self.assertIn("pass@3 (at least one of 3): 98.0%", out)        # (1 + 1 + 1 + .9 + 1) / 5

    def test_cli_target_and_per_trial(self):
        out = run_main(self.m, ["--target", "0.01", "--per-trial", "0.9", "--k", "3"])
        self.assertIn("300 clean trials", out)
        self.assertIn("pass^3 = 72.9%, pass@3 = 99.9%", out)

    def test_cli_attack_uses_rule_of_three_at_zero(self):
        out = run_main(self.m, ["--attack", "send_outside=0/150", "--attack", "change_payee=2/150"])
        self.assertIn("send_outside: 0/150 = 0.0%, upper bound 2.0% (rule of three", out)
        hi = wilson_ref(2, 150)[1]
        self.assertIn(f"change_payee: 2/150 = 1.3%, upper bound {100 * hi:.1f}% (Wilson)", out)


class SpikeReadout(unittest.TestCase):
    m = load("ai-feasibility-spike/scripts/spike_readout.py")

    def test_readings(self):
        r = self.m.reading
        self.assertEqual(r(50, 50, 0.90, 0.75), "clears")      # lower 50 / 53.84 = 0.929
        self.assertEqual(r(28, 30, 0.90, 0.75), "promising")   # 0.787 to 0.981
        self.assertEqual(r(30, 30, 0.90, 0.75), "promising")   # lower 0.886 < bar, point 1.0
        self.assertEqual(r(9, 10, 0.90, 0.75), "undecided")    # lower 0.596 < stop line
        self.assertEqual(r(5, 10, 0.90, 0.75), "short")        # upper 0.763: above stop, below bar
        self.assertEqual(r(3, 10, 0.90, 0.75), "dead")         # upper 0.604 < stop

    def test_plan_is_the_smallest_n(self):
        self.assertEqual(self.m.plan(0.75, 0), 12)              # n / (n + z^2) >= 0.75 from n = 11.52
        for errors in (0, 1, 2):
            n = self.m.plan(0.75, errors)
            self.assertGreaterEqual(wilson_ref(n - errors, n)[0], 0.75 - 1e-9)
            self.assertLess(wilson_ref(n - 1 - errors, n - 1)[0], 0.75)

    def test_size(self):
        self.assertEqual(self.m.size(0.90, 0.05), 139)          # 1.96^2 * 0.09 / 0.0025 = 138.3
        self.assertEqual(self.m.size(0.95, 0.05), 73)           # 72.99

    def test_cli_cost_per_correct_answer(self):
        out = run_main(self.m, ["--class", "a=28/30", "--class", "b=9/10", "--bar", "0.90", "--stop", "0.75",
                                "--spend", "37", "--appetite", "0.25"])
        self.assertIn("cost per correct answer: 1.000", out)    # 37 / (28 + 9) correct, not / 40 answers
        self.assertIn("over, 4.0 times", out)
        self.assertIn("decision the readings point to: reshape", out)


class Bakeoff(unittest.TestCase):
    m = load("ai-vendor-evaluation/scripts/bakeoff.py")

    def test_paired_noise_and_cost(self):
        # 40 cases: both right 28, A only 8, B only 2, both wrong 2 -> A 36/40, B 30/40.
        data = ([("x", {"A": 1, "B": 1})] * 28 + [("x", {"A": 1, "B": 0})] * 8
                + [("x", {"A": 0, "B": 1})] * 2 + [("x", {"A": 0, "B": 0})] * 2)
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.m.report(["A", "B"], data, volume=1000, costs={"A": 9000.0, "B": 9000.0})
        out = out.getvalue()
        lo, hi = wilson_ref(36, 40)
        self.assertIn(f"A            36/40 = 90.0%  [{100 * lo:.1f}% to {100 * hi:.1f}%]", out)
        # gap 6/40 = 15.0 pts, noise 2 * sqrt(10) / 40 = 15.8 pts: a tie
        self.assertIn("A vs B: d = 10 (A only 8, B only 2), gap +15.0 pts, noise 15.8 pts -> tie", out)
        self.assertIn("(1,000 x 90.0% = 900 correct) = 10.00 EUR", out)
        self.assertIn("(1,000 x 75.0% = 750 correct) = 12.00 EUR", out)


class FailureModes(unittest.TestCase):
    m = load("error-analysis/scripts/failure_modes.py")

    def test_shares_come_from_the_random_stream(self):
        tmp = Path(tempfile.mkdtemp())
        rows = ([("random", "")] * 6 + [("random", "wrong_amount")] * 3 + [("random", "missed_clause")]
                + [("targeted", "wrong_amount")] * 2 + [("targeted", "invented_reference")])
        with open(tmp / "log.csv", "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["trace_id", "stream", "class", "mode"])
            for i, (s, mode) in enumerate(rows, 1):
                w.writerow([i, s, "claims", mode])
        (tmp / "costs.csv").write_text("mode,cost_eur\nwrong_amount,100\nmissed_clause,to source\n")
        out = run_main(self.m, [str(tmp / "log.csv"), "--costs", str(tmp / "costs.csv"), "--monthly-volume", "1000"])
        self.assertIn("Traces read: 13 (random 10, targeted 3)", out)
        self.assertIn("Last new mode at trace 13; traces read since: 0", out)
        self.assertIn("NOT reached", out)
        lo, hi = wilson_ref(6, 10)
        self.assertIn(f"6/10 = 60.0% [{100 * lo:.1f}%, {100 * hi:.1f}%]", out)
        lo, hi = wilson_ref(3, 10)
        self.assertIn(f"| wrong_amount | 3 | 2 | 30.0% [{100 * lo:.1f}%, {100 * hi:.1f}%] |", out)
        self.assertIn(f"30,000 EUR [{1000 * lo * 100:,.0f} EUR, {1000 * hi * 100:,.0f} EUR]", out)
        self.assertIn(f"not seen in random, up to {100 * wilson_ref(0, 10)[1]:.1f}%", out)
        self.assertIn("| missed_clause | 1 | 0 | 10.0%", out)
        self.assertIn("to source", out)


class JudgeMetrics(unittest.TestCase):
    m = load("llm-judge-calibration/scripts/judge_metrics.py")

    def test_rogan_gladen(self):
        self.assertAlmostEqual(self.m.corrected_rate(0.85, 0.90, 0.80), 0.65 / 0.70)
        self.assertAlmostEqual(self.m.corrected_rate(0.30, 0.90, 0.80), 0.10 / 0.70)
        self.assertEqual(self.m.corrected_rate(0.95, 0.90, 0.80), 1.0)   # 1.071 clipped
        self.assertEqual(self.m.corrected_rate(0.10, 0.90, 0.80), 0.0)   # -0.143 clipped
        self.assertIsNone(self.m.corrected_rate(0.5, 0.5, 0.5))          # Youden 0: undefined
        # a perfect judge needs no correction
        self.assertAlmostEqual(self.m.corrected_rate(0.37, 1.0, 1.0), 0.37)

    def test_cli_tpr_tnr_kappa(self):
        tmp = Path(tempfile.mkdtemp()) / "split.csv"
        rows = [("pass", "pass")] * 18 + [("pass", "fail")] * 2 + [("fail", "pass")] * 3 + [("fail", "fail")] * 17
        tmp.write_text("human,judge\n" + "".join(f"{h},{j}\n" for h, j in rows))
        out = run_main(self.m, [str(tmp), "--observed-pass", "340", "--observed-n", "400", "--resamples", "2000"])
        lo, hi = wilson_ref(18, 20)
        self.assertIn(f"0.900   95% CI {lo:.3f} to {hi:.3f}   (18/20)", out)    # TPR
        lo, hi = wilson_ref(17, 20)
        self.assertIn(f"0.850   95% CI {lo:.3f} to {hi:.3f}   (17/20)", out)    # TNR
        self.assertIn("Raw agreement                              0.875", out)
        self.assertIn("Cohen's kappa (judge vs expert)            0.750", out)  # (0.875 - 0.5) / 0.5
        est = (0.85 + 0.85 - 1) / 0.75
        self.assertIn(f"corrected          {est:.3f}", out)
        line = next(l for l in out.splitlines() if "bootstrap CI" in l)
        blo, bhi = (float(x) for x in line.split("CI ")[1].split(" to "))
        self.assertTrue(blo < est < bhi)

    def test_example_csv_runs(self):
        out = run_main(self.m, [str(ROOT / "skills/llm-judge-calibration/scripts/example.csv")])
        self.assertIn("TPR (judge passes", out)


class ControlLimits(unittest.TestCase):
    m = load("production-evals-monitoring/scripts/control_limits.py")

    def test_three_sigma_limits(self):
        out = run_main(self.m, ["--centre", "90", "--n", "100", "--latest", "80"])
        self.assertIn("sigma 3.00 points, 3-sigma limits 81.0% to 99.0% (±9.0 points)", out)  # sqrt(.09 / 100)
        self.assertIn("latest 80.0%: OUTSIDE the limits", out)

    def test_run_rule(self):
        hist = ",".join(["96"] * 2 + ["92"] * 8)  # centre 92.8%: the last 8 periods, and the latest, are below
        out = run_main(self.m, ["--history", hist, "--n", "150", "--latest", "92"])
        self.assertIn("centre line 92.8% from 10 periods", out)
        self.assertIn("inside the limits", out)
        self.assertIn("FIRED (9 below the centre)", out)
        hist = ",".join(["96"] * 4 + ["92"] * 4)
        out = run_main(self.m, ["--history", hist, "--n", "150", "--latest", "92"])
        self.assertIn("not met (5 below the centre)", out)

    def test_sample_size_for_a_drop(self):
        out = run_main(self.m, ["--centre", "90", "--drop", "5"])
        self.assertIn("n >= 324 per class per period", out)    # 9 * .9 * .1 / .05^2
        self.assertIn("n >= 576 for ~84%", out)                # 16 * .9 * .1 / .05^2

    @unittest.expectedFailure
    def test_sample_size_exact_integer(self):
        # Finding: math.ceil on a float product. 9 * 0.95 * 0.05 / 0.05^2 is exactly 171, the script computes
        # 171.00000000000009 and prints 172 (one case too many; conservative, but not the stated formula).
        # Same at --centre 94 --drop 3: 564 exact, 565 printed. A fix would be ceil(round(x, 9)) in the skill script.
        out = run_main(self.m, ["--centre", "95", "--drop", "5"])
        self.assertIn("n >= 171 per class per period", out)


if __name__ == "__main__":
    unittest.main()
