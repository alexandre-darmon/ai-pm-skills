#!/usr/bin/env python3
"""Check the structure of every skill in skills/ and drafts/ against PRD §7.2 and §11.1.

Usage: python3 scripts/validate_skills.py [repo_root]
Exits 1 and prints one line per problem if anything is wrong.
"""
import datetime
import re
import sys
from pathlib import Path

import yaml

STAGES = {"strategy", "specify", "data", "build", "measure", "govern", "transform"}
STATUSES = {"draft", "tested", "verified-in-mission"}
GRADER_TYPES = {"regex", "tool_used", "tool_order", "file_exists", "llm", "baseline"}
JUDGE_TYPES = {"llm", "baseline"}
HEADINGS = ["When to use", "Inputs", "Method", "Output", "Rules and red lines", "Links", "Sources"]
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
MAX_SKILLS = 30
MAX_DESCRIPTION = 200
MAX_WORDS = 2000
MIN_CASES = 3


def read_frontmatter(path: Path) -> tuple[dict, str]:
    """Return (frontmatter, body) of a Markdown file. Raises ValueError if malformed."""
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if not text.startswith("---") or len(parts) < 3:
        raise ValueError("must start with a --- YAML frontmatter block")
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as e:
        raise ValueError(f"frontmatter is not valid YAML: {e}")
    if not isinstance(fm, dict):
        raise ValueError("frontmatter must be a mapping")
    return fm, parts[2]


def check_skill(folder: Path, in_catalog: bool) -> list[str]:
    errors = []
    err = errors.append
    skill_md = folder / "SKILL.md"
    if not skill_md.is_file():
        return ["missing SKILL.md"]
    try:
        fm, body = read_frontmatter(skill_md)
    except ValueError as e:
        return [f"SKILL.md {e}"]

    name = fm.get("name")
    if name != folder.name or not KEBAB.match(str(name)):
        err(f"name '{name}' must be kebab-case and equal the folder name '{folder.name}'")

    desc = fm.get("description")
    if not isinstance(desc, str) or not desc.strip():
        err("description is required")
    elif len(desc) > MAX_DESCRIPTION:
        err(f"description is {len(desc)} chars, max {MAX_DESCRIPTION}")

    stage = fm.get("stage")
    if stage not in STAGES:
        err(f"stage '{stage}' must be one of {sorted(STAGES)}")

    if not SEMVER.match(str(fm.get("version", ""))):
        err(f"version '{fm.get('version')}' must be semver (x.y.z)")

    if "last_verified" in fm and not isinstance(fm["last_verified"], datetime.date):
        err("last_verified must be a date (YYYY-MM-DD)")
    if stage == "govern" and "last_verified" not in fm:
        err("last_verified is mandatory for govern skills")

    for key in ("depends_on", "feeds"):
        value = fm.get(key)
        if not isinstance(value, list) or not all(isinstance(v, str) and KEBAB.match(v) for v in value):
            err(f"{key} must be a list of kebab-case skill names (can be empty)")
    sources = fm.get("sources")
    if not isinstance(sources, list) or not sources or not all(isinstance(s, str) for s in sources):
        err("sources must be a non-empty list of ids")

    if not isinstance(fm.get("autonomy_relevant"), bool):
        err("autonomy_relevant must be true or false")

    status = fm.get("status")
    if status not in STATUSES:
        err(f"status '{status}' must be one of {sorted(STATUSES)}")
    elif in_catalog and status == "draft":
        err("status 'draft' belongs in drafts/, not skills/")

    threshold = fm.get("eval_threshold")
    if isinstance(threshold, bool) or not isinstance(threshold, (int, float)) or not 0 < threshold <= 1:
        err("eval_threshold must be a number in (0, 1]")
    elif stage == "govern" and threshold < 0.9:
        err("govern skills need eval_threshold >= 0.90")

    found = re.findall(r"^## (.+?)\s*$", body, re.MULTILINE)
    if found != HEADINGS:
        err(f"body headings must be exactly {HEADINGS}, found {found}")
    words = len(body.split())
    if words > MAX_WORDS:
        err(f"body is {words} words, max {MAX_WORDS}; move material to references/")

    errors += check_cases(folder, str(name), govern=stage == "govern")
    return errors


