"""Fail if README.md or skill-eval-gains.md are not what the generators would write today.

Runs scripts/eval_gains.py and scripts/readme_catalog.py on a scratch copy of the two files, with the real baselines/,
skills/ and drafts/ symlinked in (the generators only read them), then compares. The two output files are written in
the scratch folder only. INPUTS must list every folder the generators read: a generator that reads a new folder must
add it here, or the check regenerates from a partial tree.
    python3 scripts/check_generated.py          # exit 1 and a diff when a file is stale
"""
import contextlib
import difflib
import io
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import eval_gains  # noqa: E402
import readme_catalog  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
FILES = ("README.md", "skill-eval-gains.md")
INPUTS = ("baselines", "skills", "drafts")  # everything eval_gains.main and readme_catalog.main read under root


def regenerate(root=ROOT):
    """Return {file name: text the generators would write} without touching root."""
    with tempfile.TemporaryDirectory() as tmp:
        scratch = Path(tmp)
        for d in INPUTS:
            if (root / d).is_dir():
                (scratch / d).symlink_to((root / d).resolve(), target_is_directory=True)
        for f in FILES:
            if (root / f).is_file():
                shutil.copyfile(root / f, scratch / f)
        with contextlib.redirect_stdout(io.StringIO()):
            eval_gains.main(scratch)
            readme_catalog.main(scratch)
        return {f: (scratch / f).read_text() for f in FILES if (scratch / f).is_file()}


def stale(root=ROOT):
    """Return [(file name, unified diff)] for each generated file that differs from what is on disk."""
    out = []
    for f, fresh in regenerate(root).items():
        current = (root / f).read_text() if (root / f).is_file() else ""
        if current != fresh:
            diff = "".join(difflib.unified_diff(current.splitlines(True), fresh.splitlines(True), f"{f} (on disk)", f"{f} (regenerated)"))
            out.append((f, diff))
    return out


def main(root=ROOT):
    problems = stale(root)
    for f, diff in problems:
        print(f"{f} is stale: run python3 scripts/eval_gains.py and python3 scripts/readme_catalog.py\n{diff}")
    if not problems:
        print(f"generated blocks up to date: {', '.join(FILES)}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
