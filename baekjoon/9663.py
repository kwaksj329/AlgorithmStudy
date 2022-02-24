import sys
import copy
input = sys.stdin.readline

def chess(x, y, board, n):
 
  for a in range(n):
    if a == y:
      for b in range(n):
        board[a][b] = 1
    for b in range(n):
      board[b][x] = 1
      if x+b <= n-1:
        board[b][x+b] = 1
      if x-b >= 0:
        board[b][x-b] = 1

  if y+1 == n:
    global ans
    ans+= 1

  else:
    for j in range(n):
      if board[y+1][j] == 0:
        innew = copy.deepcopy(board)
        chess(j, y+1, innew, n)

n = int(input())
board = [ [ 0 for j in range(n)] for i in range(n)]
ans = 0
answer = 0
for i in range(1):
  new = copy.deepcopy(board)
  chess(i, 0, new, n)
  print(ans)
print(ans)
