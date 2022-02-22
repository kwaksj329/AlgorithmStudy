import sys
from itertools import combinations
input = sys.stdin.readline

n, k = map(int, input().split())

all = {}

for i in range(0, n):
  num = int(input())
  all[num] = [num]

while max(all.keys()) <= 10000:
  temp = list(all.keys())
  if k in temp:
    break
  couple = list(combinations(temp, 2))
  for a, b in couple:
    if a+b not in temp:
      all[a+b] = list(tuple(all[a] + all[b]))
      temp.append(a+b)
    if a+b in temp and :
      

if k not in all:
  print(-1)
else:
  print(len(all[k]))
