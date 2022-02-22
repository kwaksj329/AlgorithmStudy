import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = []

for i in range(n):
  board.append(str(input())[:-1])

minnum = 64
for x in range(m-7):
  for y in range(n-7):
    white = 0
    black = 0
    for j in range(x, x+8):
      for i in range(y, y+8):
        if (i + j) % 2 == 0:
          if board[i][j] == 'W':
            black += 1
          else:
            white += 1
        else:
          if board[i][j] == 'B':
            black += 1
          else:
            white += 1
    if min(white, black) < minnum:
      minnum = min(white, black)

print(minnum)
