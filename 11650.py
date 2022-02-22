import sys
input = sys.stdin.readline

n = int(input())
all = []

for i in range(n):
  all.append(list(map(int, input().split())))

all.sort()

for num in all:
  a = num[0]
  b = num[1]
  print(a, b, sep=' ')
