#!/usr/bin/env python3
"""Check the structure of every skill in skills/ and drafts/ against PRD §7.2 and §11.1.

Usage: python3 scripts/validate_skills.py [--sync] [--no-evidence] [repo_root]
Exits 1 and prints one line per problem if anything is wrong.
--sync first rewrites each skill's references/ copies of the foundations/ files it cites.
Evidence (skip with --no-evidence while editing): every skill in skills/ needs baselines/<skill>.json from a recorded
run (3 runs per case or more) on its current text and cases, and that run must pass. The README shows those numbers.

Free checks on the eval cases (foundations/eval-conventions.md, "Free checks"):
- red lines: graders/redline-*.md must weigh enough to fail the case on their own;
- fixtures: evals/<case>/fixtures/good.md must pass every regex grader, bad.md must fail the case;
- echo: a must-include regex that matches the prompt itself proves nothing;
- triggering: input_match is anchored on the skill name, and one case tagged negative checks the skill stays silent.
"""
import datetime
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

STAGES = {"specify", "build", "evaluate", "prove"}  # what correct means, build to learn, measure it offline and online, prove it
# Agent Skills spec: only these keys at the top level (claude.ai, the Skills API and skills-ref reject any other).
TOP_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
# The repo's own keys live under metadata:, as strings (the spec maps string keys to string values).
META_KEYS = {"stage", "version", "status", "eval_threshold", "legal", "last_verified", "autonomy_relevant", "depends_on", "feeds", "sources"}
LIST_KEYS = {"depends_on", "feeds", "sources"}
BOOL_KEYS = {"legal", "autonomy_relevant"}
STATUSES = {"draft", "tested", "verified-in-mission"}
# Keys the harness accepts per grader type (claude plugin eval 2.1.302, strict schema: anything else fails the load).
GRADER_KEYS = {
    "regex": {"target", "pattern", "flags", "match", "weight", "arm"},
    "tool_used": {"tool", "input_match", "min", "max", "weight", "arm"},
    "tool_order": {"before", "after", "weight", "arm"},
    "file_exists": {"path", "exists", "weight", "arm"},
    "llm": {"criteria", "focus", "weight", "arm"},
    "baseline": {"baseline_file", "criteria", "weight", "arm"},
}
GRADER_TYPES = set(GRADER_KEYS)
PROMPT_KEYS = {"schema_version", "name", "description", "tags", "plugins", "runs", "expected_outcome", "model", "max_turns",
               "timeout_seconds", "allowed_tools", "disallowed_tools", "artifact_publish", "growthbook_overrides",
               "append_system_prompt", "env"}
JUDGE_TYPES = {"llm", "baseline"}
HEADINGS = ["When to use", "Inputs", "Method", "Output", "Rules and red lines", "Links", "Sources"]
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
MAX_SKILLS = 30
MAX_DESCRIPTION = 200
MAX_WORDS = 2000
MIN_CASES = 3
RECORD_RUNS = 3  # runs per case that make a recorded run: it replaces baselines/<skill>.json, pass or fail
REDLINE = "redline-"
# The Skill tool input reaches input_match as JSON, e.g. {"skill":"llm-feature-prd:llm-feature-prd"}.
# Anchoring on the whole name stops a sibling such as llm-feature-prd-lite from counting as this skill.
TRIGGER = r'"skill"\s*:\s*"(?:[\w-]+:)?{name}"'
# A skill installed alone has no foundations/ folder, so it cites a synced copy in its own references/.
COPY_HEADER = "<!-- Synced copy of foundations/{name}. Edit the original, then run: python3 scripts/validate_skills.py --sync -->\n"


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


