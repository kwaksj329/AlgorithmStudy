import sys
input = sys.stdin.readline

def star(n, x, y):
  if n == 3:
    allstar[x][y] = 1
    allstar[x+1][y] = 1
    allstar[x+2][y] = 1
    allstar[x][y+1] = 1
    allstar[x+2][y+1] = 1
    allstar[x][y+2] = 1
    allstar[x+1][y+2] = 1
    allstar[x+2][y+2] = 1
  
  else:
    star(n//3, x, y)
    star(n//3, x+n//3, y)
    star(n//3, x+(2*n)//3, y)
    star(n//3, x, y+n//3)
    star(n//3, x+(2*n)//3, y+n//3)
    star(n//3, x, y+(2*n)//3)
    star(n//3, x+n//3, y+(2*n)//3)
    star(n//3, x+(2*n)//3, y+(2*n)//3)

n = int(input())
allstar = [[ 0 for i in range(n)] for j in range(n)]
star(n, 0, 0)

for i in allstar:
  for j in i:
    if j == 1:
      print('*', end='')
    else:
      print(' ', end='')
  print()
