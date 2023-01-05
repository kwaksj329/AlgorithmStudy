import sys
input = sys.stdin.readline

n = int(input())
all = []
i = 1
ans = ""
nono = False
for k in range(n):
  
  num = int(input())

  while True:
    if all:
      if all[-1] == num:
        all.pop()
        ans += '-'
        break

      if all[-1] > num:
        if num in all:
          nono = True
          break

    all.append(i)
    i += 1
    ans += '+'

if not nono:
  for s in ans:
    print(s)

else:
  print("NO")
