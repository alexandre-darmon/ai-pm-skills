#!/usr/bin/env python3
"""Count, rate and price failure modes from an error-analysis reading log. Standard library only.

Reading log (CSV, one row per trace, in the order the expert read them):
    trace_id,stream,class,mode
    stream = random | targeted
    mode   = the failure mode of the trace's first upstream failure; empty or "pass" when it passed

Costs (optional CSV): mode,cost_eur  (the sourced cost of one occurrence)

    python3 failure_modes.py log.csv [--costs costs.csv] [--monthly-volume 9000] [--window 20]

Shares come from the random stream only: targeted traces over-represent failures. Each share carries
its 95% Wilson interval; a mode absent from the random stream gets 0 with its upper bound.
"""
import argparse
import csv
import math
import sys

Z = 1.96
PASS = {"", "pass", "none", "ok"}


def wilson(k: int, n: int) -> tuple[float, float]:
    if n == 0:
        return float("nan"), float("nan")
    p, z2 = k / n, Z * Z
    d = 1 + z2 / n
    centre = (p + z2 / (2 * n)) / d
    half = Z * math.sqrt(p * (1 - p) / n + z2 / (4 * n * n)) / d
    return max(0.0, centre - half), min(1.0, centre + half)


def pct(x: float) -> str:
    return "n/a" if math.isnan(x) else f"{100 * x:.1f}%"


def eur(x: float) -> str:
    return f"{x:,.0f} EUR"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("log")
    ap.add_argument("--costs")
    ap.add_argument("--monthly-volume", type=float)
    ap.add_argument("--window", type=int, default=20, help="traces with no new mode that count as saturation")
    a = ap.parse_args()

    with open(a.log, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        sys.exit("empty reading log")
    missing = {"stream", "mode"} - set(rows[0])
    if missing:
        sys.exit(f"reading log lacks column(s): {', '.join(sorted(missing))}")
    odd = sorted({r["stream"].strip().lower() for r in rows} - {"random", "targeted"})
    if odd:
        sys.exit(f"stream must be random or targeted, found: {', '.join(odd)}")
    costs = {}
    if a.costs:
        with open(a.costs, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                try:
                    costs[r["mode"].strip()] = float(r.get("cost_eur", "").strip())
                except ValueError:
                    pass  # "to source" or empty: no sourced cost, the mode stays unpriced

    n_random = sum(r["stream"].strip().lower() == "random" for r in rows)
    seen, last_new = {}, 0
    for i, r in enumerate(rows, start=1):
        mode = r["mode"].strip()
        if mode.lower() in PASS:
            continue
        stream = "random" if r["stream"].strip().lower() == "random" else "targeted"
        m = seen.setdefault(mode, {"random": 0, "targeted": 0, "classes": set(), "first": i})
        m[stream] += 1
        m["classes"].add(r.get("class", "").strip() or "-")
        if m["first"] == i:
            last_new = i

    since = len(rows) - last_new
    print(f"Traces read: {len(rows)} (random {n_random}, targeted {len(rows) - n_random})")
    print(f"Last new mode at trace {last_new}; traces read since: {since}; "
          f"saturation (>= {a.window} with no new mode): {'reached' if since >= a.window else 'NOT reached, taxonomy provisional'}")
    if n_random == 0:
        print("No random stream: shares and monthly costs cannot be estimated.")
    passed = n_random - sum(m["random"] for m in seen.values())
    if n_random:
        lo, hi = wilson(passed, n_random)
        print(f"Random traces with no failure: {passed}/{n_random} = {pct(passed / n_random)} [{pct(lo)}, {pct(hi)}]")
    print()

    table = []
    for mode, m in seen.items():
        share = m["random"] / n_random if n_random else float("nan")
        lo, hi = wilson(m["random"], n_random)
        cost = costs.get(mode)
        monthly = None
        if a.monthly_volume and cost is not None and n_random:
            monthly = tuple(a.monthly_volume * s * cost for s in (share, lo, hi))
        table.append((mode, m, share, lo, hi, cost, monthly))
    table.sort(key=lambda t: (-(t[6][0] if t[6] else -1), -(0 if math.isnan(t[2]) else t[2]), -(t[1]["random"] + t[1]["targeted"])))

    print("| Mode | Random | Targeted | Share of random [95% interval] | Classes | Cost per occurrence | Expected monthly cost [interval] |")
    print("| --- | --- | --- | --- | --- | --- | --- |")
    for mode, m, share, lo, hi, cost, monthly in table:
        share_txt = f"{pct(share)} [{pct(lo)}, {pct(hi)}]" if n_random else "n/a"
        if n_random and m["random"] == 0:
            share_txt = f"not seen in random, up to {pct(hi)}"
        cost_txt = eur(cost) if cost is not None else "to source"
        month_txt = f"{eur(monthly[0])} [{eur(monthly[1])}, {eur(monthly[2])}]" if monthly else "-"
        print(f"| {mode} | {m['random']} | {m['targeted']} | {share_txt} | {', '.join(sorted(m['classes']))} | {cost_txt} | {month_txt} |")
    return 0


if __name__ == "__main__":
    sys.exit(main())
