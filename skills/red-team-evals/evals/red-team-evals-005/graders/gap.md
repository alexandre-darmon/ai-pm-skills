---
type: regex  # compares the tuned set with the fresh set
pattern: '\bgap\b|differen\w*[^\n.]{0,60}(tun|fresh|new|held|unseen)|compar\w*[^\n.]{0,80}(fresh|new|held|unseen|tun\w*)|(drop|fall)s?[^\n.]{0,40}(fresh|new|held|unseen)'
flags: i
weight: 2
---
