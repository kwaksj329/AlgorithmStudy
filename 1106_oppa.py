import sys
input = sys.stdin.readline

c, n = map(int, input().split())
cost_list = [0] * 100001
costs = []
for i in range(n):
    cost, customer = map(int, input().split())
    cost_list[cost] = max(customer, cost_list[cost])
    costs.append(cost)
i = 0
while cost_list[i] < c:
    i+=1
    for cost in costs:
        if i >= cost:
            cost_list[i] = max(cost_list[i], cost_list[cost] + cost_list[i-cost])
print(i)
