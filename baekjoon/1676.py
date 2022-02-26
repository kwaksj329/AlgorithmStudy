import sys
import math
input = sys.stdin.readline

n = int(input())
n = math.factorial(n)

st = str(n)
ans = 0
for s in range(len(st)-1, -1, -1):
  if st[s] == '0':
    ans += 1
    continue
  else:
    break

print(ans)
