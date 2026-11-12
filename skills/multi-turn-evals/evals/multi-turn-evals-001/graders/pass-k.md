---
type: regex  # asks for repeated runs per scenario
pattern: 'pass\^ ?(k|\d)|pass-hat|(each|every) (scenario|conversation|case)[^\n.]{0,50}\b(\d+|k|three|five|several|multiple) times|(repeat|rerun|re-run|replay|simulat|run)\w*[^\n.]{0,50}\b(\d+|k|three|five|several|multiple) (times|runs|trials|seeds)|(\b\d+|\bk|three|five|several|multiple|(?<!(\bnot|n.t|\bnever) )\b(fix|set|choose|define|pick|agree)\w* (on )?(the |a )?number of)( \w+)? (repeats|reruns|runs|trials) (per|for each|of each) (scenario|conversation|case)|number of (\w+ )?(repeats|reruns|runs|trials) (per|for each|of each) (scenario|conversation|case)s? ?[(:=,]? ?(\d|k\b|three|five)|pass\w* (on|in|across) (every|all|each) (repeat|run|trial)'
flags: i
---
