import sys
input = sys.stdin.readline

n = int(input())
money = list(map(int, input().split()))

money.sort()

for i in range(1, n):
  money[i] = money[i-1] + money[i]

print(sum(money))
