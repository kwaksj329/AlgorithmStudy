import sys
input = sys.stdin.readline

a, b = map(int, input().split())
tempa = a
tempb = b
ina = []
inb = []
i = 2

for i in range(1, a+1):  
  if a % i == 0:
    ina.append(i)

for i in range(1, b+1):
  if b % i == 0:
    inb.append(i)

if a > b:
  min = inb
  max = ina
else:
  max = inb
  min = ina

first = 1
for i in min:

  if i in max:
    first = i

print(first)

print(tempa * tempb // first)
