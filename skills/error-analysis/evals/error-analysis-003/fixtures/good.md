I would not let an LLM label the 5,000 conversations on its own: an LLM doing the first pass applies generic categories nobody has checked, and "hallucination" or "tone" will not tell the committee what broke after the prompt change.

What fits before Friday:

1. **Mask, then sample 100 conversations**: 60 at random and 40 targeted on complaints and escalations since the prompt change.
2. **One expert reads them first** (the head of customer service or a senior advisor), writing a free note on what went wrong in each, on the first upstream failure. At 2 to 3 minutes per conversation this is 4 to 5 hours, one day. Stop when about 20 conversations in a row add no new failure: that is saturation.
3. **Then the LLM clusters the expert's notes** into proposed failure modes; the expert keeps, merges or rewrites each one. The categories come from the notes, not from a predefined list.
4. **Write a binary pass/fail definition per mode**, with a pass and a fail example.
5. **For the dashboard**: shares come from the 60 random conversations, with their interval. To score all 5,000, build one LLM judge per mode and calibrate it on the expert's labels (TPR and TNR) before trusting its counts; that can follow next week.

The Friday dashboard then shows real failure modes, how often they occur and what each costs, with the taxonomy marked provisional if saturation is not reached.
