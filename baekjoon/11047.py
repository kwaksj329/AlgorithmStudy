import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = [ 0 for i in range(n)]
for i in range(n):
  a[i] = int(input())

ans = 0

for coin in a[::-1]:
  if coin <= k:
    ans += k // coin
    k -= (k // coin) * coin

print(ans)
