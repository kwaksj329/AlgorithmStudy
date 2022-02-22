import sys
import math
input = sys.stdin.readline

T = int(input())
for i in range(0, T):
  n, m = map(int, input().split())
  result = math.factorial(m) // (math.factorial(n) * math.factorial(m-n))
  print(result)
