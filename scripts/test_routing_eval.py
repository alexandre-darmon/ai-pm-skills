import io
import json
import re
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

import routing_eval as re_
from run_evals import JUDGE, MODEL
from validate_skills import read_frontmatter

CASES = [{"id": "r1", "zone": "evals-release-model", "expected": "model-selection", "request": "Which model goes to production?"},
         {"id": "r2", "zone": "out-of-scope", "expected": "none", "request": "Draft an interview guide."}]


def trace(tmp: Path, name: str, skills: list[str]) -> str:
    path = tmp / f"{name}.jsonl"
    lines = [json.dumps({"type": "system"})]
    for s in skills:
        lines.append(json.dumps({"type": "assistant", "message": {"content": [
            {"type": "text", "text": "Skill"}, {"type": "tool_use", "name": "Skill", "input": {"skill": f"ai-pm-routing:{s}"}}]}}))
    lines.append(json.dumps({"type": "assistant", "message": {"content": [{"type": "tool_use", "name": "Read", "input": {"file_path": "x"}}]}}))
    path.write_text("\n".join(lines) + "\n")
    return str(path)


class CaseFilesTest(unittest.TestCase):
    def test_expected_skill_grader_is_anchored(self):
        files = re_.case_files(CASES[0], runs=3, max_turns=10)
        with tempfile.TemporaryDirectory() as d:
            for rel, text in files.items():
                (Path(d) / rel).parent.mkdir(parents=True, exist_ok=True)
                (Path(d) / rel).write_text(text)
            fm, body = read_frontmatter(Path(d) / "prompt.md")
            g, _ = read_frontmatter(Path(d) / "graders" / "routes.md")
        self.assertEqual((fm["name"], fm["runs"], fm["max_turns"]), ("r1", 3, 10))
        self.assertEqual(fm["allowed_tools"], ["Read", "Glob", "Grep", "Skill"])
        self.assertEqual(body.strip(), CASES[0]["request"])
        self.assertEqual((g["type"], g["tool"], g["min"]), ("tool_used", "Skill", 1))
        pattern = g["input_match"]
        self.assertTrue(re.search(pattern, '{"skill":"ai-pm-routing:model-selection"}'))
        self.assertFalse(re.search(pattern, '{"skill":"ai-pm-routing:build-evals"}'))
        self.assertFalse(re.search(pattern, '{"skill":"ai-pm-routing:model-selection-v2"}'))

    def test_none_case_forbids_any_skill(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "routes.md"
            path.write_text(re_.case_files(CASES[1], 1, 10)["graders/routes.md"])
            g, _ = read_frontmatter(path)
        self.assertEqual((g["min"], g["max"]), (0, 0))
        self.assertTrue(re.search(g["input_match"], '{"skill":"build-evals"}'))


class TraceTest(unittest.TestCase):
    def test_skill_calls_in_order_without_prefix(self):
        with tempfile.TemporaryDirectory() as d:
            path = trace(Path(d), "t", ["build-evals", "model-selection"])
            Path(path).write_text(Path(path).read_text() + "not json \"Skill\"\n")
            self.assertEqual(re_.skill_calls(path), ["build-evals", "model-selection"])
        self.assertEqual(re_.skill_calls(None), [])
        self.assertEqual(re_.skill_calls("/no/such/trace.jsonl"), [])

    def test_summarise_accuracy_and_confusion(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            ok = {"graders": [{"name": "routes", "passed": True}]}
            ko = {"graders": [{"name": "routes", "passed": False}]}
            result = {"startedAt": "2026-11-12T10:00:00Z", "cases": [
                {"name": "r1", "arms": {"with": [
                    {**ok, "tracePath": trace(tmp, "a", ["model-selection"])},
                    {**ok, "tracePath": trace(tmp, "b", ["build-evals", "model-selection"])},  # right skill, second try
                    {**ko, "tracePath": trace(tmp, "c", ["build-evals"])}]}},
                {"name": "r2", "arms": {"with": [
                    {**ok, "tracePath": trace(tmp, "d", [])},
                    {**ko, "error": "timeout", "tracePath": None}]}},
                {"name": "unknown", "arms": {"with": [ok]}}]}
            s = re_.summarise(result, CASES)
        self.assertEqual(s["runs"], 5)
        self.assertAlmostEqual(s["accuracy"], 3 / 5)
        self.assertAlmostEqual(s["firstAccuracy"], 2 / 5)
        self.assertEqual(s["confusion"], [{"expected": "model-selection", "loaded": "build-evals", "count": 2}])
        self.assertEqual(s["zones"]["out-of-scope"], {"correct": 1, "runs": 2})
        self.assertEqual(s["cases"][1]["errors"], 1)
        md = re_.markdown(s)
        self.assertIn("| r1 | model-selection | 2/3 | model-selection, build-evals, build-evals |", md)
        self.assertIn("- model-selection → build-evals (2)", md)


class LostTraceTest(unittest.TestCase):
    """The traces live in temporary folders: --summarise must not read a cleaned-up trace as 'no skill loaded'."""

    def result(self, tmp: Path) -> dict:
        ok = {"graders": [{"name": "routes", "passed": True}]}
        return {"startedAt": "2026-11-12", "cases": [{"name": "r1", "arms": {"with": [
            {**ok, "tracePath": trace(tmp, "a", ["model-selection"])},
            {**ok, "error": "timeout", "tracePath": None}]}}]}

    def test_extract_calls_flags_lost_traces_only(self):
        with tempfile.TemporaryDirectory() as d:
            result = self.result(Path(d))
            calls, missing = re_.extract_calls(result)
            self.assertEqual((calls, missing), ({"r1": [["model-selection"], None]}, []))
            Path(result["cases"][0]["arms"]["with"][0]["tracePath"]).unlink()
            calls, missing = re_.extract_calls(result)
            self.assertEqual(calls, {"r1": [None, None]})
            self.assertEqual(len(missing), 1)
            self.assertIn("r1 run 1", missing[0])
            s = re_.summarise(result, CASES, calls)
            self.assertEqual(s["cases"][0]["calls"][0]["first"], re_.UNKNOWN)  # not "none"
            self.assertEqual(s["confusion"], [{"expected": "model-selection", "loaded": re_.UNKNOWN, "count": 1}])

    def test_summarise_uses_saved_calls_and_stops_on_lost_traces(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d)
            result = self.result(out)
            (out / "raw.json").write_text(json.dumps(result))
            (out / "cases.yaml").write_text(json.dumps({"cases": CASES}))  # JSON is YAML
            args = ["--summarise", "--out", d, "--cases", str(out / "cases.yaml")]
            Path(result["cases"][0]["arms"]["with"][0]["tracePath"]).unlink()
            err = io.StringIO()
            with redirect_stdout(io.StringIO()), redirect_stderr(err):
                self.assertEqual(re_.main(args), 1)
            self.assertIn("trace(s) are gone", err.getvalue())
            self.assertFalse((out / "summary.json").exists())
            (out / "calls.json").write_text(json.dumps({"r1": [["model-selection"], None]}))  # saved right after the run
            with redirect_stdout(io.StringIO()):
                self.assertEqual(re_.main(args), 0)
            s = json.loads((out / "summary.json").read_text())
            self.assertEqual((s["firstAccuracy"], s["confusion"]), (0.5, []))


class DryRunTest(unittest.TestCase):
    def test_dry_run_builds_the_plugin_and_prints_the_command(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d)
            buf = io.StringIO()
            with redirect_stdout(buf):
                code = re_.main(["--dry-run", "--runs", "2", "--out", str(out)])
            self.assertEqual(code, 0)
            plugin = out / "plugin"
            manifest = json.loads((plugin / ".claude-plugin" / "plugin.json").read_text())
            self.assertEqual(manifest["name"], re_.PLUGIN)
            skills = {p.name for p in (plugin / "skills").iterdir()}
            self.assertEqual(skills, {p.name for p in re_.skill_folders(re_.ROOT)})
            self.assertIn("ai-incident-playbook", skills)  # drafts are installed too
            self.assertEqual(list((plugin / "skills").rglob("evals")), [])  # no skill brings its own cases
            self.assertTrue((plugin / "skills" / "build-evals" / "SKILL.md").is_file())
            cases = sorted(p.name for p in (plugin / "evals").iterdir())
            self.assertEqual(len(cases), len(re_.load_cases(re_.ROOT / "routing" / "cases.yaml")))
            text = buf.getvalue()
            cmd = next(line for line in text.splitlines() if line.startswith("$ "))
            for flag in ("claude plugin eval", str(plugin), "--ablation none", f"--model {MODEL}", f"--judge-model {JUDGE}",
                         "--runs 2", "--trust-plugin", "--no-publish", f"--json {out / 'raw.json'}"):
                self.assertIn(flag, cmd)
            self.assertFalse((out / "raw.json").exists())  # nothing ran

    def test_case_filter_and_cost_ceiling(self):
        cmd = re_.command(Path("p"), Path("raw.json"), 3, 7.5, 2, "route-00*")
        self.assertEqual(cmd[cmd.index("--max-cost-usd") + 1], "7.5")
        self.assertEqual(cmd[-2:], ["--case", "route-00*"])
        self.assertEqual(cmd[cmd.index("-j") + 1], "2")

    def test_summarise_needs_a_raw_result(self):
        with tempfile.TemporaryDirectory() as d:
            with redirect_stdout(io.StringIO()):
                self.assertEqual(re_.main(["--summarise", "--out", d]), 1)


if __name__ == "__main__":
    unittest.main()
