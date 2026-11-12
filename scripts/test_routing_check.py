import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

import routing_check as rc
from validate_skills import check_routing

DOCS = {
    "model-selection": "model selection Choose a model for an AI use case on your own eval suite: cost per success, latency, hosting.",
    "release-to-production": "release to production Plan the release of an AI change through shadow, canary and A/B.",
    "build-evals": "build evals Build or review AI eval sets, graders, thresholds.",
}


def row(cid, expected, rank, predicted=None):
    return {"id": cid, "zone": "", "expected": expected, "rank": rank, "predicted": predicted or expected, "top": [["x", 0.5]]}


def rec(rank, margin=None, edge=0.1, winner="x"):
    """One recorded case of routing/baseline.json."""
    return {"rank": rank, "winner": winner, "margin": margin, "edge": edge}


def write_skill(root: Path, where: str, name: str, description: str):
    folder = root / where / name
    folder.mkdir(parents=True)
    (folder / "SKILL.md").write_text(f"---\nname: {name}\ndescription: '{description}'\n---\n\nbody\n")


class TokensTest(unittest.TestCase):
    def test_stem_merges_plurals_and_verb_forms(self):
        self.assertEqual(rc.stem("evals"), rc.stem("eval"))
        self.assertEqual(rc.stem("graders"), rc.stem("grader"))
        self.assertEqual(rc.stem("labelling"), rc.stem("label"))
        self.assertEqual(rc.stem("policies"), "policy")
        self.assertEqual(rc.stem("status"), "status")  # no -s stripping after u or s
        self.assertEqual(rc.stem("process"), "process")

    def test_stem_merges_e_stems_with_their_past_and_ing_forms(self):
        for a, b in (("release", "released"), ("score", "scored"), ("route", "routed"), ("route", "routing"),
                     ("code", "coding"), ("price", "pricing"), ("release", "releases")):
            self.assertEqual(rc.stem(a), rc.stem(b), (a, b))
        self.assertEqual(rc.stem("notes"), "note")  # dropping the e would make it the stop word "not"
        self.assertEqual(rc.stem("speed"), "speed")  # -eed is not a past tense

    def test_tokens_drop_stop_words(self):
        self.assertEqual(rc.tokens("Which model should we use for the KYC checks?"), ["model", "kyc", "check"])


class RankTest(unittest.TestCase):
    def test_rank_is_deterministic_and_lexical(self):
        index = rc.Index(DOCS)
        ranking = index.rank("Which model is cheapest per success on our suite?")
        self.assertEqual(ranking[0][0], "model-selection")
        self.assertEqual(ranking, index.rank("Which model is cheapest per success on our suite?"))
        # the known weakness: a request with no shared word scores zero everywhere, so the proxy says none
        rows = rc.score_cases([{"id": "c", "expected": "build-evals", "request": "Is the quality good enough?"}], index)
        self.assertEqual(rows[0]["predicted"], rc.NONE)

    def test_summary_counts_hits_and_confusions(self):
        rows = [row("a", "model-selection", 1), row("b", "build-evals", 2, "model-selection"), row("n", rc.NONE, None, "build-evals")]
        s = rc.summary(rows)
        self.assertAlmostEqual(s["top1"], 1 / 3)
        self.assertEqual(s["top3"], 1.0)  # in-scope cases only
        self.assertEqual({(c["expected"], c["predicted"]) for c in s["confusion"]},
                         {("build-evals", "model-selection"), (rc.NONE, "build-evals")})


