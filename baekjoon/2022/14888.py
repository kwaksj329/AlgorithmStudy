import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
all = list(map(int, input().split()))
min = 1000000000
max = -1000000000
math = []
for i, b in enumerate(all):
  if i == 0:
    for j in range(b):
      math.append('plus')
  elif i == 1:
    for j in range(b):
      math.append('minus')
  elif i == 2:
    for j in range(b):
      math.append('mul')
  elif i == 3:
    for j in range(b):
      math.append('div')

all = list(permutations(math, n-1))
all = list(set(all))

for m in all:
  for i, number in enumerate(a):
    if i == 0:
      temp = a[0]
      continue
    if m[i-2] == 'plus':
      temp += number
    elif m[i-2] == 'minus':
      temp -= number
    elif m[i-2] == 'mul':
      temp *= number
    elif m[i-2] == 'div':
      if number > 0:
        temp = int(temp / number)
      else:
        number = -number
        temp = -(int(temp / number))

  if temp > max:
    max = temp
  if temp < min:
    min = temp

print(max, min)
