#!/usr/bin/env python3
"""Read an LLM judge as a classifier against expert labels, and correct the pass rate it reports.

Input: a CSV of the judge's TEST split (labels never used to write or tune its prompt), with
columns `human` and `judge`, values `pass` or `fail` (other columns are ignored).

Output:
- confusion counts (expert x judge);
- TPR (judge passes what the expert passes) and TNR (judge fails what the expert fails),
  each with its Wilson 95% interval;
- raw agreement, flagged as not sufficient, next to what a judge that passes everything would get;
- Cohen's kappa between judge and expert;
- with --observed-pass K --observed-n N (the judge's verdicts on unlabelled traffic): the corrected
  pass rate (Rogan-Gladen) with a percentile bootstrap 95% interval that resamples the labelled
  rows (within each expert class) and the observed sample together.

Python 3.9+, standard library only. Fixed seed: the same input gives the same interval.

Examples:
  python3 judge_metrics.py example.csv
  python3 judge_metrics.py example.csv --observed-pass 340 --observed-n 400
  python3 judge_metrics.py example.csv --tpr-target 0.80 --tnr-target 0.80
"""
import argparse
import csv
import math
import random
import sys

Z95 = 1.959964
MIN_CLASS = 20      # fewer expert passes or fails than this: the rate is indicative only
MIN_YOUDEN = 0.5    # TPR + TNR - 1 below this: the correction is unstable
VALUES = {"pass": True, "fail": False}


def wilson(k, n, z=Z95):
    """Wilson score interval for k successes out of n."""
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return (max(0.0, centre - half), min(1.0, centre + half))


def read_labels(path):
    """Return a list of (human_pass, judge_pass) booleans from the CSV."""
    rows = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fields = {(name or "").strip().lower(): name for name in (reader.fieldnames or [])}
        missing = [c for c in ("human", "judge") if c not in fields]
        if missing:
            sys.exit(f"error: {path} needs columns human and judge (missing: {', '.join(missing)})")
        for line, row in enumerate(reader, start=2):
            h = (row.get(fields["human"]) or "").strip().lower()
            j = (row.get(fields["judge"]) or "").strip().lower()
            if not h and not j:
                continue
            if h not in VALUES or j not in VALUES:
                sys.exit(f"error: {path} line {line}: human and judge must be pass or fail, got {h!r} and {j!r}")
            rows.append((VALUES[h], VALUES[j]))
    if not rows:
        sys.exit(f"error: {path} has no labelled rows")
    return rows


def corrected_rate(observed, tpr, tnr):
    """Rogan-Gladen: (observed + TNR - 1) / (TPR + TNR - 1), clipped to [0, 1]. None if undefined."""
    youden = tpr + tnr - 1
    if youden <= 0:
        return None
    return min(1.0, max(0.0, (observed + tnr - 1) / youden))


def binomial(rng, n, p):
    """Number of successes in n draws with probability p (resampling n items with replacement)."""
    return sum(1 for _ in range(n) if rng.random() < p)


def bootstrap(tp, n_pos, tn, n_neg, k_obs, n_obs, resamples, seed):
    """Percentile 95% interval of the corrected rate, resampling the expert-pass rows, the expert-fail
    rows and the observed sample. Returns (low, high, dropped) where dropped counts resamples with
    TPR + TNR - 1 <= 0, for which the correction is undefined."""
    rng = random.Random(seed)
    tpr, tnr, obs = tp / n_pos, tn / n_neg, k_obs / n_obs
    values, dropped = [], 0
    for _ in range(resamples):
        est = corrected_rate(binomial(rng, n_obs, obs) / n_obs,
                             binomial(rng, n_pos, tpr) / n_pos,
                             binomial(rng, n_neg, tnr) / n_neg)
        if est is None:
            dropped += 1
        else:
            values.append(est)
    if not values:
        return (float("nan"), float("nan"), dropped)
    values.sort()
    lo = values[int(0.025 * (len(values) - 1))]
    hi = values[int(math.ceil(0.975 * (len(values) - 1)))]
    return (lo, hi, dropped)


def fmt(x):
    return "n/a" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{x:.3f}"