class RuleTest(unittest.TestCase):
    def test_a_case_won_by_a_clear_margin_cannot_be_taken(self):
        baseline = {"cases": {"a": rec(1, margin=0.05)}}
        self.assertEqual(rc.failures([row("a", "x", 1)], baseline), [])
        fails = rc.failures([row("a", "x", 2, "thief")], baseline)  # still in the top 3: the old rule let it pass
        self.assertEqual(len(fails), 1)
        self.assertIn("a: thief took it from x", fails[0])

    def test_near_ties_share_the_slack(self):
        baseline = {"cases": {"a": rec(1, margin=0.005), "b": rec(1, margin=0.01), "c": rec(1, margin=0.05)}}
        one = [row("a", "x", 2, "y"), row("b", "x", 1), row("c", "x", 1)]
        self.assertEqual(rc.failures(one, baseline), [])
        self.assertIn("moved from rank 1 to 2 (under the", rc.notes(one, baseline)[0])
        two = [row("a", "x", 2, "y"), row("b", "x", 2, "y"), row("c", "x", 1)]
        self.assertIn("2 near-tie cases lost top-1 (a, b; slack 1)", rc.failures(two, baseline)[0])

    def test_top3_ratchet_above_the_floor_only(self):
        baseline = {"cases": {"b": rec(3, edge=0.05), "t": rec(3, edge=0.001), "c": rec(9, edge=None)}}
        rows = [row("b", "y", 4, "z"), row("t", "y", 4, "z"), row("c", "w", 12, "z")]
        fails = rc.failures(rows, baseline)
        self.assertEqual(len(fails), 1)
        self.assertIn("b: y fell from rank 3 to 4", fails[0])
        self.assertTrue(any(n.startswith("t: ") and "not gated" in n for n in rc.notes(rows, baseline)))

    def test_a_soft_winner_that_collapses_still_fails(self):
        baseline = {"cases": {"a": rec(1, margin=0.001, edge=0.2)}}
        self.assertIn("a: x fell from rank 1 to 7", rc.failures([row("a", "x", 7, "y")], baseline)[0])

    def test_a_recorded_case_cannot_vanish(self):
        fails = rc.failures([row("a", "x", 1)], {"cases": {"a": rec(1, 0.1), "gone": rec(2)}})
        self.assertEqual(len(fails), 1)
        self.assertIn("gone: recorded in routing/baseline.json but gone from cases.yaml", fails[0])

    def test_none_cases_and_new_cases_are_not_gated(self):
        baseline = {"cases": {}}
        rows = [row("n", rc.NONE, None, "x"), row("new", "x", 20, "y")]
        self.assertEqual(rc.failures(rows, baseline), [])
        self.assertIn("new: new case, not gated until --update", rc.notes(rows, baseline))

    def test_improvement_is_noted(self):
        self.assertEqual(rc.notes([row("a", "x", 1)], {"cases": {"a": rec(2)}}), ["a: x improved from rank 2 to 1"])

    def test_worse_lists_every_lost_rank_and_vanished_case(self):
        baseline = {"cases": {"a": rec(1, 0.001), "b": rec(5, edge=None), "gone": rec(1, 0.3)}}
        lost = rc.worse([row("a", "x", 2, "y"), row("b", "x", 4, "y")], baseline)
        self.assertEqual(lost, ["gone: gone from cases.yaml", "a: x rank 1 -> 2 (top-1 now y)"])


class BroadenTest(unittest.TestCase):
    """The usual collision: one description grows until it takes a neighbour's request."""

    def test_a_description_that_grows_into_a_neighbour_fails(self):
        cases = [{"id": "r1", "expected": "model-selection", "request": "Which model has the best cost per success and latency?"},
                 {"id": "r2", "expected": "release-to-production", "request": "Plan the canary and shadow release."}]
        baseline = rc.record(rc.score_cases(cases, rc.Index(DOCS)))
        self.assertEqual(baseline["cases"]["r1"]["rank"], 1)
        self.assertGreaterEqual(baseline["cases"]["r1"]["margin"], rc.FLOOR)
        grown = {**DOCS, "build-evals": DOCS["build-evals"] + " Which model has the best cost per success and latency?"}
        rows = rc.score_cases(cases, rc.Index(grown))
        self.assertEqual(rows[0]["rank"], 2)  # still in the top 3: a rank-only ratchet would pass
        fails = rc.failures(rows, baseline)
        self.assertEqual(len(fails), 1)
        self.assertIn("r1: build-evals took it from model-selection", fails[0])

    def test_repo_reviewer_mutation_fails(self):
        """Adding route-002's four rarest words to ai-vendor-evaluation took it and passed the old gate."""
        skills = rc.load_skills(rc.ROOT)
        cases = rc.load_cases(rc.ROOT / "routing" / "cases.yaml")
        baseline = json.loads((rc.ROOT / "routing" / "baseline.json").read_text())
        if baseline["cases"]["route-002"]["margin"] < rc.FLOOR:
            self.skipTest("route-002 is a near tie in the current record")
        index = rc.Index(skills)
        case = next(c for c in cases if c["id"] == "route-002")
        words = sorted(set(rc.tokens(case["request"])), key=lambda t: (-index.idf.get(t, 0), t))[:4]
        grown = {**skills, "ai-vendor-evaluation": skills["ai-vendor-evaluation"] + " " + " ".join(words)}
        rows = rc.score_cases(cases, rc.Index(grown))
        self.assertEqual(next(r for r in rows if r["id"] == "route-002")["predicted"], "ai-vendor-evaluation")
        self.assertTrue(any("route-002: ai-vendor-evaluation took it" in f for f in rc.failures(rows, baseline)))

    def test_repo_every_catalog_description_is_gated(self):
        """Wiping any catalog skill's description must fail the gate: each one has a case the ratchet holds."""
        skills = rc.load_skills(rc.ROOT)
        cases = rc.load_cases(rc.ROOT / "routing" / "cases.yaml")
        baseline = json.loads((rc.ROOT / "routing" / "baseline.json").read_text())
        catalog = {p.name for p in (rc.ROOT / "skills").glob("*") if (p / "SKILL.md").is_file()}
        unseen = [n for n in sorted(catalog) if not rc.failures(rc.score_cases(cases, rc.Index({**skills, n: ""})), baseline)]
        self.assertEqual(unseen, [], "no gated case holds these descriptions")


