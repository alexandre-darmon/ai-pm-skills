#!/usr/bin/env python3
"""Agent reliability from trial results: pass@1, pass^k, pass@k, the bound on events never seen, and attack runs.

Stdlib only. Run from the skill folder:

  python3 scripts/agent_reliability.py --k 3 5/5 4/5 5/5 2/5 5/5      # successes/trials, one per task
  python3 scripts/agent_reliability.py --k 3 --events 0 --volume 9000 5/5 5/5 4/5 ...
  python3 scripts/agent_reliability.py --per-trial 0.9 --k 3            # what a per-trial rate gives over k trials
  python3 scripts/agent_reliability.py --pass-at-k 0.9 --k 3            # what a pass@k figure can hide
  python3 scripts/agent_reliability.py --target 0.01                    # clean trials needed to bound a rate
  python3 scripts/agent_reliability.py --attack change_payee=2/150 --attack send_outside=0/150 \
      --utility 282/300 231/300 --attacked-volume 50                     # the same tasks clean and under attack

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


def parse_cn(text: str) -> tuple[int, int]:
    try:
        c, n = (int(x) for x in text.split("/"))
    except ValueError:
        sys.exit(f"{text}: expected successes/trials, e.g. 2/150")
    if not 0 <= c <= n or n == 0:
        sys.exit(f"{text}: need 0 <= successes <= trials and trials > 0")
    return c, n


def upper_bound(c: int, n: int) -> tuple[float, str]:
    """95% upper bound on a rate: rule of three when nothing was seen, Wilson otherwise."""
    if c == 0:
        r3, exact = zero_bound(n)
        return r3, f"rule of three; exact {pct(exact)}, Wilson {pct(wilson(0, n)[1])}"
    return wilson(c, n)[1], "Wilson"


def report_attacks(attacks: list[str], volume: int | None) -> None:
    print("Attack success per forbidden action (gate on the upper bound, references/eval-statistics.md §2):")
    for item in attacks:
        name, _, cn = item.rpartition("=")
        c, n = parse_cn(cn)
        bound, how = upper_bound(c, n)
        line = f"  {name or 'attack'}: {c}/{n} = {pct(c / n)}, upper bound {pct(bound)} ({how})"
        if volume:
            line += f" -> up to {bound * volume:,.1f} successful attacks a month at {volume:,} attacked runs a month"
        print(line)
    print("  measured on attacks kept apart from those used to tune the defence, or it proves nothing")


def report_utility(clean: str, attacked: str) -> None:
    (c1, n1), (c2, n2) = parse_cn(clean), parse_cn(attacked)
    lo1, hi1 = wilson(c1, n1)
    lo2, hi2 = wilson(c2, n2)
    print(f"Benign utility: {pct(c1 / n1)}  95% interval {pct(lo1)} to {pct(hi1)}")
    print(f"Utility under attack: {pct(c2 / n2)}  95% interval {pct(lo2)} to {pct(hi2)}")
    print(f"  drop under attack: {100 * (c1 / n1 - c2 / n2):.1f} points (same tasks, clean then attacked)")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("results", nargs="*", help="successes/trials per task, e.g. 4/5")
    ap.add_argument("--k", type=int, default=3)
    ap.add_argument("--events", type=int, help="forbidden events observed across all trials")
    ap.add_argument("--volume", type=int, help="monthly volume of the action, to turn a bound into an exposure")
    ap.add_argument("--per-trial", type=float, help="per-trial success rate p: prints p^k and 1-(1-p)^k")
    ap.add_argument("--pass-at-k", type=float, help="a pass@k figure: prints the per-trial rate it implies if tasks were alike")
    ap.add_argument("--target", type=float, help="rate to bound, e.g. 0.01: prints the clean trials needed")
    ap.add_argument("--attack", action="append", metavar="ACTION=C/N",
                    help="successful attacks / attacked trials for one forbidden action, e.g. change_payee=2/150 (repeat per action)")
    ap.add_argument("--attacked-volume", type=int, help="attacked runs a month (an assumption), to turn an attack bound into an exposure")
    ap.add_argument("--utility", nargs=2, metavar="C/N", help="benign utility and utility under attack on the same tasks, e.g. 282/300 231/300")
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
    if a.utility:
        report_utility(*a.utility)
    if a.attack:
        report_attacks(a.attack, a.attacked_volume)
    if not (a.results or a.per_trial is not None or a.pass_at_k is not None or a.target is not None or a.attack or a.utility):
        ap.print_help()


if __name__ == "__main__":
    main()
