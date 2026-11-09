#!/usr/bin/env python3
"""Read a vendor bake-off: per-class rates with intervals, paired gaps against noise, cost per correct outcome.

Input: a CSV with columns `case_id`, `class`, then one column per candidate (vendor or current process),
values 1 (the business unit is correct, e.g. every critical field of the document) or 0. All candidates
ran on the same cases. A case run several times is averaged before it gets here (the case is the unit).

Output:
- per candidate and per class: correct / n, rate, Wilson 95% interval, "indicative" under 30 cases;
- per pair of candidates, overall and per class: d (cases where exactly one is right), the gap in points,
  the noise 2*sqrt(d)/n in points, and "tie" when the gap is smaller (references/eval-statistics.md section 5);
- with --volume and --cost NAME=EUR (total cost for the period, human review and correction included):
  cost per correct outcome = cost / (volume x overall rate).

Python 3.9+, standard library only.

Example:
  python3 bakeoff.py results.csv --volume 25000 --cost A=200000 --cost B=165000
"""
import argparse
import csv
import itertools
import math
import sys

Z95 = 1.959964
MIN_CLASS = 30


def wilson(k, n, z=Z95):
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    centre = (p + z * z / (2 * n)) / (1 + z * z / n)
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return (max(0.0, centre - half), min(1.0, centre + half))


def read(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        sys.exit("empty CSV")
    names = [c for c in rows[0] if c not in ("case_id", "class")]
    if len(names) < 1 or "class" not in rows[0]:
        sys.exit("need columns case_id, class and at least one candidate")
    data = []
    for r in rows:
        try:
            data.append((r["class"], {n: int(r[n]) for n in names}))
        except ValueError:
            sys.exit(f"case {r.get('case_id')}: values must be 0 or 1")
    return names, data


def pct(x):
    return f"{100 * x:.1f}%"


def report(names, data, volume=None, costs=None):
    classes = sorted({c for c, _ in data})
    groups = [("ALL", data)] + [(c, [d for d in data if d[0] == c]) for c in classes]
    print("== Rates per class (Wilson 95%)")
    for label, rows in groups:
        n = len(rows)
        flag = "  indicative (n < 30)" if n < MIN_CLASS else ""
        for name in names:
            k = sum(v[name] for _, v in rows)
            lo, hi = wilson(k, n)
            print(f"{label:<20} {name:<12} {k}/{n} = {pct(k / n)}  [{pct(lo)} to {pct(hi)}]{flag}")
    print("\n== Paired comparison (same cases)")
    for a, b in itertools.combinations(names, 2):
        for label, rows in groups:
            n = len(rows)
            only_a = sum(1 for _, v in rows if v[a] and not v[b])
            only_b = sum(1 for _, v in rows if v[b] and not v[a])
            d = only_a + only_b
            gap = (only_a - only_b) / n
            noise = 2 * math.sqrt(d) / n
            verdict = "tie" if abs(gap) < noise or d == 0 else f"real gap, {a if gap > 0 else b} ahead"
            print(f"{label:<20} {a} vs {b}: d = {d} ({a} only {only_a}, {b} only {only_b}), "
                  f"gap {100 * gap:+.1f} pts, noise {100 * noise:.1f} pts -> {verdict}")
    if volume and costs:
        print("\n== Cost per correct outcome (overall rate)")
        n = len(data)
        for name, cost in costs.items():
            if name not in names:
                sys.exit(f"--cost {name}: no such column")
            rate = sum(v[name] for _, v in data) / n
            correct = volume * rate
            per = cost / correct if correct else float("inf")
            print(f"{name:<12} {cost:,.0f} EUR / ({volume:,} x {pct(rate)} = {correct:,.0f} correct) = {per:.2f} EUR")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("csv")
    ap.add_argument("--volume", type=int, help="business units per period")
    ap.add_argument("--cost", action="append", default=[], help="NAME=total cost for the period, in EUR")
    args = ap.parse_args()
    costs = {}
    for c in args.cost:
        name, _, value = c.partition("=")
        costs[name] = float(value)
    names, data = read(args.csv)
    report(names, data, args.volume, costs)


if __name__ == "__main__":
    main()
