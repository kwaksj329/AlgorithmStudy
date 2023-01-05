import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

nums = [ i for i in range(1, n+1)]

all = list(combinations( nums, m))

for a in all:
  a = list(a)
  a.sort()
  for i in range(m):
    if i < m-1:
      print(a[i], end = ' ')
    else:
      print(a[i])
