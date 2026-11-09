"""Intervals for eval scores: how much a mean could move if other cases had been written.

Pure Python on purpose: CI only installs pyyaml.
"""
import math
import random


def macro_mean(groups):
    """Mean of the group means: each skill weighs the same, whatever its number of cases."""
    return sum(sum(g) / len(g) for g in groups) / len(groups)


def bootstrap_ci(groups, draws=10_000, level=0.95, seed=0):
    """Percentile interval for macro_mean(groups), resampling cases within each group (stratified bootstrap).

    A plain bootstrap on n cases shrinks the spread of a mean by (n - 1) / n, which matters at 3 to 5 cases
    per skill. Each resampled group mean is therefore stretched by sqrt(n / (n - 1)) around the observed one
    (Rao and Wu's rescaled bootstrap), so the interval is not narrower than the data allow. A group of one
    case has no spread to resample and stays fixed. The seed is fixed so a regenerated file does not drift.
    """
    rng = random.Random(seed)
    fixed = [(len(g), sum(g) / len(g), math.sqrt(len(g) / (len(g) - 1)) if len(g) > 1 else 0.0) for g in groups]
    stats = []
    for _ in range(draws):
        total = 0.0
        for g, (n, m, stretch) in zip(groups, fixed):
            resampled = sum(g[int(rng.random() * n)] for _ in range(n)) / n
            total += m + stretch * (resampled - m)
        stats.append(total / len(groups))
    stats.sort()
    tail = (1 - level) / 2
    return stats[int(draws * tail)], stats[min(draws - 1, int(draws * (1 - tail)))]
