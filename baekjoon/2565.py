import sys
input = sys.stdin.readline

n = int(input())
all = []
for i in range(n):
    temp = list(map(int, input().split()))
    all.append(temp)

all.sort()
right = [ [i[1], 0] for i in all ]

for i, num in enumerate(right):

    if i == 0:
        right[0][1] = 1
        continue

    temp = 0
    find = False
    for r in right[:i]:

        if r[0] < num[0] and r[1] + 1 > temp:
            temp = r[1] + 1
            find = True

    if find is True:
        right[i][1] = temp
    else:
        right[i][1] = 1

answer = 0
i = 1
for num in right:

    if num[1] == i:
        answer += 1
        i += 1

print(n-answer)
