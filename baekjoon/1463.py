import sys
input = sys.stdin.readline

n = int(input())

all = [0] * (n+1)
all[1] = 1
all[2] = 1
all[3] = 1
all[4] = 2

for i in range(5, n+1):

    num = i
    a = i -1
    b = i -1
    c = i -1
    if i % 3 == 0:
        a = i // 3
    elif i % 2 == 0:
        b = i // 2
    else:
        c = i - 1
    
    all[num] = 1 + min(all[a], all[b], all[c])
    
print(all[n])

