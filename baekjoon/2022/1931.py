import sys
input = sys.stdin.readline

n = int(input())
ans = 0
alltime = []
maxn = 0
for i in range(n):
  start, end = map(int, input().split())
  alltime.append([start, end])

end = 0
num = [0 for i in range(maxn+1)]
alltime.sort()
alltime = sorted(alltime, key = lambda x : x[1])
for a in alltime:
  x = a[0]
  y = a[1]
  if end <= x:
    end = y
    ans += 1
print(ans)
