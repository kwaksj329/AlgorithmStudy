import sys
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
  command = str(input())[:-1]

  if command == 'pop':
    if stack:
      print(stack.pop())
    else:
      print(-1)
  elif command == 'size':
    print(len(stack))
  elif command == 'empty':
    if stack:
      print(0)
    else:
      print(1)
  elif command == 'top':
    if stack:
      print(stack[-1])
    else:
      print(-1)
  else:
    number = command.split(' ')[-1]
    stack.append(int(number))
