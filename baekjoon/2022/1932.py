import sys
input = sys.stdin.readline

n = int(input())
all = []

for i in range(n):
    temp = list(map(int, input().split()))
    all.append(temp)

for i, a in enumerate(all):
    if i == 0:
        continue
    
    for j, v in enumerate(a):
        if j == 0:
            all[i][j] += all[i-1][0]
        elif j == len(a)-1:
            all[i][j] += all[i-1][-1]

        else:
            all[i][j] += max(all[i-1][j-1], all[i-1][j])
    
print(max(all[i]))