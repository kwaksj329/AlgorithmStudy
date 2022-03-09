import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):

  n = int(input())
  all = []
  for j in range(n):
    temp = list(map(int, input().split()))
    all.append(temp)

  ans = 0
  all.sort(reverse=True)
  while all:

    a = all.pop()
    if not all:
      break
    k = all[0]
    #print(a, k)
    if ((a[0] - k[0]) ** 2 + (a[1] - k[1]) ** 2) <= (a[2] + k[2] ) ** 2:
      continue
    else:
      print(a, k)
      ans += 1

  print(ans)
