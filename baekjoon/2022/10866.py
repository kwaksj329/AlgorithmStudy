import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
que = deque()

for i in range(n):

  command = str(input())[:-1]
  
  if command == 'pop_front':
    if que:
      print(que.popleft())
    else:
      print(-1)
  elif command == 'pop_back':
    if que:
      print(que.pop())
    else:
      print(-1)
  elif command == 'size':
    print(len(que))
  elif command == 'empty':
    if que:
      print(0)
    else:
      print(1)
  elif command == 'front':
    if que:
      print(que[0])
    else:
      print(-1)
  elif command == 'back':
    if que:
      print(que[-1])
    else:
      print(-1)
  elif command[:9] == 'push_back':
    num = int(command[10:])
    que.append(num)
  else:
    num = int(command[11:])
    que.appendleft(num)
