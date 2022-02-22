import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
max = 0

cards = list(map(int, input().split()))

all = list(combinations(cards, 3))

for i in all:
  temp = sum(i)
  if temp > max and temp <= m:
    max = temp

print(max)
