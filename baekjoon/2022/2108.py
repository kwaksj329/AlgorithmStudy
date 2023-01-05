import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
all = []

for i in range(n):
  all.append(int(input()))

one = sum(all) / n
one = int(round(one, 0))

all.sort()
two = all[int(n / 2)]

cnt = Counter(all)
threetemp = cnt.most_common()
mosttemp = []
most = threetemp[0][1]
for t in threetemp:
  if most == t[1]:
    mosttemp.append(t)
mosttemp.sort()
if len(mosttemp) > 1:
  three = mosttemp[1][0]
else:
  three = mosttemp[0][0]

four = all[-1] - all[0]

print(one, two, three, four, sep=' ')