def skill_meta(fm: dict) -> tuple[dict, list[str]]:
    """Typed view of a SKILL.md frontmatter: top-level keys plus the metadata: strings parsed (lists, booleans, number, date).

    A value that does not parse is kept as the raw string, so the field checks in check_skill report it.
    """
    errors = []
    unknown = sorted(set(fm) - TOP_KEYS)
    if unknown:
        errors.append(f"top-level keys {unknown} are not in the Agent Skills spec; move them under metadata:")
    meta = fm.get("metadata")
    if not isinstance(meta, dict):
        return dict(fm), errors + ["metadata: must be a mapping holding stage, version, status, eval_threshold, sources..."]
    not_str = sorted(k for k, v in meta.items() if not isinstance(v, str))
    if not_str:
        errors.append(f"metadata values must be quoted strings (Agent Skills spec): {not_str}")
    extra = sorted(set(meta) - META_KEYS)
    if extra:
        errors.append(f"metadata keys {extra} are unknown; allowed: {sorted(META_KEYS)}")
    out = {k: v for k, v in fm.items() if k != "metadata"}
    for key, raw in meta.items():
        value = raw
        if isinstance(raw, str):
            if key in LIST_KEYS:
                value = [x.strip() for x in raw.split(",") if x.strip()]
            elif key in BOOL_KEYS and raw in ("true", "false"):
                value = raw == "true"
            elif key == "eval_threshold":
                try:
                    value = float(raw)
                except ValueError:
                    pass
            elif key == "last_verified":
                try:
                    value = datetime.date.fromisoformat(raw)
                except ValueError:
                    pass
        out[key] = value
    return out, errors


def read_skill(path: Path) -> tuple[dict, str]:
    """(typed frontmatter, body) of a SKILL.md, the metadata: keys flattened. Raises ValueError if malformed."""
    fm, body = read_frontmatter(path)
    return skill_meta(fm)[0], body


def cases_hash(folder: Path) -> str:
    """Fingerprint of the cases and graders: a change means stored scores are stale."""
    h = hashlib.sha256()
    evals = folder / "evals"
    # results/ is output and fixtures/ is only read by the validator: neither changes a run.
    for f in sorted(p for p in evals.rglob("*") if p.is_file() and not {"results", "fixtures"} & set(p.relative_to(evals).parts)):
        h.update(str(f.relative_to(evals)).encode() + b"\0" + f.read_bytes())
    return h.hexdigest()


def skill_hash(folder: Path) -> str:
    """Fingerprint of what the agent reads: SKILL.md name, description and body, then references/, templates/, scripts/.

    metadata: (stage, status, version) is left out: promoting a skill or moving it to another block does not change
    what the model reads, so it does not make a recorded run stale. Neither does the folder (drafts/ or skills/).
    """
    h = hashlib.sha256()
    fm, body = read_frontmatter(folder / "SKILL.md")
    h.update(f"{fm.get('name')}\0{fm.get('description')}\0{body}".encode())
    for f in sorted(p for p in folder.rglob("*") if p.is_file() and p.name != "SKILL.md" and p.suffix != ".pyc"
                    and not {"evals", "__pycache__"} & set(p.relative_to(folder).parts)):
        h.update(str(f.relative_to(folder)).encode() + b"\0" + f.read_bytes())
    return h.hexdigest()


def check_evidence(root: Path, folder: Path) -> list[str]:
    """A catalog skill is shown with the numbers of its last recorded run: that run must be on today's text and cases, and pass."""
    path = root / "baselines" / f"{folder.name}.json"
    fix = f"python3 scripts/run_evals.py --full --runs {RECORD_RUNS} {folder.relative_to(root)}"
    if not path.is_file():
        return [f"no baselines/{folder.name}.json: a catalog skill needs a recorded run ({fix})"]
    b = json.loads(path.read_text(encoding="utf-8"))
    errors = []
    if b.get("skillHash") != skill_hash(folder):
        errors.append(f"baselines/{folder.name}.json was recorded on another text of the skill (SKILL.md body, description, "
                      f"references, templates or scripts): rerun it ({fix}) or move the skill back to drafts/")
    if b.get("casesHash") != cases_hash(folder):
        errors.append(f"baselines/{folder.name}.json was recorded on other cases or graders: a grader-only change is regraded "
                      f"for free (run_evals.py --regrade --out <dir of that run>), a new or changed prompt needs {fix}")
    if errors:
        pass  # a stale run's verdict says nothing about today's skill
    elif "failures" not in b:
        errors.append(f"baselines/{folder.name}.json has no recorded verdict: rerun it ({fix})")
    elif b["failures"]:
        errors.append(f"the last recorded run fails ({'; '.join(b['failures'][:3])}): fix the skill and rerun, or move it back to drafts/")
    short = sorted(n for n, c in b.get("cases", {}).items() if c.get("runs", 0) < RECORD_RUNS)
    if short:
        errors.append(f"baselines/{folder.name}.json: cases {short} ran fewer than {RECORD_RUNS} times with the skill")
    return errors


