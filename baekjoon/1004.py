import sys
import math
input = sys.stdin.readline

T = int(input())
i = 0
for i in range(0, T):
  answer = 0
  x1, y1, x2, y2 = map(int, input().split())
  n = int(input())
  for j in range(0, n):
    c1, c2, r = map(int, input().split())
    a = (x1 - c1) ** 2 + (y1 - c2) ** 2 - (r ** 2)
    b = (x2 - c1) ** 2 + (y2 - c2) ** 2 - (r ** 2)
    if a < 0 and b > 0:
      answer += 1
    elif a > 0 and b < 0:
      answer += 1
  print(answer)
