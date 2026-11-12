"""package_skills.py: one zip per catalog skill and a bundle, without evals, with the licence, byte-for-byte reproducible."""
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from package_skills import build  # noqa: E402


def write(path, text="x"):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


class PackageSkillsTest(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.root, ignore_errors=True)
        write(self.root / "LICENSE-CC-BY-4.0", "Attribution 4.0 International\n")
        for name, ver in (("alpha", "0.2.1"), ("beta", "1.0.0")):
            s = self.root / "skills" / name
            write(s / "SKILL.md", f'---\nname: {name}\nlicense: CC-BY-4.0\nmetadata:\n  stage: "evaluate"\n  version: "{ver}"\n---\nbody\n')
            write(s / "references/eval-statistics.md")
            write(s / "templates/out.md")
            write(s / "scripts/calc.py", "print(1)\n")
            write(s / "scripts/__pycache__/calc.cpython-312.pyc")
            write(s / "evals" / f"{name}-001/prompt.md")
            write(s / "evals/results/run.json")
            write(s / ".DS_Store")
        write(self.root / "drafts/gamma/SKILL.md", '---\nname: gamma\nmetadata:\n  version: "0.1.0"\n---\n')
        self.out = self.root / "dist"

    def names(self, path):
        with zipfile.ZipFile(path) as z:
            return z.namelist()

    def test_one_zip_per_skill_and_a_bundle(self):
        paths = build(self.root, self.out, "2026-11-12")
        self.assertEqual([p.name for p in paths], ["alpha-0.2.1.zip", "beta-1.0.0.zip", "ai-pm-skills-2026-11-12.zip"])
        self.assertEqual(self.names(self.out / "alpha-0.2.1.zip"), [
            "alpha/LICENSE", "alpha/SKILL.md", "alpha/references/eval-statistics.md",
            "alpha/scripts/calc.py", "alpha/templates/out.md"])
        bundle = self.names(self.out / "ai-pm-skills-2026-11-12.zip")
        self.assertEqual(len(bundle), 10)
        self.assertEqual(bundle, sorted(bundle))
        self.assertFalse(any("gamma" in n or "evals" in n or "pycache" in n for n in bundle))

    def test_licence_is_the_cc_by_text(self):
        build(self.root, self.out, "2026-11-12")
        with zipfile.ZipFile(self.out / "beta-1.0.0.zip") as z:
            self.assertEqual(z.read("beta/LICENSE"), b"Attribution 4.0 International\n")

    def test_byte_identical_across_builds(self):
        first = {p.name: p.read_bytes() for p in build(self.root, self.out, "2026-11-12")}
        for p in (self.root / "skills").rglob("*"):
            os.utime(p, (1_900_000_000, 1_900_000_000))  # new mtimes must not change the zips
        second = {p.name: p.read_bytes() for p in build(self.root, self.root / "dist2", "2026-11-12")}
        self.assertEqual(first, second)
        with zipfile.ZipFile(self.out / "alpha-0.2.1.zip") as z:
            self.assertEqual({i.date_time for i in z.infolist()}, {(1980, 1, 1, 0, 0, 0)})

    def test_zip_is_readable(self):
        build(self.root, self.out, "2026-11-12")
        with zipfile.ZipFile(self.out / "alpha-0.2.1.zip") as z:
            self.assertIsNone(z.testzip())
            self.assertEqual(z.read("alpha/scripts/calc.py"), b"print(1)\n")

    def test_sha256sums_verify_from_the_output_folder(self):
        paths = build(self.root, self.out, "2026-11-12")
        lines = (self.out / "SHA256SUMS").read_text().splitlines()
        self.assertEqual([line.split("  ", 1)[1] for line in lines], [p.name for p in paths])
        for line in lines:  # what `sha256sum -c SHA256SUMS` does, run from inside the folder of downloaded assets
            digest, name = line.split("  ", 1)
            self.assertNotIn("/", name)
            self.assertEqual(hashlib.sha256((self.out / name).read_bytes()).hexdigest(), digest)
        tool = shutil.which("sha256sum") or shutil.which("shasum")
        if tool:
            cmd = [tool, "-c", "SHA256SUMS"] if tool.endswith("sha256sum") else [tool, "-a", "256", "-c", "SHA256SUMS"]
            self.assertEqual(subprocess.run(cmd, cwd=self.out, capture_output=True).returncode, 0)

    def test_missing_version_fails(self):
        write(self.root / "skills/alpha/SKILL.md", "---\nname: alpha\n---\n")
        with self.assertRaises(SystemExit):
            build(self.root, self.out, "2026-11-12")


if __name__ == "__main__":
    unittest.main()
