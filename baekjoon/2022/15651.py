import sys
from itertools import product
input = sys.stdin.readline

n, m = map(int, input().split())

nums = [i for i in range(1, n+1)]

all = list(product(nums, repeat=m))

for a in all:
  for i in range(m):
    if i < m-1:
      print(a[i], end=' ')
    else:
      print(a[i])

