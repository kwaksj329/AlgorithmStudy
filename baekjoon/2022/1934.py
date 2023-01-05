import sys
input = sys.stdin.readline

n = int(input())
ans = 1
for i in range(n):
  a, b = map(int, input().split())

  if a > b:
    x = a
    y = b
  else:
    x = b
    y = a

  minimum = y
  while minimum > 1:

    minimum = x % y
    if minimum == 0:
      break
    else:
      x = y
      y = minimum

  print(a * b // y)
