"""Build release zips of the catalog: one per skill in skills/, and one bundle of all of them.

    python3 scripts/package_skills.py                     # dist/<skill>-<version>.zip and dist/ai-pm-skills-<today>.zip
    python3 scripts/package_skills.py --date 2026-11-12   # fixed bundle date (the release workflow passes the tag date)

Each zip holds <skill>/ as it installs: SKILL.md, references/, templates/, scripts/, plus <skill>/LICENSE (the
CC-BY-4.0 text from LICENSE-CC-BY-4.0). Left out: evals/ (the cases are the repo's evidence, not part of the skill),
results/, __pycache__/, *.pyc and OS litter. Deterministic: entries sorted, fixed timestamps and permissions,
so the same tree gives byte-identical zips. <out>/SHA256SUMS (also printed) names each zip by its bare file name,
so `sha256sum -c SHA256SUMS` checks the downloaded release assets.
Drafts are never packaged.
"""
import argparse
import datetime
import hashlib
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {"evals", "results", "__pycache__", ".git"}
SKIP_FILES = {".DS_Store", "Thumbs.db"}
STAMP = (1980, 1, 1, 0, 0, 0)  # earliest date a zip can hold
LICENSE = "LICENSE-CC-BY-4.0"
SUMS = "SHA256SUMS"  # written next to the zips, one `<sha256>  <file name>` line each


def version(folder):
    m = re.search(r'^\s+version:\s*"?([0-9A-Za-z.+-]+)"?\s*$', (folder / "SKILL.md").read_text(), re.M)
    if not m:
        sys.exit(f"{folder.name}: no metadata version in SKILL.md")
    return m.group(1)


def catalog(root=ROOT):
    return sorted(p for p in (root / "skills").iterdir() if (p / "SKILL.md").is_file())


def entries(folder):
    """(arcname, source path) for the files of one skill, sorted, without what does not ship."""
    out = []
    for p in folder.rglob("*"):
        rel = p.relative_to(folder)
        if not p.is_file() or SKIP_DIRS & set(rel.parts[:-1]) or p.name in SKIP_FILES or p.suffix == ".pyc":
            continue
        out.append((f"{folder.name}/{rel.as_posix()}", p))
    return sorted(out)


def write_zip(path, items):
    """items: sorted (arcname, bytes). Fixed timestamp, permissions and compression: same input, same bytes."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w") as z:
        for name, data in items:
            info = zipfile.ZipInfo(name, date_time=STAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3  # unix, whatever the build machine
            info.external_attr = 0o644 << 16
            z.writestr(info, data, compresslevel=9)


def skill_items(folder, license_text):
    items = [(name, src.read_bytes()) for name, src in entries(folder)]
    items.append((f"{folder.name}/LICENSE", license_text))
    return sorted(items)


def build(root=ROOT, out=None, date=None):
    out = Path(out) if out else root / "dist"
    date = date or datetime.date.today().isoformat()
    lic = root / LICENSE
    if not lic.is_file():
        sys.exit(f"missing {LICENSE}")
    license_text = lic.read_bytes()
    skills = catalog(root)
    if not skills:
        sys.exit("no skill in skills/")
    written, bundle = [], []
    for folder in skills:
        items = skill_items(folder, license_text)
        path = out / f"{folder.name}-{version(folder)}.zip"
        write_zip(path, items)
        written.append(path)
        bundle += items
    path = out / f"ai-pm-skills-{date}.zip"
    write_zip(path, sorted(bundle))
    written.append(path)
    (out / SUMS).write_text("".join(line + "\n" for line in checksums(written)))
    return written


def checksums(paths):
    """sha256sum lines with bare file names, so `sha256sum -c SHA256SUMS` passes next to the downloaded assets."""
    return [f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}" for p in paths]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", help="output folder (default dist/)")
    ap.add_argument("--date", help="bundle date, YYYY-MM-DD (default today)")
    a = ap.parse_args(argv)
    if a.date and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", a.date):
        ap.error("--date must be YYYY-MM-DD")
    for line in checksums(build(out=a.out, date=a.date)):
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
