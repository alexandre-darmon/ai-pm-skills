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

    def test_template_is_valid(self):
        self.assertEqual(check_skill(self.skill, in_catalog=False), [])
        self.assertEqual(main(self.root), 0)

    def test_draft_status_rejected_in_catalog(self):
        self.assertIn("status 'draft' belongs in drafts/, not skills/", check_skill(self.skill, in_catalog=True))

    def test_govern_rules(self):
        self.edit("stage: specify", "stage: govern")
        self.edit("graders: [checklist, exact]", "graders: [checklist, judge]")
        errors = check_skill(self.skill, in_catalog=False)
        self.assertTrue(any("threshold >= 0.90" in e for e in errors))
        self.assertTrue(any("no judge" in e for e in errors))

    def test_structure_errors(self):
        self.edit("## Links", "## See also")
        self.edit("name: my-skill", "name: other-skill")
        self.edit("id: my-skill-003", "id: my-skill-001", file="evals/cases.yaml")
        errors = check_skill(self.skill, in_catalog=False)
        self.assertTrue(any("body headings" in e for e in errors))
        self.assertTrue(any("must be kebab-case and equal the folder name" in e for e in errors))
        self.assertTrue(any("must start with 'other-skill-'" in e for e in errors))
        self.assertEqual(main(self.root), 1)


if __name__ == "__main__":
    unittest.main()
