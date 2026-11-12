#!/usr/bin/env python3
"""Attack-success rates per class with Wilson 95% intervals, the pooled rate it must not replace, and sizing.

Unit: n = independent seeds (an attack idea with its context). A seed counts as one success when the
success criterion is met in any of the fixed attempts run for it (best of k). Variants of a seed are attempts.

Results:  python3 redteam_rates.py [--relevant N] [--attempts A] class=successes/seeds[:tolerance] ...
          tolerance as a share (0.01) or a percent (1%). --relevant: attack classes judged relevant
          (tested + untested), for the coverage share. --attempts: estimated attack attempts a month on
          the live feature (from logs, conversation analysis or incident data, never the conversation
          count), to turn an upper bound into an exposure.
Sizing:   python3 redteam_rates.py --plan 0.01 0.005 ...
          held-out seeds needed per class so the Wilson 95% upper bound (the bound the reading uses)
          falls under r with 0, 1 or 2 successes. Total seeds to write = held-out n / held-out share.
Stdlib only.
"""
from __future__ import annotations

import math
import sys

Z = 1.96


def wilson(k: int, n: int) -> tuple[float, float]:
    if n == 0:
        return 0.0, 1.0
    p, z2 = k / n, Z * Z
    centre = (p + z2 / (2 * n)) / (1 + z2 / n)
    half = Z * math.sqrt(p * (1 - p) / n + z2 / (4 * n * n)) / (1 + z2 / n)
    return max(0.0, centre - half), min(1.0, centre + half)


def share(text: str) -> float:
    return float(text[:-1]) / 100 if text.endswith("%") else float(text)


def seeds_needed(r: float, k: int) -> int:
    n = max(k + 1, int(Z * Z * (1 - r) / r) - 5)
    while wilson(k, n)[1] >= r:
        n += 1
    return n


def plan(rates: list[str]) -> None:
    print("tolerable rate | seeds if 0 successes (about 4/r) | if 1 success | if 2 successes | rule of three (3/r), one-sided, for reference")
    for r in map(share, rates):
        print(f"{r:.2%} | {seeds_needed(r, 0)} | {seeds_needed(r, 1)} | {seeds_needed(r, 2)} | {math.ceil(3 / r)}")
    print("Held-out seeds only; count independent seeds, not variants. Plan with a margin for a success or two.")


def results(args: list[str], relevant: int | None, attempts: float | None) -> None:
    rows, tot_k, tot_n = [], 0, 0
    for arg in args:
        name, _, rest = arg.partition("=")
        frac, _, tol = rest.partition(":")
        k, n = (int(x) for x in frac.split("/"))
        lo, hi = wilson(k, n)
        tol_v = share(tol) if tol else None
        if tol_v is None:
            reading = "no tolerance signed"
        elif hi < tol_v:
            reading = "under tolerance"
        elif lo > tol_v:
            reading = "OVER tolerance"
        else:
            reading = "undecided: more seeds"
        if k == 0:
            reading += f" (0 in {n}: up to about {hi:.1%} by Wilson, {3 / n:.1%} by the rule of three)"
        rows.append((name, k, n, lo, hi, tol_v, reading))
        tot_k, tot_n = tot_k + k, tot_n + n
    print("class | successes/seeds | rate | 95% interval | tolerance | reading")
    for name, k, n, lo, hi, tol_v, reading in rows:
        tol_s = f"{tol_v:.1%}" if tol_v is not None else "-"
        print(f"{name} | {k}/{n} | {k / n:.1%} | {lo:.1%} to {hi:.1%} | {tol_s} | {reading}")
        if attempts and hi > 0:
            p100 = 1 - (1 - hi) ** 100
            print(f"   at the upper bound: up to {hi * attempts:,.0f} successes on {attempts:,.0f} attempts a month;"
                  f" a persistent attacker needs about {1 / hi:,.0f} tries for a first success; P(>=1 in 100 tries) = {p100:.0%}")
    lo, hi = wilson(tot_k, tot_n)
    print(f"pooled (never alone) | {tot_k}/{tot_n} | {tot_k / tot_n:.1%} | {lo:.1%} to {hi:.1%} | - | hides the worst class")
    worst = max(rows, key=lambda r: r[1] / r[2])
    print(f"worst class: {worst[0]} at {worst[1] / worst[2]:.1%} ({worst[3]:.1%} to {worst[4]:.1%})")
    if relevant:
        print(f"coverage: {len(rows)} of {relevant} relevant classes tested = {len(rows) / relevant:.0%}; list the untested ones")


def main(argv: list[str]) -> None:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return
    if argv[0] == "--plan":
        plan(argv[1:])
        return
    relevant = attempts = None
    rest = []
    it = iter(argv)
    for a in it:
        if a == "--relevant":
            relevant = int(next(it))
        elif a == "--attempts":
            attempts = float(next(it))
        else:
            rest.append(a)
    results(rest, relevant, attempts)


if __name__ == "__main__":
    main(sys.argv[1:])
