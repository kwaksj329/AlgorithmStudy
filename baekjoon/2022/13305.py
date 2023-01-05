import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))
min = cost[0]
sum = 0

for i in range(n-1):

  if min > cost[i]:
    min = cost[i]
  sum += (min * road[i])

print(sum)
