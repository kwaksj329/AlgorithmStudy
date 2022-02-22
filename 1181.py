import sys
input = sys.stdin.readline

n = int(input())
words = []

for i in range(n):
  letter = str(input())[:-1]
  if letter in words:
    continue
  else:
    words.append(letter)

words.sort()

all = [[] for i in range(0, 51)]

for w in words:
  all[len(w)].append(w)

for a in all:
  if a:
    for answer in a:
      print(answer)
