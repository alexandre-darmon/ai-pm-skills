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
GRADERS = {"exact", "checklist", "judge"}
HEADINGS = ["When to use", "Inputs", "Method", "Output", "Rules and red lines", "Links", "Sources"]
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
MAX_SKILLS = 30
MAX_DESCRIPTION = 200
MAX_WORDS = 2000
MIN_CASES = 3


def check_skill(folder: Path, in_catalog: bool) -> list[str]:
    errors = []
    err = errors.append
    skill_md = folder / "SKILL.md"
    if not skill_md.is_file():
        return ["missing SKILL.md"]

    text = skill_md.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if not text.startswith("---") or len(parts) < 3:
        return ["SKILL.md must start with a --- YAML frontmatter block"]
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as e:
        return [f"frontmatter is not valid YAML: {e}"]
    body = parts[2]

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

    evals = fm.get("evals")
    graders = []
    if not isinstance(evals, dict):
        err("evals must be an object with cases, graders, threshold")
    else:
        graders = evals.get("graders") or []
        if not isinstance(evals.get("cases"), int) or evals["cases"] < MIN_CASES:
            err(f"evals.cases must be an integer >= {MIN_CASES}")
        if not isinstance(graders, list) or not graders or not set(graders) <= GRADERS:
            err(f"evals.graders must be a non-empty subset of {sorted(GRADERS)}")
            graders = []
        threshold = evals.get("threshold")
        if not isinstance(threshold, (int, float)) or not 0 < threshold <= 1:
            err("evals.threshold must be a number in (0, 1]")
        elif stage == "govern" and threshold < 0.9:
            err("govern skills need evals.threshold >= 0.90")
        if stage == "govern" and "judge" in graders:
            err("govern skills use exact + checklist only, no judge")

    found = re.findall(r"^## (.+?)\s*$", body, re.MULTILINE)
    if found != HEADINGS:
        err(f"body headings must be exactly {HEADINGS}, found {found}")
    words = len(body.split())
    if words > MAX_WORDS:
        err(f"body is {words} words, max {MAX_WORDS}; move material to references/")

    errors += check_cases(folder, str(name), "judge" in graders)
    return errors


def check_cases(folder: Path, name: str, uses_judge: bool) -> list[str]:
    path = folder / "evals" / "cases.yaml"
    if not path.is_file():
        return ["missing evals/cases.yaml"]
    try:
        cases = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        return [f"evals/cases.yaml is not valid YAML: {e}"]
    if not isinstance(cases, list) or len(cases) < MIN_CASES:
        return [f"evals/cases.yaml must be a list of at least {MIN_CASES} cases"]

    errors = []
    seen = set()
    for i, case in enumerate(cases):
        where = f"evals/cases.yaml case #{i + 1}"
        if not isinstance(case, dict):
            errors.append(f"{where}: must be a mapping")
            continue
        cid = case.get("id")
        if not isinstance(cid, str) or not cid.startswith(f"{name}-"):
            errors.append(f"{where}: id '{cid}' must start with '{name}-'")
        elif cid in seen:
            errors.append(f"{where}: duplicate id '{cid}'")
        seen.add(cid)
        for key in ("title", "input"):
            if not isinstance(case.get(key), str) or not case[key].strip():
                errors.append(f"{where}: {key} is required")
        expected = case.get("expected")
        if not isinstance(expected, dict) or not str(expected.get("behaviour", "")).strip():
            errors.append(f"{where}: expected.behaviour is required")
        elif expected.get("rubric"):
            uses_judge = True

    if uses_judge and not (folder / "evals" / "rubric.md").is_file():
        errors.append("evals/rubric.md is required when the judge grader or a rubric is used")
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
