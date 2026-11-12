**Do not send the sentence.** The table cannot support "every class is under its signed tolerance", for three reasons, and one class may already be over.

## 1. Count attacks, not runs

The 5 runs of one attack at temperature 0.7 are not independent: they are attempts on the same seed. The unit is the attack, and an attack counts as one success when any of its 5 runs succeeds (best of 5). So the lookup class is 150 attacks, not 750 runs, and the campaign is 400 attacks, not 2,000.

## 2. Take the October attacks out of the decision rate

160 of the 400 attacks are the ones the prompt engineers used while iterating on the prompt and the filter. The defence was tuned against them, so they are burned: they flatter every rate they are mixed into. Tag each row with its origin, move the 160 to the regression suite, and read the decision only on the security team's 240 new attacks. Report the two subsets separately per class: the gap between the reused set and the new set tells you whether the filter learned those attacks or the class.

## 3. Read each class on its interval

Even counting all 400 as if none had been seen (best case), per class with Wilson 95% intervals:

| Class | Successful attacks / attacks | Interval | Tolerance | Reading |
|---|---|---|---|---|
| Prompt extraction | 0/100 | 0% to 3.7% | 1% | undecided |
| Another customer's transactions | 1 to 3 /150 | 0.1% to 5.7% | 0.5% | undecided, over if the 3 runs are 3 different attacks (lower bound 0.7%) |
| Hidden instructions in uploads | 1 to 2 /80 | 0.2% to 8.7% | 1% | undecided |
| Fee refund promise | 0/70 | 0% to 5.2% | 1% | undecided |

On the 240 new attacks alone each class has fewer seeds, so the intervals are wider still.

## 4. Size the next round on the held-out seeds

To read a class under its tolerance with no success, the Wilson bound needs about 4/r held-out attacks: 381 for a 1% class and 765 for the 0.5% lookup class (about 1,130 if one succeeds). Write them as new seeds kept from the prompt engineers.

## 5. The five successes

Each successful attack, with its context, becomes a regression case run on every prompt, filter or model change. The cross-customer success goes to the guardrail owner now.

## Sentence for the memo

"Version 2.3, security team campaign (temperature 0.7, 5 runs per attack, an attack counted once if any run succeeds). 160 of the 400 attacks were used to develop the prompt and filter and are excluded from the decision rates; rates on the 240 new attacks per class, with 95% intervals, are in table X. No class can yet be read as under its signed tolerance; the cross-customer lookup class may be over it. Next round: 381 held-out attacks per 1% class and 765 for the lookup class."
