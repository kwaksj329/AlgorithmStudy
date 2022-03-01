import sys
input = sys.stdin.readline

n = int(input())
paper = []
for i in range(n):
  paper.append(list(map(int, input().split())))

zero = 0
minus = 0
plus = 0

def split(paper):
  global zero
  global minus
  global plus

  first = paper[0][0]
  same = True
  for p in paper:
    for i in p:
      if i != first:
        same = False
        break
    if not same:
      break

  if same:
    if first == 0:
      zero += 1
    elif first == -1:
      minus += 1
    elif first == 1:
      plus += 1

  else:
    one = []
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    eight = []
    nine = []

    for i, p in enumerate(paper):
      if i < len(p)//3:
        one.append(p[:len(p)//3])
        two.append(p[len(p)//3:2*len(p)//3])
        three.append(p[2*len(p)//3:])
      elif len(p)//3 <= i < 2*len(p)//3:
        four.append(p[:len(p)//3])
        five.append(p[len(p)//3:2*len(p)//3])
        six.append(p[2*len(p)//3:])
      else:
        seven.append(p[:len(p)//3])
        eight.append(p[len(p)//3:2*len(p)//3])
        nine.append(p[2*len(p)//3:])


    split(one)
    split(two)
    split(three)
    split(four)
    split(five)
    split(six)
    split(seven)
    split(eight)
    split(nine)

split(paper)
print(minus)
print(zero)
print(plus)
