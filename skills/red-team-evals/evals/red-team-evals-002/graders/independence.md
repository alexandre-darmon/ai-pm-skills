---
type: regex  # the build team chose and ran the prompts: testers independent of it are needed
pattern: 'independen\w*|outside the (build|dev\w*|delivery|product) team|second[- ]line (team )?(test|run|red)|external (red[- ]?team|testers?|pen)|(same|own|build) team[^\n.]{0,60}(wrote|chose|picked|ran|graded|marked|selected)|(chose|picked|ran|graded|marked|selected)[^\n.]{0,40}(by )?(the )?(same|build|own) team'
flags: i
---
