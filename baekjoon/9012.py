import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
  
  line = str(input())[:-1]

  if len(line) % 2 != 0:
    print("NO")
    continue

  else:
    temp = []
    con = False
    for j in range(len(line)):
      if line[j] == '(':
        temp.append('(')
      else:
        if not temp:
          print("NO")
          con = True
          break
        else:
          temp.pop()

    if temp:
      print("NO")
    elif not con:
      print("YES")
