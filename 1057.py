import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())
result = 1

while(n != 1):
  
  if a % 2 == 1 and b % 2 == 0 and a+1 == b:
    break

  else:
    if a % 2 == 0:
      a = a // 2
    else:
      a = a // 2 + 1
    if b % 2 == 0:
      b = b // 2
    else:
      b = b // 2 + 1
    if n % 2 == 0:
      n = n // 2
    else:
      n = n // 2 + 1
    result += 1

  if n == 1:
    result = -1

print(result)
