import sys
input = sys.stdin.readline

c, n = map(int, input().split())

all = {}

for i in range(1, n+1):
  money, people = map(int, input().split())
  all[money] = people

for m in range(1, 1001):
  if m in all:
    person = all[m]
  else:
    person = 0

  for i in range(1, m//2+1):
    if i in all and m-i in all:
      if all[i] + all[m-i] > person:
        person = all[i] + all[m-i]
      elif person == 0:
        person = all[i] + all[m-i]
    else:
      continue 

  if person != 0:
    all[m] = person
  print(all)
  if person >= c:
    print(m)
    break
