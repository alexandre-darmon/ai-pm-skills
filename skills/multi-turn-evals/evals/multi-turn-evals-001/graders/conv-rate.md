---
type: regex  # the conversation failure rate (24 of 120 = 20%) is priced: the cost of one failed conversation or wrong quote is asked of the business owner, so the monthly count becomes money
pattern: '\b(cost|price|loss) (of|per) (a |one |each )?(single )?(failed|wrong|bad|failing|unsuitable|mis-?sold)\b[^.!?\n]{0,20}\b(conversations?|quotes?|answers?|cases?)|\b(failed|wrong|bad|unsuitable) (conversations?|quotes?)\b[^.!?\n]{0,30}\bcosts?\b'
flags: i
---
