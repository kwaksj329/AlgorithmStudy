import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
dic = {}

for i in range(n):
    
    num = int(input())

    if num == 0 and not heap:
        print(0)
    elif num == 0 and heap:
        mini = heapq.heappop(heap)
        if -mini in dic:
            if dic[-mini] > 0:
                dic[-mini] -= 1
                print(-mini)
                continue

        if mini in dic:
            if dic[mini] > 0:
                dic[mini] -= 1
                print(mini)
                continue

    elif num != 0:
        if num < 0:
            heapq.heappush(heap, -num)
        else:
            heapq.heappush(heap, num)
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1