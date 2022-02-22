import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = [[ 0 for j in range(0, m)] for i in range(0, n)]

for i in range(0, n):
  temp = input()
  for j in range(0, m):
    board[i][j] = int(temp[j])

if n > m:
  max = n
  min = m
else:
  max = m
  min = n

result = 1

for i in range(2, min+1):
  for a in range(0, n - i + 1):
    for b in range(0, m - i + 1):
      if( board[a][b] == board[a + i -1][b] == board[a][b + i -1] == board[a + i -1][b + i -1] ):
        result = i

print(result ** 2)
