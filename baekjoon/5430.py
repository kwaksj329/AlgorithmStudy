import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for i in range(t):

  p = str(input())[:-1]
  n = int(input())
  num = str(input())[1:-2]
  if num:
    num = list(map(int, num.split(',')))
    num = deque(num)
  else:
    num = []
    num = deque(num)
  left = True
  err = False

  for k in range(len(p)):

    if p[k] == 'R':
      left = not left
    elif p[k] == 'D' and left:
      if num:
        num.popleft()
      else:
        print('error')
        err = True
        break
    elif p[k] == 'D' and not left:
      if num:
        num.pop()
      else:
        print('error')
        err = True
        break

  if num and not err:
    if left:
      print('[', end='')
      for i in range(len(num)):
        if i < len(num)-1:
          print(num[i], end=',')
        else:
          print(num[i], end=']')
          print()
    else:
      num = list(num)[::-1]
      print('[', end='')
      for i in range(len(num)):
        if i < len(num)-1:
          print(num[i], end=',')
        else:
          print(num[i], end=']')
          print()
  elif not num and not err:
    print('[]')
