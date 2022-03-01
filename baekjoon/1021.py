import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
place = list(map(int, input().split()))
que = [i for i in range(1, n+1)]
que = deque(que)
place = deque(place)

ans = 0

while place:

  front = que[0]
  find = que.index(place[0])
  left = find
  right = len(que) - find

  if front == place[0]:
    que.popleft()
    place.popleft()

  elif left <= right:
    que.rotate(-left)
    ans += left

  elif right < left:
    que.rotate(right)
    ans += right

print(ans)

