import sys
input = sys.stdin.readline

n = int(input())
numbers = []

for i in range(n):
  numbers.append(int(input()))

numbers.sort()

for n in numbers:
  print(n)
