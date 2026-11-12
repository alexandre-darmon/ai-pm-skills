I would not send the note as planned. Two of its asks break the plan she signed: the disputes bar was set at 90% before the run, and lowering it to 80% after seeing the results reads the results instead of judging them. And two more weeks of dispute cases is not an extension of this spike; it is a reshape, with its own appetite and kill date.

**First, the numbers need one more pass.** The definition of correct moved in both directions on day two: wrong sub-reason now passes, wrong transaction date now fails. You re-scored only the misses, so the 25 disputes it got right were never checked against the date rule; some of them could now fail. Re-grade all 110 chats under the final definition before anything goes to her, and log the change with its date and reason (day two, after reading the first outputs: sub-reason is not what the dispute agents need; the date is). That drift log goes to whoever builds the release eval set.

**Read per class, not pooled.** 100 of 110 overall hides the class the project exists for.

| Class | n of N | Rate | 95% interval (Wilson) | Reading against 90% bar, 75% stop line |
|---|---|---|---|---|
| Fees | 38 of 40 | 95% | 83.5% to 98.6% | promising: plausible, not demonstrated |
| Lost card | 37 of 40 | 92.5% | 80.1% to 97.4% | promising |
| Disputes | 25 of 30 | 83% | 66.4% to 92.7% | undecided: the interval straddles the 75% stop line |

From `spike_readout.py --class disputes=25/30 --bar 0.90 --stop 0.75 --spend 4.20 --appetite 0.05`:

```
disputes         25 of 30   83.3%    66.4% to 92.7%   90.0%   undecided
```

Disputes are undecided: the data fits a true rate under the stop line as well as one over the bar. That is a reason to reshape, not to lower the bar.

**Cost per correct routing:** 4.20 EUR / 100 correct = 0.042 EUR, not 0.038 per chat. Within the 0.05 ceiling, with less room than the per-chat figure suggests.

**Draft note**

> Spike result, card-servicing chat routing (plan signed on [date], ended today as planned).
>
> Fees 38 of 40 and lost card 37 of 40: promising against the 90% bar, not yet demonstrated. Disputes 25 of 30 (interval about 66% to 93%): undecided, the interval reaches below the 75% stop line. Scores are being re-graded on all 110 chats under the final definition of correct, logged with date and reason. Cost per correct routing 0.042 EUR, within the 0.05 ceiling.
>
> The 90% bar stays as signed. I propose a reshape: a second spike on disputes only, about 60 more anonymised dispute chats, its own time box of five days, its own cost ceiling and a new kill date, for your signature. If disputes stay undecided after that, we decide whether disputes leave scope.

None of these numbers is release evidence: if this goes to a PRD, the release eval set is sampled from live traffic per class and sized before its run.
