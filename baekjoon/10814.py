import sys
from operator import itemgetter
input = sys.stdin.readline

n = int(input())

members = []

for i in range(n):
  sage, name = map(str, input().split())
  age = int(sage)
  members.append([age, name])

members = sorted(members, key =itemgetter(0))

for m in members:
  print(m[0], m[1], sep=' ')
