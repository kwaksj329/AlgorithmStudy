import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
s = []
for i in range(n):
  s.append(list(map(int, input().split())))

people = [ i for i in range(0, n)]
combi = list(combinations(people, n//2))
#print(combi)
half = n//2
end = len(combi)-1
min = 100 * n//2
#print(len(combi))
for ci in range(len(combi)//2):
  a = 0
  b = 0
  c = combi[ci]
  sub_c = combi[end-ci]
  for i in range(1, half):
    for j in range(0, half-i):
#      print(c[j+i], c[j], sub_c[j+i], sub_c[j])
      a += s[c[j+i]][c[j]]
      a += s[c[j]][c[j+i]]
      b += s[sub_c[j+i]][sub_c[j]]
      b += s[sub_c[j]][sub_c[j+i]]
#  print(a, b)
  if abs(a - b) < min:
    min = abs(a-b)

print(min)
