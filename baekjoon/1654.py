import sys
input = sys.stdin.readline

k, n = map(int, input().split())
all = []

for i in range(k):
  all.append(int(input()))

start = 1
mani = max(all)
end = mani

while start <= end:

  mid = (start + end) // 2
  ans = 0

  for a in all:
    ans += a // mid

  if ans >= n:
    start = mid + 1
  elif ans < n:
    end = mid -1

print(end)
