import sys
input = sys.stdin.readline

n = int(input())
all = []

for i in range(n):
  x, y = map(int, input().split())
  all.append([y, x])

all.sort()

for i in all:
  y = i[0]
  x = i[1]
  print(x, y, sep=' ')  
