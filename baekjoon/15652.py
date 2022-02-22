import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n, m = map(int, input().split())

nums = [i for i in range(1, n+1)]

all = list(combinations_with_replacement(nums, m))

for a in all:
  for i in range(m):
    if i < m-1:
      print(a[i], end = ' ')
    else:
      print(a[i])
