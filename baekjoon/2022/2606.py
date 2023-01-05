import sys
input = sys.stdin.readline

comnum = int(input())
n = int(input())
dic = {}

for i in range(n):
    temp = list(map(int, input().split()))
    if temp[0] not in dic:
        dic[temp[0]] = [temp[1]]
    else:
        dic[temp[0]].append(temp[1])
    if temp[1] not in dic:
        dic[temp[1]] = [temp[0]]
    else:
        dic[temp[1]].append(temp[0])

visited = []
stack = [1]
while stack:

    node = stack.pop()
    if node not in visited:
        visited.append(node)
        stack.extend(dic[node])

print(len(visited)-1)