#!/usr/bin/env python3
"""Read a feasibility spike: per class n of N with a Wilson interval against the bar and stop line fixed
before the run, cost per correct answer against the appetite, and the reading that drives the decision.

Stdlib only. Run from the skill folder:

  python3 scripts/spike_readout.py --class passports=28/30 --class registry=9/10 --bar 0.90 --stop 0.75
  python3 scripts/spike_readout.py --class motor=14/15:0.90 --class injury=9/12:0.95 --stop 0.70 \
      --spend 31 --appetite 0.25
  python3 scripts/spike_readout.py --plan 0.75                    # cases a spike class needs for its stop line
  python3 scripts/spike_readout.py --size 0.95 --bar 0.90          # cases build-evals needs to show the bar
  python3 scripts/spike_readout.py --size 0.90 --margin 0.05       # cases to read a rate within ±5 points

--class name=k/n[:bar] gives one class (a per-class bar overrides --bar). --spend is the total model
cost of the run (same currency as --appetite, the maximum cost per correct answer fixed before the run).

Readings per class (references/eval-statistics.md §2, §4):
  clears        lower bound >= bar: the spike shows the bar is within reach (still not release evidence)
  promising     point >= bar, lower bound < bar but >= stop line: plausible, not demonstrated
  undecided     the interval straddles the stop line, or point < bar with upper bound >= bar
  short         upper bound < bar: even the optimistic reading misses the bar with this approach
  dead          upper bound < stop line: stop, or drop the class
"""
from __future__ import annotations

import argparse
import math
import sys


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    p = k / n
    centre = (p + z * z / (2 * n)) / (1 + z * z / n)
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return max(0.0, centre - half), min(1.0, centre + half)


def reading(k: int, n: int, bar: float, stop: float | None) -> str:
    lo, hi = wilson(k, n)
    if stop is not None and hi < stop:
        return "dead"
    if hi < bar:
        return "short"
    if lo >= bar:
        return "clears"
    if k / n >= bar and (stop is None or lo >= stop):
        return "promising"
    return "undecided"


def size(p: float, e: float) -> int:
    return math.ceil(1.96 ** 2 * p * (1 - p) / e ** 2)


def plan(stop: float, errors: int) -> int:
    """Smallest n where n - errors of n has a Wilson lower bound at or above the stop line."""
    n = errors + 1
    while wilson(n - errors, n)[0] < stop:
        n += 1
    return n


def pct(x: float) -> str:
    return f"{100 * x:.1f}%"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--class", dest="classes", action="append", default=[], metavar="NAME=K/N[:BAR]")
    ap.add_argument("--bar", type=float, help="bar for classes without their own")
    ap.add_argument("--stop", type=float, help="stop line: under it the idea is not worth pursuing")
    ap.add_argument("--spend", type=float, help="total model cost of the run")
    ap.add_argument("--appetite", type=float, help="maximum cost per correct answer, fixed before the run")
    ap.add_argument("--size", type=float, metavar="P", help="expected rate, to size a class for build-evals")
    ap.add_argument("--margin", type=float, help="half-width wanted with --size (default 0.05, or size - bar)")
    ap.add_argument("--plan", type=float, metavar="STOP", help="stop line, to size a spike class before the run")
    a = ap.parse_args()

    if a.plan is not None:
        if not 0 < a.plan < 1:
            sys.exit("--plan takes a stop line between 0 and 1")
        print(f"Spike class with a {pct(a.plan)} stop line: {plan(a.plan, 1)} cases (one error allowed), "
              f"{plan(a.plan, 0)} if it must be perfect. Under {plan(a.plan, 0)}, no result can read 'promising'.")
        if not a.classes and a.size is None:
            return

    if a.size is not None:
        if a.margin is None and a.bar is not None:
            if a.size <= a.bar:
                sys.exit("--size must be above --bar: an expected rate at or under the bar can never show it")
            m = a.size - a.bar
            print(f"Cases to show a {pct(a.bar)} bar on the lower bound when you expect {pct(a.size)} "
                  f"(margin {pct(m)}): {size(a.size, m)} per class")
        else:
            m = a.margin if a.margin is not None else 0.05
            print(f"Cases to read a rate near {pct(a.size)} within ±{pct(m)} at 95%: {size(a.size, m)} per class")
        if not a.classes:
            return

    if not a.classes:
        sys.exit("give at least one --class name=k/n[:bar]")
    total_k = total_n = 0
    readings = []
    print(f"{'class':<16}{'n of N':>9}{'rate':>8}   95% interval      bar    reading")
    for spec in a.classes:
        try:
            name, rest = spec.split("=")
            frac, _, bar_s = rest.partition(":")
            k, n = (int(x) for x in frac.split("/"))
            bar = float(bar_s) if bar_s else a.bar
        except ValueError:
            sys.exit(f"{spec}: expected name=k/n or name=k/n:bar")
        if bar is None:
            sys.exit(f"{name}: no bar (give --bar or name=k/n:bar)")
        if not 0 <= k <= n or n == 0:
            sys.exit(f"{spec}: need 0 <= k <= n and n > 0")
        lo, hi = wilson(k, n)
        r = reading(k, n, bar, a.stop)
        readings.append(r)
        total_k, total_n = total_k + k, total_n + n
        print(f"{name:<16}{f'{k} of {n}':>9}{pct(k / n):>8}   {pct(lo):>6} to {pct(hi):<7}{pct(bar):>6}   {r}")
        if n < 10:
            print(f"{'':<16}fewer than 10 cases: indicative only")
    if a.stop is not None:
        print(f"stop line: {pct(a.stop)}")

    if a.spend is not None:
        if total_k == 0:
            print("cost per correct answer: undefined, no correct answer")
        else:
            cpc = a.spend / total_k
            print(f"cost per answer: {a.spend / total_n:.3f} · cost per correct answer: {cpc:.3f} "
                  f"({a.spend} ÷ {total_k} correct, not ÷ {total_n} answers)")
            if a.appetite is not None:
                verdict = "within" if cpc <= a.appetite else f"over, {cpc / a.appetite:.1f} times"
                print(f"appetite: {a.appetite:.3f} per correct answer, {verdict}")

    if "dead" in readings:
        hint = "stop, or reshape without the dead class"
    elif "short" in readings or (a.spend is not None and a.appetite is not None and total_k and a.spend / total_k > a.appetite):
        hint = "reshape (other approach, narrower scope, lower autonomy level, cheaper path) or stop"
    elif "undecided" in readings:
        hint = "reshape: more cases for the undecided class is a new appetite and a new kill date, or drop the class"
    else:
        hint = "go to PRD, with every 'promising' class listed as not demonstrated for build-evals to size"
    print(f"decision the readings point to: {hint}")
    print("A spike number is never release evidence: build-evals samples from traffic and sizes each class.")


if __name__ == "__main__":
    main()
