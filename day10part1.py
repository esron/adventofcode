from collections import deque
from sys import stdin

score = 0

closing = {
  ')': ['(', 3],
  ']': ['[', 57],
  '}': ['{', 1197],
  '>': ['<', 25137],
}

for line in stdin:
  line = line.rstrip()
  q = deque()

  for c in line:
    if c in ('(', '[', '{', '<'):
      q.append(c)
    elif q[-1] == closing[c][0]:
      q.pop()
    else:
      score += closing[c][1]
      break

print(score)
