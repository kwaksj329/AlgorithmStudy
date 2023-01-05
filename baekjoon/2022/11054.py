import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

maxnum = 1
maxi = 0
all = [ [i, 0] for i in nums ]

for i, num in enumerate(all):

    if i == 0:
        all[i][1] = 1
        continue

    find = False
    temp = 0
    for before in reversed(all[:i]):
        if before[0] < num[0] and before[1] + 1 > temp:
            temp = before[1] + 1
            find = True

    if find is False:
        all[i][1] = 1
    else:
        all[i][1] = temp

    if temp > maxi:
        maxnum = temp
        maxi = i

beforeall = all[::]
nums = nums[::-1]

maxnum = 1
maxi = 0
all = [ [i, 0] for i in nums ]

for i, num in enumerate(all):

    if i == 0:
        all[i][1] = 1
        continue

    find = False
    temp = 0
    for before in reversed(all[:i]):
        if before[0] < num[0] and before[1] + 1 > temp:
            temp = before[1] + 1
            find = True

    if find is False:
        all[i][1] = 1
    else:
        all[i][1] = temp

    if temp > maxi:
        maxnum = temp
        maxi = i

afterall = all[::-1]
maximum = 0
for i in range(n):

    if afterall[i][1] + beforeall[i][1] > maximum:
        maximum = afterall[i][1] + beforeall[i][1]

print(maximum-1)
