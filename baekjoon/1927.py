import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):

    num = int(input())

    if num == 0 and not heap:
        print(0)
    elif num == 0 and heap:
        print(heapq.heappop(heap))
    elif num != 0:
        heapq.heappush(heap, num)