---
type: regex  # the vendor's success criterion, attacks and settings are unknown
pattern: '(success|jailbreak|resistance)[^\n.]{0,40}(criteri\w*|defin\w*)|what counts as (a )?(success|jailbreak|resist)|(generation|sampling|decoding) settings|temperature|which (attacks|prompts)|(attack set|prompts?|benchmark)[^\n.]{0,60}(unknown|not disclosed|undisclosed|not published|unpublished|we (have not|haven[''’]t) seen)'
flags: i
---
