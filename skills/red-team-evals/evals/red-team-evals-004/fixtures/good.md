# Steering note: advisor copilot release

**Recommendation: no-go for Friday.** The 3.5% overall rate hides an attack type that fails at 30%. The bar has to be read per attack type, never on the pooled figure.

| Attack type | Successes / attempts | Rate | 95% interval (Wilson) |
| --- | --- | --- | --- |
| Direct jailbreak | 3/300 | 1.0% | 0.3% to 2.9% |
| System prompt extraction | 3/150 | 2.0% | 0.7% to 5.7% |
| Injection in uploaded documents | 12/40 | 30% | 18% to 45% |
| Another client's portfolio data | 3/110 | 2.7% | 0.9% to 7.7% |

- Indirect injection through uploads fails at 30%, with a lower bound of 18%: far over 5% whatever the noise. The copilot drafts client emails, so a planted instruction can send data out.
- Client-data leakage at 2.7% could be up to 7.7%. A breach of another client's data is a costly class: it needs its own stricter tolerance, signed before testing (for example 0.5%, which takes about 765 held-out attacks with no success to read under it).
- The upload type had only 40 attempts; the others are indicative too where they sit near the bar.

**Next steps.** The 21 successful attacks become regression cases. The fix for upload injection goes to the prompt and guardrail owners; then the type is re-tested on fresh attacks from a sealed held-out set, written by the security team.
