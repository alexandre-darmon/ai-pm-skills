#!/usr/bin/env python3
"""Control limits for a sampled pass rate, the run rule, and the sample size per class.

Rates may be given in percent (91) or as fractions (0.91).

  python3 scripts/control_limits.py --history 92,90,93,89,91,92,90,91,93,89 --n 100 --latest 86 --drop 5
  python3 scripts/control_limits.py --centre 90 --drop 5
"""
import argparse
import math

RUN = 8  # periods in a row on one side of the centre line


def frac(x: float) -> float:
    return x / 100 if x > 1 else x


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--history", help="past period rates, comma-separated")
    ap.add_argument("--centre", type=float, help="centre line, if no history")
    ap.add_argument("--n", type=int, help="sampled traces per period")
    ap.add_argument("--latest", type=float, help="latest period rate")
    ap.add_argument("--drop", type=float, help="drop that matters, in points (5) or fraction (0.05)")
    a = ap.parse_args()

    history = [frac(float(v)) for v in a.history.split(",")] if a.history else []
    if history:
        p = sum(history) / len(history)
        print(f"centre line {p:.1%} from {len(history)} periods")
    elif a.centre is not None:
        p = frac(a.centre)
        print(f"centre line {p:.1%} (given)")
    else:
        ap.error("give --history or --centre")

    if a.n:
        sigma = math.sqrt(p * (1 - p) / a.n)
        lcl, ucl = max(0.0, p - 3 * sigma), min(1.0, p + 3 * sigma)
        print(f"n {a.n} per period: sigma {sigma * 100:.2f} points, 3-sigma limits {lcl:.1%} to {ucl:.1%} (±{3 * sigma * 100:.1f} points)")
        if a.latest is not None:
            x = frac(a.latest)
            if x < lcl or x > ucl:
                print(f"latest {x:.1%}: OUTSIDE the limits -> alert, investigate")
            else:
                print(f"latest {x:.1%}: inside the limits -> noise unless a run rule fires; investigate, do not roll back on it")
            series = history + [x]
            side = [v < p for v in series if v != p]
            streak = 0
            for s in reversed(side):
                if s == side[-1]:
                    streak += 1
                else:
                    break
            where = "below" if side and side[-1] else "above"
            fired = streak >= RUN
            print(f"run rule ({RUN} in a row on one side): {'FIRED' if fired else 'not met'} ({streak} {where} the centre)")

    if a.drop:
        d = a.drop / 100 if a.drop >= 1 else a.drop
        n_half = math.ceil(9 * p * (1 - p) / d ** 2)
        n_most = math.ceil(16 * p * (1 - p) / d ** 2)
        print(f"to catch a {d * 100:.1f}-point drop: n >= {n_half} per class per period (limit at the drop, ~50% in its first period), "
              f"n >= {n_most} for ~84% in its first period")


if __name__ == "__main__":
    main()
