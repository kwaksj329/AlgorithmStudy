import sys
input = sys.stdin.readline

sudoku = []

for i in range(9):
  sudoku.append(map(int, input().split()))

print(sudoku)
