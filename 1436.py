import sys
input = sys.stdin.readline

n = int(input())

six = 666
answer = 0

while answer < n:
  
  if '666' in str(six):
    answer += 1
  six += 1

print(six-1)
