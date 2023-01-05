import sys
input = sys.stdin.readline
line = ""

while line != '.':
  line = str(input())[:-1]
  no = False
  temp = []
  for i in range(len(line)):
    if line[i] == '(' or line[i] == '[':
      temp.append(line[i])
      continue

    elif line[i] == ')':
      if not temp:
        print("no")
        no = True
        break
      else:
        letter = temp.pop()
        if letter != '(':
          print("no")
          no = True
          break

    elif line[i] == ']':
      if not temp:
        print("no")
        no = True
        break
      else:
        letter = temp.pop()
        if letter != '[':
          print("no")
          no = True
          break

  if line == '.':
    break

  if not no and not temp:
    print("yes")
    continue

  if not no and temp:
    print("no")
    continue