def check_cases(folder: Path, name: str, govern: bool) -> list[str]:
    """Cases use the native `claude plugin eval` layout: evals/<case>/prompt.md + graders/*.md."""
    evals = folder / "evals"
    errors = []
    # claude plugin eval picks up any prompt.md / case.yaml below the target, so strays become cases.
    for stray in list(folder.rglob("prompt.md")) + list(folder.rglob("case.yaml")):
        rel = stray.relative_to(folder)
        if len(rel.parts) != 3 or rel.parts[0] != "evals" or rel.name != "prompt.md":
            errors.append(f"{rel}: cases live in evals/<case>/prompt.md only")

    # evals/results/ is where claude plugin eval writes its runs (git-ignored), not a case.
    cases = sorted(p for p in evals.glob("*") if p.is_dir() and p.name != "results") if evals.is_dir() else []
    if len(cases) < MIN_CASES:
        errors.append(f"evals/ must hold at least {MIN_CASES} case folders, found {len(cases)}")

    for case in cases:
        where = f"evals/{case.name}"
        if not case.name.startswith(f"{name}-"):
            errors.append(f"{where}: case folder must start with '{name}-'")
        prompt = case / "prompt.md"
        if not prompt.is_file():
            errors.append(f"{where}: missing prompt.md")
            continue
        try:
            fm, body = read_frontmatter(prompt)
        except ValueError as e:
            errors.append(f"{where}/prompt.md {e}")
            continue
        if fm.get("name", case.name) != case.name:
            errors.append(f"{where}: name must equal the folder name")
        tags = fm.get("tags")
        if not isinstance(tags, list) or not tags or tags[0] != name:
            errors.append(f"{where}: first tag must be the skill name '{name}'")
        for key in ("description", "expected_outcome"):
            if not str(fm.get(key) or "").strip():
                errors.append(f"{where}: {key} is required")
        if not body.strip():
            errors.append(f"{where}: prompt.md body (the scenario) is empty")
        errors += check_graders(case, where, govern)
    return errors


def check_graders(case: Path, where: str, govern: bool) -> list[str]:
    errors = []
    triggered = False
    for grader in sorted((case / "graders").glob("*.md")):
        gwhere = f"{where}/graders/{grader.name}"
        try:
            fm, _ = read_frontmatter(grader)
        except ValueError as e:
            errors.append(f"{gwhere} {e}")
            continue
        gtype = fm.get("type")
        if gtype not in GRADER_TYPES:
            errors.append(f"{gwhere}: type '{gtype}' must be one of {sorted(GRADER_TYPES)}")
        elif gtype == "regex" and not fm.get("pattern"):
            errors.append(f"{gwhere}: regex grader needs a pattern")
        elif gtype in JUDGE_TYPES and govern:
            errors.append(f"{gwhere}: govern skills use exact + checklist only, no judge")
        triggered |= gtype == "tool_used" and fm.get("tool") == "Skill"
    if not triggered:
        errors.append(f"{where}: needs a tool_used grader with tool: Skill (proves the skill fired)")
    return errors


def main(root: Path) -> int:
    problems = []
    catalog = sorted(p for p in (root / "skills").glob("*") if p.is_dir())
    drafts = sorted(p for p in (root / "drafts").glob("*") if p.is_dir())
    if len(catalog) > MAX_SKILLS:
        problems.append(f"skills/: {len(catalog)} skills, hard cap is {MAX_SKILLS}")
    for folder in catalog + drafts:
        for e in check_skill(folder, in_catalog=folder in catalog):
            problems.append(f"{folder.relative_to(root)}: {e}")

    for p in problems:
        print(p)
    print(f"{len(catalog)} skills, {len(drafts)} drafts, {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent.parent)))
