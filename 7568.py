import sys
input = sys.stdin.readline

n = int(input())
all = []

for i in range(n):
  x, y = map(int, input().split())
  all.append([x, y])

answer = []

for i in all:
  k = 1
  for j in all:
    if i[0] < j[0] and i[1] < j[1]:
      k += 1
  answer.append(k)

for i in range(n):
  if i < n-1:
    print(answer[i], end=' ')
  else:
    print(answer[i])
