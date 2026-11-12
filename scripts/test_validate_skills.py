"""The skill template must pass the validator, and a broken copy must fail it."""
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import json  # noqa: E402

from validate_skills import cases_hash, check_evidence, check_skill, main, skill_hash  # noqa: E402
from validate_skills import overlapping_descriptions  # noqa: E402

TEMPLATE = Path(__file__).parent.parent / "templates" / "skill"


class ValidateSkillsTest(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        self.skill = self.root / "drafts" / "my-skill"
        shutil.copytree(TEMPLATE, self.skill)

    def tearDown(self):
        shutil.rmtree(self.root)

    def edit(self, old, new, file="SKILL.md"):
        path = self.skill / file
        path.write_text(path.read_text().replace(old, new, 1))

    def errors(self):
        return check_skill(self.skill, in_catalog=False)

    def assertError(self, fragment):
        self.assertTrue(any(fragment in e for e in self.errors()), f"no error containing {fragment!r}")

    def test_template_is_valid(self):
        (self.skill / "evals/results/run-1").mkdir(parents=True)  # written by claude plugin eval
        self.assertEqual(self.errors(), [])
        self.assertEqual(main(self.root), 0)

    def test_draft_status_rejected_in_catalog(self):
        self.assertIn("status 'draft' belongs in drafts/, not skills/", check_skill(self.skill, in_catalog=True))

    def test_legal_rules(self):
        self.edit('stage: "specify"', 'stage: "prove"')
        self.edit('legal: "false"', 'legal: "true"')
        (self.skill / "evals/my-skill-001/graders/judge.md").write_text("---\ntype: llm\n---\nCoherent.\n")
        self.assertError("eval_threshold >= 0.90")
        self.assertError("no judge")

    def test_overlapping_descriptions(self):
        same = "Build the eval set, graders and thresholds for an AI feature. Use for a release gate."
        self.assertEqual(len(overlapping_descriptions({"a": same, "b": same + " Also a review."})), 1)
        self.assertEqual(overlapping_descriptions({"a": same, "b": "Classify a use case under the EU AI Act."}), [])

    def test_old_stage_rejected(self):
        self.edit('stage: "specify"', 'stage: "govern"')
        self.assertError("stage 'govern' must be one of")

    def test_spec_frontmatter(self):
        self.edit("license: CC-BY-4.0", "license: CC-BY-4.0\nversion: 0.1.0")
        self.assertError("not in the Agent Skills spec")
        self.edit('eval_threshold: "0.80"', "eval_threshold: 0.80")
        self.assertError("metadata values must be quoted strings")

    def test_evidence_gate(self):
        skill = self.root / "skills" / "my-skill"
        shutil.move(self.skill, skill)
        self.assertIn("no baselines/my-skill.json", check_evidence(self.root, skill)[0])
        (self.root / "baselines").mkdir()
        record = {"skillHash": skill_hash(skill), "casesHash": cases_hash(skill), "failures": [],
                  "cases": {"my-skill-001": {"runs": 3}}}
        (self.root / "baselines/my-skill.json").write_text(json.dumps(record))
        self.assertEqual(check_evidence(self.root, skill), [])
        path = skill / "SKILL.md"
        path.write_text(path.read_text().replace('status: "draft"', 'status: "tested"'))  # metadata is not what the model reads
        self.assertEqual(check_evidence(self.root, skill), [])
        path.write_text(path.read_text() + "\nOne more rule.\n")
        self.assertIn("another text of the skill", check_evidence(self.root, skill)[0])
        (self.root / "baselines/my-skill.json").write_text(json.dumps({**record, "skillHash": skill_hash(skill), "failures": ["x: red line"]}))
        self.assertIn("the last recorded run fails", check_evidence(self.root, skill)[0])

    def test_unknown_source(self):
        self.edit('sources: "own-practice"', 'sources: "own-practice, cagan-inspired, made-up"')
        errors = check_skill(self.skill, in_catalog=False, known_sources={"cagan-inspired"})
        self.assertEqual(errors, ["sources ['made-up'] are not in foundations/sources.md (own-* ids are free)"])

    def test_skill_structure_errors(self):
        self.edit("## Links", "## See also")
        self.edit("name: my-skill", "name: other-skill")
        self.assertError("body headings")
        self.assertError("must be kebab-case and equal the folder name")
        self.assertError("case folder must start with 'other-skill-'")
        self.assertEqual(main(self.root), 1)

    def test_foundation_copies(self):
        (self.root / "foundations").mkdir()
        (self.root / "foundations/autonomy-ladder.md").write_text("# Ladder\n")
        self.assertEqual(main(self.root), 1)  # template cites references/autonomy-ladder.md, no copy yet
        self.assertEqual(main(self.root, sync=True), 0)
        self.edit("# Ladder", "# Edited locally", file="references/autonomy-ladder.md")
        self.edit("references/autonomy-ladder.md", "foundations/autonomy-ladder.md")
        errors = check_skill(self.skill, in_catalog=False, foundations=self.root / "foundations")
        self.assertTrue(any("not foundations/" in e for e in errors))
        self.assertTrue(any("differs from foundations/autonomy-ladder.md" in e for e in errors))  # stale copy still checked

    def test_case_errors(self):
        (self.skill / "evals/my-skill-002/graders/triggered.md").unlink()
        self.edit("tags: [my-skill,", "tags: [other,", file="evals/my-skill-001/prompt.md")
        shutil.rmtree(self.skill / "evals/my-skill-003")
        (self.skill / "templates").mkdir()
        (self.skill / "templates/prompt.md").write_text("stray")
        self.assertError("my-skill-002: needs a tool_used grader")
        self.assertError("my-skill-001: first tag must be the skill name")
        self.assertError("at least 3 case folders not tagged negative, found 2")
        self.assertError("templates/prompt.md: cases live in evals/<case>/prompt.md only")

    def test_red_lines(self):
        self.edit("weight: 5", "weight: 0.2", file="evals/my-skill-001/graders/redline-must-not-include.md")
        (self.skill / "evals/my-skill-003/graders/redline-must-not-include.md").rename(
            self.skill / "evals/my-skill-003/graders/must-not-include.md")
        self.assertError("red-line weight 0.2 must exceed 0.25")  # one other weight of 1 at threshold 0.8
        self.assertError("my-skill-003: a case tagged red-line needs a graders/redline-*.md grader")

    def test_fixtures_and_echo(self):
        self.edit("<An answer", "<Nothing useful", file="evals/my-skill-001/fixtures/good.md")
        self.edit("It contains replace-me-must-include.", "", file="evals/my-skill-001/fixtures/good.md")
        (self.skill / "evals/my-skill-002/fixtures/bad.md").write_text("It contains replace-me-must-include.\n")
        (self.skill / "evals/my-skill-003/fixtures/good.md").unlink()
        self.edit("<A scenario that", "replace-me-must-include <A scenario that", file="evals/my-skill-003/prompt.md")
        self.assertError("my-skill-001: fixtures/good.md fails ['must-include']: these graders reject a good answer")
        self.assertError("my-skill-002: fixtures/bad.md scores 1.00 >= 0.8: the graders let a bad answer pass")
        self.assertError("my-skill-002: fixtures/bad.md passes every red line")
        self.assertError("my-skill-003: missing fixtures/good.md")
        self.assertError("must-include.md: matches the prompt itself")

    def test_extra_fixtures(self):
        # real answers saved as good-*.md / bad-*.md follow the same rules as good.md / bad.md
        fixtures = self.skill / "evals/my-skill-001/fixtures"
        (fixtures / "good-run1.md").write_text("A sound answer that forgot the key words.\n")
        (fixtures / "bad-run2.md").write_text("It contains replace-me-must-include.\n")
        (fixtures / "notes-x.md").write_text("ignored: not a good- or bad- fixture\n")
        self.assertError("my-skill-001: fixtures/good-run1.md fails ['must-include']")
        self.assertError("my-skill-001: fixtures/bad-run2.md scores 1.00 >= 0.8")

    def test_triggering(self):
        self.edit("?my-skill\"'", "?my-skill.*\"'", file="evals/my-skill-001/graders/triggered.md")  # unanchored
        self.edit("min: 0\n", "", file="evals/my-skill-004/graders/not-triggered.md")  # min defaults to 1: never passes
        self.assertError("my-skill-001: needs a tool_used grader with tool: Skill")
        self.assertError("max: 0 needs min: 0")
        (self.skill / "evals/my-skill-002/graders/sibling.md").write_text(
            "---\ntype: tool_used\ntool: Skill\ninput_match: 'other-skill'\nmin: 0\nmax: 0\narm: both\n---\n")
        self.assertError("graders/sibling.md: a Skill grader needs input_match")
        shutil.rmtree(self.skill / "evals/my-skill-004")
        self.assertError("needs a case tagged negative")

    def test_harness_schema_and_js_regex(self):
        self.edit("weight: 5", "weight: 5\nname: must-not-include", file="evals/my-skill-001/graders/redline-must-not-include.md")
        self.edit("flags: i", "flag: i", file="evals/my-skill-002/graders/must-include.md")
        self.edit("max_turns: 10", "max_turn: 10", file="evals/my-skill-002/prompt.md")
        # Python re treats é as a word character, JavaScript does not: the harness would never match this.
        self.edit("pattern: 'replace-me-must-include'", "pattern: '\\bétude'", file="evals/my-skill-003/graders/must-include.md")
        (self.skill / "evals/my-skill-003/fixtures/good.md").write_text("Une étude est requise.\n")
        self.assertError("name 'must-not-include' must equal the file name 'redline-must-not-include'")
        self.assertError("unknown keys ['flag'] for type regex")
        self.assertError("my-skill-002/prompt.md: unknown frontmatter keys ['max_turn']")
        self.assertError("my-skill-003: fixtures/good.md fails ['must-include']")


if __name__ == "__main__":
    unittest.main()
