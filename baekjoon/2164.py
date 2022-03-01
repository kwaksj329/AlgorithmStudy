import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

que = [ i for i in range(1, n+1)]
que = deque(que)

if len(que) == 1:
  print(*que)

while len(que) > 1:
  que.popleft()
  temp = que.popleft()
  que.append(temp)

  if len(que) == 1:
    print(*que)
    break
