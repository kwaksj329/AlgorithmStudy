import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

for i in range(n):
  n, m = map(int, input().split())
  paper = list(map(int, input().split()))
  paper = deque(paper)
  order = 0
  while True:
    front = paper[0]
    maxnum = max(paper)
    if front < maxnum:
      paper.rotate(-1)
      if m == 0:
        m = len(paper)-1
      else:
        m -= 1
    else:
      paper.popleft()
      order += 1
      if m == 0:
        break
      m -= 1

  print(order)
