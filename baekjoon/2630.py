import sys
input = sys.stdin.readline

n = int(input())
board = []

for i in range(n):
  board.append(list(map(int, input().split())))

#global wnum
wnum = 0
#global bnum
bnum = 0

def paper(board):

  global wnum
  global bnum
  same = True
  white = False
  blue = False

  allw = board[0][0]
  for b in board:
    for a in b:
      if a != allw:
        same = False
        break

  if same:
    if allw == 0:
      white = True
    elif allw == 1:
      blue = True

  if not white and not blue:
    first = []
    second = []
    third = []
    fourth = []
    for i, b in enumerate(board):
      if i <= len(board)//2 -1:
        first.append(b[:len(b)//2])
        second.append(b[len(b)//2:])
      else:
        third.append(b[:len(b)//2])
        fourth.append(b[len(b)//2:])

    paper(first)
    paper(second)
    paper(third)
    paper(fourth)

  elif white or blue:
    if white:
      wnum += 1
    elif blue:
      bnum += 1

paper(board)

print(wnum)
print(bnum)