def load_sources(root: Path) -> set[str] | None:
    """Ids from the first column of foundations/sources.md tables, or None if the file is absent."""
    path = root / "foundations" / "sources.md"
    if not path.is_file():
        return None
    return set(re.findall(r"^\| ([a-z][a-z0-9-]*) \|", path.read_text(encoding="utf-8"), re.MULTILINE))


def foundation_copies(folder: Path, foundations: Path) -> dict[str, str]:
    """Expected content of each references/<file> that mirrors foundations/<file>: the ones SKILL.md cites, plus existing ones."""
    cited = re.findall(r"references/([a-z0-9-]+\.md)", (folder / "SKILL.md").read_text(encoding="utf-8"))
    present = [p.name for p in (folder / "references").glob("*.md")]
    return {
        name: COPY_HEADER.format(name=name) + (foundations / name).read_text(encoding="utf-8")
        for name in set(cited + present)
        if (foundations / name).is_file()
    }


def sync_foundations(folder: Path, foundations: Path) -> None:
    for name, expected in foundation_copies(folder, foundations).items():
        (folder / "references").mkdir(exist_ok=True)
        (folder / "references" / name).write_text(expected, encoding="utf-8")


def check_foundations(folder: Path, body: str, foundations: Path) -> list[str]:
    errors = []
    if "foundations/" in body:
        errors.append("cite references/<file>.md, not foundations/: a skill installed alone has no foundations/ folder")
    for name, expected in sorted(foundation_copies(folder, foundations).items()):
        copy = folder / "references" / name
        if not copy.is_file() or copy.read_text(encoding="utf-8") != expected:
            errors.append(f"references/{name} is missing or differs from foundations/{name}; run python3 scripts/validate_skills.py --sync")
    return errors


def check_skill(folder: Path, in_catalog: bool, known_sources: set[str] | None = None, foundations: Path | None = None) -> list[str]:
    errors = []
    err = errors.append
    skill_md = folder / "SKILL.md"
    if not skill_md.is_file():
        return ["missing SKILL.md"]
    try:
        fm, body = read_frontmatter(skill_md)
    except ValueError as e:
        return [f"SKILL.md {e}"]
    fm, meta_errors = skill_meta(fm)
    errors += meta_errors

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
    legal = fm.get("legal", False)
    if not isinstance(legal, bool):
        err("legal must be true or false (optional, default false)")
        legal = False
    if legal and "last_verified" not in fm:
        err("last_verified is mandatory for legal skills")

    for key in ("depends_on", "feeds"):
        value = fm.get(key)
        if not isinstance(value, list) or not all(isinstance(v, str) and KEBAB.match(v) for v in value):
            err(f"{key} must be comma-separated kebab-case skill names (can be empty)")
    sources = fm.get("sources")
    if not isinstance(sources, list) or not sources or not all(isinstance(s, str) for s in sources):
        err("sources must be comma-separated ids, at least one")
    elif known_sources is not None:
        unknown = [s for s in sources if s not in known_sources and not s.startswith("own-")]
        if unknown:
            err(f"sources {unknown} are not in foundations/sources.md (own-* ids are free)")

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
    elif legal and threshold < 0.9:
        err("legal skills need eval_threshold >= 0.90")

    found = re.findall(r"^## (.+?)\s*$", body, re.MULTILINE)
    if found != HEADINGS:
        err(f"body headings must be exactly {HEADINGS}, found {found}")
    words = len(body.split())
    if words > MAX_WORDS:
        err(f"body is {words} words, max {MAX_WORDS}; move material to references/")

    if foundations is not None:
        errors += check_foundations(folder, body, foundations)
    valid_threshold = threshold if not any(e.startswith("eval_threshold") for e in errors) else None
    errors += check_cases(folder, str(name), legal=legal, threshold=valid_threshold)
    return errors


