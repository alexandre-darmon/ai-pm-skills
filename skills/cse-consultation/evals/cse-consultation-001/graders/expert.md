---
type: regex  # the CSE can appoint an expert
pattern: '\bL\.?\s?2315-94\b|\b(CSE|it|committee|comité)\b[^\n]{0,30}\b(appoints?|calls? on|commissions?|hires?|designates?|uses?|be assisted by|désign\w*|recour\w*|fai\w* appel)\b[^\n]{0,15}\b(an? |un )?experts?\b|\bexpert(ise)?\b[^\n]{0,40}\b(appointed|paid|commissioned|chosen|payée?) (by|par) (the |le )?(CSE|committee|employer|employeur)\b|\bassist[ée]+ d[''’]un expert'
flags: i
---
