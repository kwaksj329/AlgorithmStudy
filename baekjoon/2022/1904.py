import sys
import math
input = sys.stdin.readline

n = int(input())

left = n
right = 0
ans = 0

arr = [0] * 1000001
arr[1] = 1
arr[2] = 2

for i in range(3, 1000001):
    arr[i] = arr[i-1] + arr[i-2]
    if arr[i] >= 15746:
        arr[i] = arr[i] % 15746
    if n == i:
        break

print(arr[n])