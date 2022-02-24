import sys
input = sys.stdin.readline

line = str(input()[:-1])

met = False
temp = ''
number = []
porm = []
for i in line:
  if i != '+' and i != '-':
    temp += i
  else:
    number.append(int(temp))
    temp = ''
    porm.append(i)

number.append(int(temp))

ans = number[0]
met = False
for i, v in enumerate(porm):
  if v == '-':
    met = True

  if met is True:
    ans -= number[i+1]

  else:
    ans += number[i+1]

print(ans)
