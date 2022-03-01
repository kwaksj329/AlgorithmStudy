import sys
import heapq
input = sys.stdin.readline

n = int(input())
leftheap = []
rightheap = []

for i in range(n):

    num = int(input())

    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, -num)
    else:
        heapq.heappush(rightheap, num)


    if rightheap and -leftheap[0] > rightheap[0]:
        left = heapq.heappop(leftheap)
        right = heapq.heappop(rightheap)
        heapq.heappush(leftheap, -right)
        heapq.heappush(rightheap, -left)

    print(-leftheap[0])
