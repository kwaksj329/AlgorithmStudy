import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
all = {}
nums = []

for i in range(m):
    temp = list(map(int, input().split()))
    nums.append(temp)

for temp in nums:
    if temp[0] not in all:
        all[temp[0]] = [temp[1]]
    else:
        all[temp[0]].append(temp[1])
    if temp[1] not in all:
        all[temp[1]] = [temp[0]]
    else:
        all[temp[1]].append(temp[0])

for k, value in all.items():
    all[k].sort()

stack = [v]
ans = []

while stack:
    
    node = stack.pop()

    if node not in ans:
        ans.append(node)
        if node in all:
            stack.extend(all[node][::-1])

print(*ans)

queue = [v]
ans = []

while queue:

    start = queue.pop(0)

    if start not in ans:
        ans.append(start)
        if node in all:
            queue.extend(all[start])

print(*ans)