def target_line(name, rate, low, target):
    if target is None:
        return None
    point = "met" if rate >= target else "NOT met"
    bound = "clears it" if low >= target else "is below it"
    return f"  {name} target {target:.2f} (set before measuring): {point} on the point estimate; the lower bound {low:.3f} {bound}"


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Judge metrics on a labelled test split (TPR, TNR with Wilson intervals, kappa) and the "
                    "corrected pass rate on unlabelled traffic (Rogan-Gladen, bootstrap interval).",
        epilog="The CSV must be the test split: labels never used to write, tune or illustrate the judge prompt. "
               "Metrics on tuning labels describe the tuning, not the judge.")
    ap.add_argument("csv", help="test split CSV with columns human,judge (values pass/fail)")
    ap.add_argument("--observed-pass", type=int, metavar="K", help="answers the judge passed on unlabelled traffic")
    ap.add_argument("--observed-n", type=int, metavar="N", help="answers the judge scored on unlabelled traffic")
    ap.add_argument("--tpr-target", type=float, help="TPR target written before measuring (e.g. 0.80)")
    ap.add_argument("--tnr-target", type=float, help="TNR target written before measuring (e.g. 0.80)")
    ap.add_argument("--resamples", type=int, default=10000, help="bootstrap resamples (default 10000)")
    ap.add_argument("--seed", type=int, default=20261109, help="random seed (default 20261109)")
    args = ap.parse_args(argv)

    if (args.observed_pass is None) != (args.observed_n is None):
        ap.error("--observed-pass and --observed-n go together")
    if args.observed_n is not None and not (0 < args.observed_n and 0 <= args.observed_pass <= args.observed_n):
        ap.error("need 0 <= --observed-pass <= --observed-n and --observed-n > 0")
    if args.resamples < 1000:
        ap.error("--resamples must be at least 1000")

    rows = read_labels(args.csv)
    n = len(rows)
    tp = sum(1 for h, j in rows if h and j)
    fn = sum(1 for h, j in rows if h and not j)
    fp = sum(1 for h, j in rows if not h and j)
    tn = sum(1 for h, j in rows if not h and not j)
    n_pos, n_neg = tp + fn, fp + tn
    warnings = []

    print(f"Judge on test split: {args.csv} ({n} labelled answers: {n_pos} expert pass, {n_neg} expert fail)")
    print()
    print("Confusion counts             judge pass   judge fail")
    print(f"  expert pass                {tp:>10}   {fn:>10}")
    print(f"  expert fail                {fp:>10}   {tn:>10}")
    print()

    tpr = tp / n_pos if n_pos else None
    tnr = tn / n_neg if n_neg else None
    tpr_ci = wilson(tp, n_pos)
    tnr_ci = wilson(tn, n_neg)
    print(f"TPR (judge passes what the expert passes)  {fmt(tpr)}   95% CI {fmt(tpr_ci[0])} to {fmt(tpr_ci[1])}   ({tp}/{n_pos})")
    print(f"TNR (judge fails what the expert fails)    {fmt(tnr)}   95% CI {fmt(tnr_ci[0])} to {fmt(tnr_ci[1])}   ({tn}/{n_neg})")
    for line in (target_line("TPR", tpr, tpr_ci[0], args.tpr_target) if tpr is not None else None,
                 target_line("TNR", tnr, tnr_ci[0], args.tnr_target) if tnr is not None else None):
        if line:
            print(line)

    agreement = (tp + tn) / n
    pass_everything = n_pos / n
    print(f"Raw agreement                              {fmt(agreement)}   NOT SUFFICIENT on its own: a judge that "
          f"passes everything would agree {fmt(pass_everything)} here")

    judge_pass = (tp + fp) / n
    chance = judge_pass * (n_pos / n) + (1 - judge_pass) * (n_neg / n)
    kappa = (agreement - chance) / (1 - chance) if chance < 1 else None
    print(f"Cohen's kappa (judge vs expert)            {fmt(kappa)}")

    if n_pos < MIN_CLASS:
        warnings.append(f"only {n_pos} expert passes: TPR is indicative, label more passing answers")
    if n_neg < MIN_CLASS:
        warnings.append(f"only {n_neg} expert fails: TNR is indicative, label more failing answers "
                        "(enrich the sample with likely fails)")
    youden = (tpr + tnr - 1) if tpr is not None and tnr is not None else None
    if youden is not None and youden < MIN_YOUDEN:
        warnings.append(f"TPR + TNR - 1 = {youden:.3f} < {MIN_YOUDEN}: the judge separates pass from fail too "
                        "weakly; a corrected rate would be unstable, do not use this judge for a rate")

    if args.observed_n is not None:
        print()
        obs = args.observed_pass / args.observed_n
        print("Pass rate on unlabelled traffic, corrected for the judge's errors (Rogan-Gladen)")
        print(f"  observed (judge)   {fmt(obs)}   ({args.observed_pass}/{args.observed_n}), biased by the judge's errors")
        if tpr is None or tnr is None:
            print("  corrected          n/a: the test split needs both expert passes and expert fails")
        else:
            est = corrected_rate(obs, tpr, tnr)
            if est is None:
                print("  corrected          n/a: TPR + TNR - 1 <= 0, the judge is no better than chance")
            else:
                raw = (obs + tnr - 1) / youden
                lo, hi, dropped = bootstrap(tp, n_pos, tn, n_neg, args.observed_pass, args.observed_n,
                                            args.resamples, args.seed)
                clipped = "" if 0 <= raw <= 1 else f" (clipped from {raw:.3f})"
                print(f"  corrected          {fmt(est)}{clipped}   95% bootstrap CI {fmt(lo)} to {fmt(hi)}")
                print(f"  ({args.resamples} resamples of the expert-pass rows, the expert-fail rows and the "
                      f"observed sample; seed {args.seed})")
                if dropped:
                    share = dropped / args.resamples
                    print(f"  {dropped} resample(s) had TPR + TNR - 1 <= 0 and were dropped ({share:.1%})")
                    if share > 0.01:
                        warnings.append("more than 1% of resamples had no defined correction: the interval is "
                                        "not reliable")
                if not 0 <= raw <= 1:
                    warnings.append("the uncorrected estimate fell outside 0-1: the observed rate and the judge's "
                                    "TPR/TNR disagree, re-validate the judge on fresh production labels")

    if warnings:
        print()
        print("Warnings")
        for w in warnings:
            print(f"  - {w}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
