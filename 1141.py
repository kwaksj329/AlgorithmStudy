import sys
input = sys.stdin.readline

n = int(input())
words = []

for i in range(0, n):
  words.append(str(input())[:-1])

temp = set(words)
words = list(temp)

result = len(words)
n = len(words)

for i in range(0, n):
  now = False

  for j in range(0, n):
    if i == j:
      continue
    elif (words[j]).startswith(words[i]):
      now = True
  
  if now is True:
    result -= 1

print(result)
