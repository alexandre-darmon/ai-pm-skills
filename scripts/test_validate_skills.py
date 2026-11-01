"""The skill template must pass the validator, and a broken copy must fail it."""
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate_skills import check_skill, main  # noqa: E402

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

    def test_govern_rules(self):
        self.edit("stage: specify", "stage: govern")
        (self.skill / "evals/my-skill-001/graders/judge.md").write_text("---\ntype: llm\n---\nCoherent.\n")
        self.assertError("eval_threshold >= 0.90")
        self.assertError("no judge")

    def test_unknown_source(self):
        self.edit("sources: [own-practice]", "sources: [own-practice, cagan-inspired, made-up]")
        errors = check_skill(self.skill, in_catalog=False, known_sources={"cagan-inspired"})
        self.assertEqual(errors, ["sources ['made-up'] are not in foundations/sources.md (own-* ids are free)"])

    def test_skill_structure_errors(self):
        self.edit("## Links", "## See also")
        self.edit("name: my-skill", "name: other-skill")
        self.assertError("body headings")
        self.assertError("must be kebab-case and equal the folder name")
        self.assertError("case folder must start with 'other-skill-'")
        self.assertEqual(main(self.root), 1)

    def test_case_errors(self):
        (self.skill / "evals/my-skill-002/graders/triggered.md").unlink()
        self.edit("tags: [my-skill,", "tags: [other,", file="evals/my-skill-001/prompt.md")
        shutil.rmtree(self.skill / "evals/my-skill-003")
        (self.skill / "templates").mkdir()
        (self.skill / "templates/prompt.md").write_text("stray")
        self.assertError("my-skill-002: needs a tool_used grader")
        self.assertError("my-skill-001: first tag must be the skill name")
        self.assertError("at least 3 case folders, found 2")
        self.assertError("templates/prompt.md: cases live in evals/<case>/prompt.md only")


if __name__ == "__main__":
    unittest.main()
