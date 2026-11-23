---
type: regex  # splits the release: the classes that clear their bar ship, the costly one stays reviewed or held
pattern: '(ship|release|go[- ]live|launch|deploy)\w*[^.\n]{0,40}\b((the )?(other|remaining) (four|three|4|3)\b|the rest\b|(everything|all|every class|every queue|the classes|the queues) (else )?(except|but|other than)\b)|\b((other|remaining) (four|three|4|3)|(four|three|4|3) other) (classes|queues)\b[^\n]{0,60}\b(ship|go live|goes live|go-live|release|launch|deploy|go ahead|proceed)'
flags: i
---