def check_cases(folder: Path, name: str, legal: bool, threshold: float | None = None) -> list[str]:
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
    negatives = 0
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
        unknown = sorted(set(fm) - PROMPT_KEYS)
        if unknown:
            errors.append(f"{where}/prompt.md: unknown frontmatter keys {unknown}; the harness would not load the case")
        tags = fm.get("tags")
        if not isinstance(tags, list) or not tags or tags[0] != name:
            errors.append(f"{where}: first tag must be the skill name '{name}'")
        for key in ("description", "expected_outcome"):
            if not str(fm.get(key) or "").strip():
                errors.append(f"{where}: {key} is required")
        if not body.strip():
            errors.append(f"{where}: prompt.md body (the scenario) is empty")
        tags = tags if isinstance(tags, list) else []
        negatives += "negative" in tags
        errors += check_graders(case, where, name, legal, tags, body, threshold)
    if len(cases) - negatives < MIN_CASES:
        errors.append(f"evals/ must hold at least {MIN_CASES} case folders not tagged negative, found {len(cases) - negatives}")
    if cases and not negatives:
        errors.append("evals/ needs a case tagged negative: a near-miss request, taken from a 'Do not use' bullet, where this skill must stay silent")
    return errors


def skill_check(fm: dict) -> str | None:
    """'fires' for a grader proving the skill was called, 'silent' for one proving it was not (max: 0)."""
    if fm.get("type") != "tool_used" or fm.get("tool") != "Skill":
        return None
    return "silent" if fm.get("max") == 0 else "fires"


# The harness runs regex graders as JavaScript RegExp; Python's re differs on Unicode \b, flags and syntax.
JS_REGEX = """const [pats, texts] = JSON.parse(require('fs').readFileSync(0, 'utf8'));
console.log(JSON.stringify(pats.map(([p, f]) => { try {
  const one = new RegExp(p, f), all = new RegExp(p, f.includes('g') ? f : f + 'g');
  return texts.map(t => [one.test(t), [...t.matchAll(all)].length]);
} catch (e) { return String(e.message); } })));"""


def run_js_regex(patterns: list[tuple[str, str]], texts: list[str]) -> list:
    """For each (pattern, flags): [[matches, count] per text], or the error message if JS cannot compile it."""
    node = shutil.which("node")
    if not node:
        sys.exit("validate_skills.py needs node: regex graders are checked with JavaScript RegExp, as the harness runs them")
    out = subprocess.run([node, "-e", JS_REGEX], input=json.dumps([patterns, texts]), capture_output=True, text=True, check=True)
    return json.loads(out.stdout)


def regex_passes(fm: dict, matched: bool, count: int) -> bool:
    match = str(fm.get("match", "contains"))
    return count == int(match[6:]) if match.startswith("count:") else matched == (match == "contains")


def check_grader_schema(fm: dict, stem: str, gwhere: str) -> list[str]:
    errors = []
    gtype = fm.get("type")
    if gtype not in GRADER_KEYS:
        return [f"{gwhere}: type '{gtype}' must be one of {sorted(GRADER_KEYS)}"]
    unknown = sorted(set(fm) - GRADER_KEYS[gtype] - {"type", "name"})
    if unknown:
        errors.append(f"{gwhere}: unknown keys {unknown} for type {gtype}; the harness would not load the case")
    if fm.get("name", stem) != stem:  # the harness reports a grader under this name; the red-line rule reads the file name
        errors.append(f"{gwhere}: name '{fm['name']}' must equal the file name '{stem}' (or be left out)")
    weight = fm.get("weight", 1)
    if isinstance(weight, bool) or not isinstance(weight, (int, float)) or weight <= 0:
        errors.append(f"{gwhere}: weight must be a positive number")
    if fm.get("arm", "both") not in ("both", "with-only"):
        errors.append(f"{gwhere}: arm must be both or with-only")
    for key in ("min", "max"):
        if key in fm and (isinstance(fm[key], bool) or not isinstance(fm[key], int) or fm[key] < 0):
            errors.append(f"{gwhere}: {key} must be a whole number >= 0")
    if gtype == "regex":
        if not isinstance(fm.get("pattern"), str) or not fm["pattern"]:
            errors.append(f"{gwhere}: regex grader needs a pattern (a quoted string, or the file body)")
        if not re.fullmatch(r"contains|not_contains|count:\d+", str(fm.get("match", "contains"))):
            errors.append(f"{gwhere}: match must be contains, not_contains or count:N")
        if not re.fullmatch(r"[dgimsuvy]*", str(fm.get("flags", ""))):
            errors.append(f"{gwhere}: flags must be JavaScript RegExp flags (d g i m s u v y)")
    return errors


