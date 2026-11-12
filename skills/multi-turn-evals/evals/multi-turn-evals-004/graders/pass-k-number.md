---
type: regex  # computes what pass^3 gives at the pilot rate, tied to 0.92 or to pass^k
pattern: '0[.,]92\s*(\^|\*\*)\s*3|0[.,]92\s*³|0[.,]92 cubed|92 ?%\s*(\^|\*\*)\s*3|0[.,]92[^\n]{0,80}(0[.,]7[6-9]|\b7[6-9]([.,]\d+)? ?%)|pass\^ ?(3|k)[^\n]{0,80}(0[.,]7[6-9]|\b7[6-9]([.,]\d+)? ?%)|(0[.,]7[6-9]|\b7[6-9]([.,]\d+)? ?%)[^\n]{0,60}pass\^ ?(3|k)'
flags: i
---
