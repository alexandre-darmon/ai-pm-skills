---
type: regex  # classification and extraction need a fixed workflow before any agent loop
pattern: 'workflow (before|first|rather than|instead of)|\bnot (an? |build an? |start with an? )?agent\b|(do not|don.t|no need to) (build|start with) an? agent|agent[^\n.]{0,60}(not needed|unnecessary|overkill|only (if|when)|later)'
flags: i
---
