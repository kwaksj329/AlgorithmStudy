import sys
input = sys.stdin.readline

global sudoku
sudoku = []
zeros = []
for i in range(9):
  temp = list(map(int, input().split()))
  for index, j in enumerate(temp):
    if j == 0:
      zeros.append((i, index))
  sudoku.append(temp)

def check(x, y, n):
  for i in range(9):
    if sudoku[x][i] == n:
      return False
    if sudoku[i][y] == n:
      return False
  
  startx = (x // 3) * 3
  starty = (y // 3) * 3

  for i in range(starty, starty+3):
    for j in range(startx, startx+3):
      if sudoku[j][i] == n:
        return False
  return True

def recur(i):
  if i >= len(zeros):
    return True
  
  else:
    for num in range(1, 10):
      if check(zeros[i][0], zeros[i][1], num) is False:
        continue
      sudoku[zeros[i][0]][zeros[i][1]] = num
      if(recur(i+1)):
        return True
    sudoku[zeros[i][0]][zeros[i][1]] = 0
    return False

recur(0)
for i in range(9):
  print(*sudoku[i])