class MainTest(unittest.TestCase):
    def make_repo(self, tmp: Path):
        for name, desc in DOCS.items():
            write_skill(tmp, "skills" if name != "build-evals" else "drafts", name, desc.split(" ", 2)[2])
        (tmp / "routing").mkdir()
        (tmp / "routing" / "cases.yaml").write_text(
            "cases:\n  - id: r1\n    expected: model-selection\n    request: Which model has the best cost per success?\n"
            "  - id: r2\n    expected: none\n    request: Draft an interview guide.\n")

    def run_main(self, *args):
        out = io.StringIO()
        with redirect_stdout(out):
            code = rc.main(list(args))
        return code, out.getvalue()

    def test_missing_baseline_fails_then_update_records_it(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            self.make_repo(tmp)
            code, out = self.run_main(str(tmp))
            self.assertEqual(code, 1)
            self.assertIn("baseline.json is missing", out)
            code, _ = self.run_main(str(tmp), "--update", "--json", str(tmp / "out.json"))
            self.assertEqual(code, 0)
            self.assertEqual(json.loads((tmp / "routing" / "baseline.json").read_text())["cases"]["r1"]["rank"], 1)
            self.assertEqual(json.loads((tmp / "out.json").read_text())["summary"]["cases"], 2)

    def test_update_refuses_a_worse_record_unless_accepted(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            self.make_repo(tmp)
            self.assertEqual(self.run_main(str(tmp), "--update")[0], 0)
            before = (tmp / "routing" / "baseline.json").read_text()
            # the case drops out of the set: a silent --update would drop it from the gate
            (tmp / "routing" / "cases.yaml").write_text("cases:\n  - id: r2\n    expected: none\n    request: Draft a guide.\n")
            code, out = self.run_main(str(tmp), "--update")
            self.assertEqual(code, 1)
            self.assertIn("not recorded", out)
            self.assertIn("r1: gone from cases.yaml", out)
            self.assertEqual((tmp / "routing" / "baseline.json").read_text(), before)
            self.assertIn("r1: recorded in routing/baseline.json but gone", self.run_main(str(tmp))[1])
            code, out = self.run_main(str(tmp), "--update", "--accept-regressions")
            self.assertEqual(code, 0, out)
            self.assertIn("recording worse ranks on purpose", out)
            self.assertEqual(json.loads((tmp / "routing" / "baseline.json").read_text())["cases"], {})

    def test_unknown_expected_skill_fails(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            self.make_repo(tmp)
            (tmp / "routing" / "cases.yaml").write_text("cases:\n  - id: r1\n    expected: retired-skill\n    request: x\n")
            code, out = self.run_main(str(tmp))
            self.assertEqual(code, 1)
            self.assertIn("'retired-skill' is not a skill or draft", out)

    def test_repo_cases_pass_the_rule(self):
        """The gate itself: the repo's routing set against its recorded baseline."""
        code, out = self.run_main(str(rc.ROOT))
        self.assertEqual(code, 0, out)


class ValidatorRoutingTest(unittest.TestCase):
    def test_check_routing(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "cases.yaml"
            path.write_text("cases:\n  - id: a\n    expected: build-evals\n    request: x\n"
                            "  - id: a\n    expected: none\n    request: y\n"
                            "  - id: b\n    expected: gone\n    request: z\n  - id: c\n    expected: none\n")
            problems = check_routing(path, {"build-evals"})
            self.assertEqual(len(problems), 3)
            self.assertEqual(check_routing(path, {"build-evals"}, {"build-evals", "model-selection"})[-1],
                             "routing/cases.yaml: no case expects model-selection: add one written against its closest neighbour")
            self.assertIn("a appears twice", problems[0])
            self.assertIn("b expects 'gone'", problems[1])
            self.assertIn("needs an id and a request", problems[2])
            path.write_text("cases: []\n")
            self.assertIn("non-empty", check_routing(path, set())[0])


if __name__ == "__main__":
    unittest.main()
