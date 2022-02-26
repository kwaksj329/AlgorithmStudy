import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())

for i in range(n):
  case = int(input())
  all = {}
  for j in range(case):
    a, b = map(str, input().split())
    if b not in all:
      all[b] = 1
    else:
      all[b] += 1

  ans = 1
  num = []
  for k, v in all.items(): 
    ans *= (v+1)
  print(ans-1)
