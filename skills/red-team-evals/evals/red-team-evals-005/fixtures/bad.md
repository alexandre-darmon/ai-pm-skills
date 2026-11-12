**The sentence needs two fixes, but the campaign itself is solid.**

1. **Count attacks, not runs.** The 5 runs of one attack are not independent, so the unit is the attack: 400 attacks, not 2,000 runs. Per class, the lookup class is 3 successful runs on 150 attacks.

2. **Add intervals per class.** 0 of 100 prompt-extraction attacks still allows up to about 3.7% (Wilson 95%), so that class is undecided against its 1% tolerance. The upload class (2 of 80) is also undecided, and the lookup class may be over its 0.5% tolerance.

The security team's 400 attacks give good coverage of the four classes, and starting from the prompt engineers' work saved time. To read each class under its tolerance you need about 381 attacks for 1% and 765 for 0.5%. Add the five successful attacks to the regression suite.

Suggested sentence: "On 400 attacks (version 2.3, 5 runs each, counted per attack), no class can yet be read as under its signed tolerance; the cross-customer lookup class may be over it. Per-class rates and 95% intervals in table X."