def check_graders(case: Path, where: str, skill: str, legal: bool, tags: list | None = None,
                  prompt: str = "", threshold: float | None = None) -> list[str]:
    errors = []
    tags = tags or []
    graders: dict[str, dict] = {}
    for grader in sorted((case / "graders").glob("*.md")):
        gwhere = f"{where}/graders/{grader.name}"
        try:
            fm, body = read_frontmatter(grader)
        except ValueError as e:
            errors.append(f"{gwhere} {e}")
            continue
        if body.strip():  # the harness reads the body as the pattern or the criteria when the key is absent
            fm.setdefault({"regex": "pattern", "llm": "criteria", "baseline": "criteria"}.get(fm.get("type"), "_body"), body.strip())
            fm.pop("_body", None)
        schema = check_grader_schema(fm, grader.stem, gwhere)
        errors += schema
        if fm.get("type") in JUDGE_TYPES and legal:
            errors.append(f"{gwhere}: legal skills use exact + checklist only, no judge")
        if not schema:
            graders[grader.stem] = fm

    expected = TRIGGER.format(name=skill)
    fires, silent = [], []
    for g, fm in graders.items():
        kind = skill_check(fm)
        if kind and fm.get("input_match") != expected:
            errors.append(f"{where}/graders/{g}.md: a Skill grader needs input_match: '{expected}' (this skill, anchored)")
        elif kind == "silent" and (fm.get("min") != 0 or fm.get("arm") != "both"):
            errors.append(f"{where}/graders/{g}.md: max: 0 needs min: 0 (the default min is 1, so it could never pass) and arm: both")
        elif kind:
            (fires if kind == "fires" else silent).append(g)
    if "negative" in tags:
        if len(silent) != 1 or len(graders) != 1:
            errors.append(f"{where}: a negative case has one grader only: type: tool_used, tool: Skill, input_match: '{expected}', "
                          "min: 0, max: 0, arm: both (proves this skill stayed silent)")
        return errors
    if silent:
        errors.append(f"{where}: max: 0 on this skill belongs in a case tagged negative")
    if not fires:
        errors.append(f"{where}: needs a tool_used grader with tool: Skill and input_match: '{expected}' (proves this skill fired)")

    redlines = [g for g in graders if g.startswith(REDLINE)]
    for g in [g for g in redlines if skill_check(graders[g])]:
        errors.append(f"{where}/graders/{g}.md: a red line checks the answer, not whether the skill fired")
        redlines.remove(g)
    if "red-line" in tags and not redlines:
        errors.append(f"{where}: a case tagged red-line needs a graders/{REDLINE}*.md grader")

    regex = {g: fm for g, fm in graders.items() if fm.get("type") == "regex"}
    # good.md and bad.md are required; good-*.md and bad-*.md (e.g. real answers from paid runs) follow the same rules
    fixtures = [(k, case / "fixtures" / f"{k}.md") for k in ("good", "bad")]
    fixtures += [(p.stem.split("-")[0], p) for p in sorted((case / "fixtures").glob("*-*.md")) if p.stem.split("-")[0] in ("good", "bad")]
    texts = [prompt] + [p.read_text(encoding="utf-8") if p.is_file() else "" for _, p in fixtures]
    results = dict(zip(regex, run_js_regex([(fm["pattern"], str(fm.get("flags", ""))) for fm in regex.values()], texts))) if regex else {}
    for g, res in list(results.items()):
        if isinstance(res, str):
            errors.append(f"{where}/graders/{g}.md: pattern is not a valid JavaScript RegExp: {res}")
            del results[g]
        elif (regex[g].get("match", "contains") == "contains" and regex[g].get("target", "last_message") == "last_message"
              and res[0][0]):
            errors.append(f"{where}/graders/{g}.md: matches the prompt itself, so an answer that repeats the brief passes; match what the skill adds")
    if threshold is None or not results:
        return errors

    scored = {g: fm.get("weight", 1) for g, fm in graders.items() if skill_check(fm) != "fires"}
    for g in redlines:
        others = sum(scored.values()) - scored[g]
        floor = others * (1 - threshold) / threshold
        if scored[g] <= floor:
            errors.append(f"{where}/graders/{g}.md: red-line weight {scored[g]} must exceed {floor:.2f} "
                          f"(other weights {others}, threshold {threshold}), or one miss would not fail the case")

    # Grader unit tests: a hand-written good answer must pass every regex grader, a bad one must fail the case.
    # Graders that cannot run offline (llm, file, tool) count as passed in both.
    for i, (kind, path) in enumerate(fixtures, start=1):
        if not path.is_file():
            what = "an answer that passes every grader" if kind == "good" else "an answer that crosses the red line"
            errors.append(f"{where}: missing fixtures/{kind}.md ({what})")
            continue
        failed = [g for g, res in results.items() if not regex_passes(regex[g], *res[i])]
        score = 1 - sum(scored[g] for g in failed) / sum(scored.values())
        if kind == "good" and failed:  # every grader, not just the threshold: a too-narrow grader is what this catches
            errors.append(f"{where}: fixtures/{path.name} fails {failed}: these graders reject a good answer")
        regex_redlines = [g for g in redlines if g in results]
        if kind == "bad" and score >= threshold:
            errors.append(f"{where}: fixtures/{path.name} scores {score:.2f} >= {threshold}: the graders let a bad answer pass")
        if kind == "bad" and regex_redlines and not set(regex_redlines) & set(failed):
            errors.append(f"{where}: fixtures/{path.name} passes every red line {regex_redlines}: write it to cross one")
    return errors


