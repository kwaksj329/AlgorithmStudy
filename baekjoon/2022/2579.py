import sys
input = sys.stdin.readline

n = int(input())

all = {}

for i in range(n):
    temp = int(input())
    all[i] = [temp, temp]

if n > 2:
    all[1][0] += all[0][0]

    for i in range(2, n):

        all[i][1] += max(all[i-2])
        all[i][0] += all[i-1][1]

    ans = max(all[n-1])

    print(ans)

else:
    if n == 1:
        print(all[0][0])
    elif n == 2:
        print(all[0][0] + all[1][0])

