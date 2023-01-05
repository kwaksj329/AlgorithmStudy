import sys
from collections import deque
mod = 10 ** 9
input = sys.stdin.readline

n = int(input())

mm = [[0] * 10 for _ in range(n+2)]
mm[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, n +1):
    mm[i][0] = mm[i-1][1]
    mm[i][9] = mm[i-1][8]
    for j in range(1, 9):
        mm[i][j] = mm[i-1][j-1] + mm[i-1][j+1]

print(sum(mm[n]) % mod)