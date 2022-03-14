import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
all = [ [i, 0] for i in nums]

for i, a in enumerate(all):

    if i == 0:
        all[i][1] = 1
        continue

    find = False
    temp = 0
    for before in reversed(all[:i]):

        if a[0] > before[0] and before[1] + 1 > temp:
            temp = before[1] + 1
            find = True

    if find is False:
        all[i][1] = 1
    else:
        all[i][1] = temp

ans = 0
i = 1
for number in all:

    if number[1] == i:
        ans += 1
        i += 1

print(ans)
