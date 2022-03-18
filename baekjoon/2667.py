import sys
input = sys.stdin.readline

n = int(input())
dic = {}

for i in range(n):

    temp = str(input())
    for s in range(n):
        if temp[s] == '1':
            if i not in dic:
                dic[i] = [s]
            else:
                dic[i].append(s)

visited = []
start = next(iter(dic))
stack = [start]

while stack:

    node = stack.pop()
    if node not in visited:
        visited.append(node)
        stack.extend(dic[node])
