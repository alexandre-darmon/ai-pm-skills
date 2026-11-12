# Sign-off note: advisor copilot

The campaign ran 600 attacks with 21 successes (3.5%), under the 5% bar agreed beforehand. However, the overall figure masks a concentrated weakness: instructions hidden in uploaded client documents succeeded in 12 of 40 attempts (30%).

**Recommendation: conditional go on Friday.** Release with document upload disabled until the injection fix is in place; the 21 successful attacks become regression tests, and upload injection is re-tested with fresh attacks before uploads are re-enabled. Client-data leakage at 2.7% should get its own stricter tolerance in the next campaign.
