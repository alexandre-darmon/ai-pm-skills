---
type: regex  # labels kept in approved storage
flags: i
---
approved[^\n]{0,30}(storage|store|database|share|location|server|environment|repository)|(storage|store|database|share)[^\n]{0,40}(approved|sanctioned|validated by (IT|security))|not (on|in) (a |the |your |anyone.s )?(laptop|browser|local ?storage|localStorage)
