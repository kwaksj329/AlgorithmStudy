import sys
input = sys.stdin.readline

n = int(input())
number = []
for i in range(n):
  a = int(input())
  if a != 0:
    number.append(a)

  else:
    number.pop()

print(sum(number))
