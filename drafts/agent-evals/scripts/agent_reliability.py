#!/usr/bin/env python3
"""Agent reliability from trial results: pass@1, pass^k, pass@k and the bound on events never seen.

Stdlib only. Run from the skill folder:

  python3 scripts/agent_reliability.py --k 3 5/5 4/5 5/5 2/5 5/5      # successes/trials, one per task
  python3 scripts/agent_reliability.py --k 3 --events 0 --volume 9000 5/5 5/5 4/5 ...
  python3 scripts/agent_reliability.py --per-trial 0.9 --k 3            # what a per-trial rate gives over k trials
  python3 scripts/agent_reliability.py --pass-at-k 0.9 --k 3            # what a pass@k figure can hide
  python3 scripts/agent_reliability.py --target 0.01                    # clean trials needed to bound a rate

The task is the unit (references/eval-statistics.md §1): rates are averaged per task, then over tasks,
and intervals come from a bootstrap over tasks. pass^k per task uses C(c,k)/C(n,k), unbiased when n >= k.
"""
from __future__ import annotations

import argparse
import math
import random
import sys


def pass_hat_k(c: int, n: int, k: int) -> float:
    """Chance that k trials drawn from this task's n all succeed."""
    return math.comb(c, k) / math.comb(n, k)


def pass_at_k(c: int, n: int, k: int) -> float:
    """Chance that at least one of k trials drawn from this task's n succeeds."""
    return 1 - math.comb(n - c, k) / math.comb(n, k)


def bootstrap(values: list[float], reps: int = 5000, seed: int = 0) -> tuple[float, float]:
    rng = random.Random(seed)
    means = sorted(sum(rng.choice(values) for _ in values) / len(values) for _ in range(reps))
    return means[int(0.025 * reps)], means[int(0.975 * reps) - 1]


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    p = k / n
    centre = (p + z * z / (2 * n)) / (1 + z * z / n)
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return max(0.0, centre - half), min(1.0, centre + half)


def zero_bound(n: int) -> tuple[float, float]:
    """95% upper bound on a rate never observed in n independent trials: rule of three, and the exact value."""
    return 3 / n, 1 - 0.05 ** (1 / n)


def pct(x: float) -> str:
    return f"{100 * x:.1f}%"


def from_results(results: list[str], k: int, events: int | None, volume: int | None) -> None:
    tasks = []
    for r in results:
        c, n = (int(x) for x in r.split("/"))
        if not 0 <= c <= n or n < k:
            sys.exit(f"{r}: need 0 <= successes <= trials and trials >= k ({k})")
        tasks.append((c, n))
    trials = sum(n for _, n in tasks)
    p1 = [c / n for c, n in tasks]
    hat = [pass_hat_k(c, n, k) for c, n in tasks]
    at = [pass_at_k(c, n, k) for c, n in tasks]
    mean = lambda v: sum(v) / len(v)  # noqa: E731
    print(f"Tasks: {len(tasks)} · trials: {trials} · k = {k}")
    lo, hi = bootstrap(p1)
    print(f"pass@1 (mean per-trial success): {pct(mean(p1))}  95% interval {pct(lo)} to {pct(hi)}")
    lo, hi = bootstrap(hat)
    print(f"pass^{k} (all {k} trials succeed): {pct(mean(hat))}  95% interval {pct(lo)} to {pct(hi)}")
    print(f"  for comparison, pass@1 ^ {k} = {pct(mean(p1) ** k)}")
    print(f"pass@{k} (at least one of {k}): {pct(mean(at))}  capability only, never a gate on an action that cannot be undone")
    if len(tasks) < 10:
        print("  fewer than 10 tasks: the bootstrap interval is too narrow, read it as indicative")
    if events is not None:
        report_events(events, trials, len(tasks), volume)


def report_events(events: int, trials: int, tasks: int, volume: int | None) -> None:
    if events:
        lo, hi = wilson(events, trials)
        print(f"Forbidden events: {events} in {trials} trials = {pct(events / trials)}  95% interval {pct(lo)} to {pct(hi)}")
        bound = hi
    else:
        r3, exact = zero_bound(trials)
        print(f"Forbidden events: 0 in {trials} trials. The true rate can still be up to {pct(r3)} (rule of three; exact 95% bound {pct(exact)})")
        if tasks < trials:
            t3, _ = zero_bound(tasks)
            print(f"  if trials of a task fail together, count tasks instead: up to {pct(t3)} over {tasks} tasks")
        bound = r3
    if volume:
        print(f"Exposure the gate accepts: up to {bound * volume:,.0f} events a month at {volume:,} a month")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("results", nargs="*", help="successes/trials per task, e.g. 4/5")
    ap.add_argument("--k", type=int, default=3)
    ap.add_argument("--events", type=int, help="forbidden events observed across all trials")
    ap.add_argument("--volume", type=int, help="monthly volume of the action, to turn a bound into an exposure")
    ap.add_argument("--per-trial", type=float, help="per-trial success rate p: prints p^k and 1-(1-p)^k")
    ap.add_argument("--pass-at-k", type=float, help="a pass@k figure: prints the per-trial rate it implies if tasks were alike")
    ap.add_argument("--target", type=float, help="rate to bound, e.g. 0.01: prints the clean trials needed")
    a = ap.parse_args()
    if a.per_trial is not None:
        p = a.per_trial
        print(f"Per trial {pct(p)} -> pass^{a.k} = {pct(p ** a.k)}, pass@{a.k} = {pct(1 - (1 - p) ** a.k)}")
    if a.pass_at_k is not None:
        p = 1 - (1 - a.pass_at_k) ** (1 / a.k)
        print(f"pass@{a.k} = {pct(a.pass_at_k)} -> per trial {pct(p)} if every task were alike, pass^{a.k} = {pct(p ** a.k)}")
        print(f"  with unequal tasks it can be lower: a task counts as passed after a single success in {a.k}")
    if a.target is not None:
        print(f"To bound a rate at {pct(a.target)} with zero events: {math.ceil(3 / a.target):,} clean trials (rule of three)")
    if a.results:
        from_results(a.results, a.k, a.events, a.volume)
    elif a.events is not None:
        sys.exit("--events needs the per-task results to count trials")
    if not (a.results or a.per_trial is not None or a.pass_at_k is not None or a.target is not None):
        ap.print_help()


if __name__ == "__main__":
    main()
