import sys
from itertools import product
input = sys.stdin.readline

n = int(input())
answer = False
for num in range(0, n+1):
  
  sum = 0
  temp = str(num)
  
  for i in temp:
    sum += int(i)
  sum += num

  if sum == n:
    print(num)
    answer = True
    break

if answer is False:
  print(0)