# Two skills whose descriptions share too many words compete for the same request.
MAX_OVERLAP = 0.30
OVERLAP_STOP = set("a an the and or of to for in on with by is are it its as at be use when if from that this what which who how do does not your our their ai llm feature skill".split())


def description_words(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z][a-z0-9-]+", text.lower()) if w not in OVERLAP_STOP and len(w) > 2}


def overlapping_descriptions(descriptions: dict[str, str]) -> list[str]:
    """Pairs of skills whose descriptions share more than MAX_OVERLAP of their words (Jaccard)."""
    words = {name: description_words(d) for name, d in descriptions.items()}
    names, problems = sorted(words), []
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            union = words[a] | words[b]
            score = len(words[a] & words[b]) / len(union) if union else 0
            if score > MAX_OVERLAP:
                problems.append(f"{a} and {b}: descriptions share {score:.0%} of their words, so they compete for the same requests; "
                                f"give each a distinct trigger")
    return problems


def check_routing(path: Path, names: set[str], catalog: set[str] = frozenset()) -> list[str]:
    """routing/cases.yaml (scripts/routing_check.py): ids unique, each expected skill a skills/ or drafts/ folder, or none,
    and every catalog skill expected by at least one case (else the routing set cannot see it under- or over-fire)."""
    try:
        cases = (yaml.safe_load(path.read_text(encoding="utf-8")) or {}).get("cases")
    except yaml.YAMLError as e:
        return [f"routing/cases.yaml: not valid YAML: {e}"]
    if not isinstance(cases, list) or not cases:
        return ["routing/cases.yaml: needs a non-empty cases: list"]
    problems, seen = [], set()
    for c in cases:
        cid = c.get("id") if isinstance(c, dict) else None
        if not cid or not isinstance(c.get("request"), str) or not c["request"].strip():
            problems.append(f"routing/cases.yaml: every case needs an id and a request ({c!r:.60})")
            continue
        if cid in seen:
            problems.append(f"routing/cases.yaml: {cid} appears twice")
        seen.add(cid)
        if c.get("expected") != "none" and c.get("expected") not in names:
            problems.append(f"routing/cases.yaml: {cid} expects '{c.get('expected')}', which is not in skills/ or drafts/")
    expected = {c.get("expected") for c in cases if isinstance(c, dict)}
    problems += [f"routing/cases.yaml: no case expects {n}: add one written against its closest neighbour"
                 for n in sorted(catalog - expected)]
    return problems


