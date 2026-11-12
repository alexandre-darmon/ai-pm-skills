**Not yet: the 0 of 120 is a development score, not evidence.** The filter was adjusted on those same 120 emails, so the re-run shows it remembers them, not that it holds. Ask for a fresh attack set, written by someone who did not tune the filter and never shown to the vendor.

1. **Plant the attacks in real tasks.** Take the 300 client emails with their approved actions and build attacked copies: the same request, with an instruction hidden in the body or the PDF. Run the same tasks clean and attacked, in a sandbox.
2. **Three numbers:** benign utility (clean pass rate, which also shows the filter's false positives), utility under attack (the approved action done and the injected goal not reached) and attack success rate per forbidden action: contact details changed, documents sent to an address not on file.
3. **Bound, not point.** Even 0 of 120 on a fresh set still allows up to about 2.5% (3/120) per action. Gate on that upper bound against the cost of one statement sent outside.
4. Contact changes and sends to a new address keep an out-of-band check until the bound is low enough.
