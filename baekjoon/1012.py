import sys
input = sys.stdin.readline

t = int(input())
nx = [0, 0, -1, 1]
ny = [1, -1, 0, 0]

for i in range(t):

    m, n, k = map(int, input().split())
    ans = 0

    visited = []
    temp = list(map(int, input().split()))
    stack = [temp]
    all = [temp]
    for i in range(k-1):
        all.append(list(map(int, input().split())))

    while stack:

        node = stack.pop()

        if node not in visited:
            visited.append(node)
            for four in range(4):
                x = node[0] + nx[four]
                y = node[1] + ny[four]
                if x < 0 or y < 0 or x > m-1 or y > n-1:
                    continue
                if [x, y] in all:
                    stack.append([x, y])

        if not stack and len(visited) < k:
            for a in all:
                if a not in visited:
                    stack.append(a)
                    ans += 1
                    break

    print(ans+1)
