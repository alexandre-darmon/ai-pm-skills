#!/usr/bin/env python3
"""Reliability table: what a confidence bucket can honestly say to a user.

Stdlib only. Run from the skill folder, one bucket per argument as label=correct/total:

  python3 scripts/reliability_table.py 0.9-1=470/500 0.6-0.9=150/210 0-0.6=33/80 --tolerate 0.85
  python3 scripts/reliability_table.py 0.9-1=470/500 --claim 0.9-1=0.98 --tolerate 0.85   # test a label such as "98% sure"

--tolerate is the lowest correct rate the use accepts. Without it no bucket gets a figure,
because whether a bucket may show one depends on that rate.

For each bucket it prints the observed rate, the Wilson 95% interval (references/eval-statistics.md §2),
the strongest frequency the bucket supports (its lower bound, rounded down to 5 points), and what to show.
A bucket under --min-cases labelled cases supports no figure.
"""
from __future__ import annotations

import argparse
import math
import sys

Z = 1.96


def wilson(k: int, n: int, z: float = Z) -> tuple[float, float]:
    """Wilson score interval for k successes out of n."""
    if n == 0:
        return 0.0, 1.0
    p = k / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return max(0.0, centre - half), min(1.0, centre + half)


def parse_bucket(text: str) -> tuple[str, int, int]:
    try:
        label, frac = text.split("=", 1)
        k, n = (int(x) for x in frac.split("/", 1))
    except ValueError:
        raise argparse.ArgumentTypeError(f"expected label=correct/total, got {text!r}")
    if n <= 0 or not 0 <= k <= n:
        raise argparse.ArgumentTypeError(f"need 0 <= correct <= total and total > 0, got {text!r}")
    return label, k, n


def parse_claim(text: str) -> tuple[str, float]:
    try:
        label, value = text.split("=", 1)
        v = float(value.rstrip("%"))
    except ValueError:
        raise argparse.ArgumentTypeError(f"expected label=rate, got {text!r}")
    return label, v / 100 if v > 1 else v


def verdict(k: int, n: int, claim: float | None, tolerate: float | None, min_cases: int) -> dict:
    lo, hi = wilson(k, n)
    supported = math.floor(lo * 20) / 20  # lower bound rounded down to 5 points
    out = {"rate": k / n, "lo": lo, "hi": hi, "supported": supported}
    if claim is not None:
        out["claim"] = "contradicted" if claim > hi else "not demonstrated" if claim > lo else "supported"
    if n < min_cases:
        out["show"] = f"no figure: fewer than {min_cases} labelled cases"
    elif tolerate is None:
        out["show"] = "set --tolerate: no figure until the tolerated rate is known"
    elif lo < tolerate:
        out["show"] = "no figure: lower bound below what the use tolerates; sources only, or no answer and a hand-off if an error is costly"
    else:
        out["show"] = f'"in testing, at least {round(supported * 100)} in 100 answers like this were right"'
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("buckets", nargs="+", type=parse_bucket, help="label=correct/total")
    ap.add_argument("--claim", action="append", type=parse_claim, default=[], help="label=rate, e.g. 0.9-1=0.95")
    ap.add_argument("--tolerate", type=float, help="lowest correct rate the use accepts, e.g. 0.85")
    ap.add_argument("--min-cases", type=int, default=100)
    args = ap.parse_args(argv)
    claims = dict(args.claim)
    unknown = set(claims) - {b[0] for b in args.buckets}
    if unknown:
        ap.error(f"--claim names unknown buckets: {sorted(unknown)}")
    print("| Bucket | Correct | Rate | 95% interval | Claim | What to show |")
    print("| --- | --- | --- | --- | --- | --- |")
    for label, k, n in args.buckets:
        v = verdict(k, n, claims.get(label), args.tolerate, args.min_cases)
        claim = f"{claims[label]:.0%}: {v['claim']}" if label in claims else "-"
        print(f"| {label} | {k}/{n} | {v['rate']:.1%} | {v['lo']:.1%} to {v['hi']:.1%} | {claim} | {v['show']} |")
    return 0


if __name__ == "__main__":
    sys.exit(main())
