import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque()

for i in range(n):
  
  command = str(input())[:-1]
  
  if command == 'pop':
    if queue:
      print(queue.popleft())
      continue
    else:
      print(-1)
      continue
  elif command == 'size':
    print(len(queue))
    continue
  elif command == 'empty':
    if queue:
      print(0)
      continue
    else:
      print(1)
      continue
  elif command == 'front':
    if queue:
      print(queue[0])
      continue
    else:
      print(-1)
      continue
  elif command == 'back':
    if queue:
      print(queue[-1])
      continue
    else:
      print(-1)
      continue
  else:
    num = int(command[5:])
    queue.append(num)
    continue
