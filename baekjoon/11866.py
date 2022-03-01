import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
que = [ i for i in range(1, n+1)]
que = deque(que)
start = 0
ans = []

while len(ans) < n:

  que.rotate(-(k-1))
  ans.append(que.popleft())

print('<', end='')
for i in range(n):
  if i < n-1:
    print(ans[i], end=', ')
  else:
    print(ans[i], end='>')
print()
