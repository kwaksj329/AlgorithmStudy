import sys
input = sys.stdin.readline

n = int(input())
nums = {}
nums[0] = [0, 0, 0]

for i in range(n):
    temp = int(input())
    nums[i+1] = [temp, temp, temp]

for i in range(2, n+1):

    if i == 2:
        nums[i][0] += nums[i-1][1]
        nums[i][1] += max(nums[i-2])
        continue

    nums[i][0] += max(nums[i-1][1], nums[i-1][2])
    nums[i][1] += max(nums[i-2])
    nums[i][2] += max(nums[i-3])

if n == 1:
    print(nums[1][0])
else:
    print(max(nums[n-1][0], nums[n-1][1], nums[n-1][2], nums[n][0], nums[n][1], nums[n][2]))