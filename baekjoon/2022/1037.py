import sys
input = sys.stdin.readline

number = int(input())
all = list(map(int, input().split()))
n = all[0]

for a in all:
  
  if n % a == 0:
    continue

  else:
    for i in range(2, a+1):
      if (n*i) % a == 0:
        n = n * i
        break

if n == max(all):
  n *= min(all)

print(n)
