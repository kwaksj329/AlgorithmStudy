import sys
input = sys.stdin.readline

n = int(input())

xs = list(map(int, input().split()))
origin = xs[:]
xs = list(set(xs))
xs.sort()

dic = {}
for i,x in enumerate(xs):
  dic[x] = i

for i, e in enumerate(origin):
  if i < n-1:
    print(dic[e], end=' ')
  else:
    print(dic[e])