OTHER_MANIFESTS = (".codex-plugin/plugin.json", ".agents/plugins/marketplace.json",  # Codex
                   "gemini-extension.json", ".antigravity-plugin/plugin.json")      # Gemini CLI, Antigravity


def check_other_manifests(root: Path, version: str | None) -> list[str]:
    """Other agents' manifests (docs/install.md): valid JSON, same version as the Claude marketplace, skills from skills/ only."""
    problems = []
    for rel in OTHER_MANIFESTS:
        path = root / rel
        if not path.is_file():
            continue
        try:
            data = json.loads(path.read_text())
        except ValueError as e:
            problems.append(f"{rel}: not valid JSON ({e})")
            continue
        if "version" in data and data["version"] != version:
            problems.append(f"{rel}: version {data['version']} differs from .claude-plugin/marketplace.json ({version})")
        if "skills" in data and data["skills"] != "./skills/":
            problems.append(f"{rel}: skills must be \"./skills/\" (drafts and templates never ship)")
    return problems


def main(root: Path, sync: bool = False, evidence: bool = True) -> int:
    problems = []
    catalog = sorted(p for p in (root / "skills").glob("*") if p.is_dir())
    drafts = sorted(p for p in (root / "drafts").glob("*") if p.is_dir())
    if len(catalog) > MAX_SKILLS:
        problems.append(f"skills/: {len(catalog)} skills, hard cap is {MAX_SKILLS}")
    known_sources = load_sources(root)
    foundations = root / "foundations"
    for folder in catalog + drafts:
        if sync and (folder / "SKILL.md").is_file():
            sync_foundations(folder, foundations)
        errors = check_skill(folder, folder in catalog, known_sources, foundations)
        if folder in catalog and not errors and evidence:
            errors = check_evidence(root, folder)
        for e in errors:
            problems.append(f"{folder.relative_to(root)}: {e}")
    descriptions = {}
    for folder in catalog + drafts:
        try:
            fm, _ = read_frontmatter(folder / "SKILL.md")
            if isinstance(fm.get("description"), str):
                descriptions[folder.name] = fm["description"]
        except (OSError, ValueError):
            pass
    problems += overlapping_descriptions(descriptions)
    if (root / "routing" / "cases.yaml").is_file():
        problems += check_routing(root / "routing" / "cases.yaml", {p.name for p in catalog + drafts}, {p.name for p in catalog})
    market = root / ".claude-plugin" / "marketplace.json"
    if market.is_file():  # the bundle plugin installs exactly the catalogue, drafts never
        if (root / ".claude-plugin" / "plugin.json").is_file():  # claude plugin validate misses this: installs, then fails to load
            problems.append(".claude-plugin/plugin.json: remove it, it conflicts with marketplace.json entries that list skills")
        data = json.loads(market.read_text())
        bundle = data["plugins"][0]["skills"]
        if sorted(bundle) != [f"./skills/{p.name}" for p in catalog]:
            problems.append(".claude-plugin/marketplace.json: the first plugin must list exactly the skills/ folders")
        stale = [pl for pl in data["plugins"][1:] if pl.get("name") in descriptions and pl.get("description") != descriptions[pl["name"]]]
        if stale and sync:  # a plugin's description is what triggers it once installed: keep it equal to SKILL.md
            for pl in stale:
                pl["description"] = descriptions[pl["name"]]
            market.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
        elif stale:
            problems.append(f".claude-plugin/marketplace.json: descriptions differ from SKILL.md for {sorted(pl['name'] for pl in stale)}; "
                            "run python3 scripts/validate_skills.py --sync")
        problems += check_other_manifests(root, data.get("metadata", {}).get("version"))

    for p in problems:
        print(p)
    print(f"{len(catalog)} skills, {len(drafts)} drafts, {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    sys.exit(main(Path(args[0]) if args else Path(__file__).parent.parent, sync="--sync" in sys.argv,
                  evidence="--no-evidence" not in sys.argv))
