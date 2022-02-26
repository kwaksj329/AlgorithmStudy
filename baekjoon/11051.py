import sys
import math
input = sys.stdin.readline

n, k = map(int, input().split())

ans = math.comb(n, k)
ans = ans % 10007

print(ans)
