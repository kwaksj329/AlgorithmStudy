import sys
input = sys.stdin.readline

n = int(input())

all = [0] * (1000001)
all[1] = 0
all[2] = 1
all[3] = 1
all[4] = 2

for i in range(5, n+1):
    
    all[i] = all[i-1] + 1
    if i % 3 == 0:
        all[i] = min(all[i], all[i//3] + 1)
    if i % 2 == 0:
        all[i] = min(all[i], all[i//2] + 1)

print(all[n])

